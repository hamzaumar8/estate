import itsdangerous
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.contrib.auth import  logout
from .forms import CustomSignupForm
from dashboard import models as dashModel
from dashboard.decorators import unauthenticated_user



@unauthenticated_user
def registration(request, *args, **kwargs):
    serializer = itsdangerous.TimedSerializer(
        settings.ITSDANGEROUS_KEY,
        serializer=itsdangerous.URLSafeSerializer(settings.ITSDANGEROUS_KEY),
    )
    try:
        serializer.loads(kwargs["token"],max_age=settings.ITSDANGEROUS_EXPIRE_PERIOD, salt="signup")
    except itsdangerous.SignatureExpired:
        msg = "Link has expired. Please contact department administrator for new link"
        return HttpResponse(msg)
    except itsdangerous.BadSignature:
        return HttpResponseNotFound("Page Not Found")

    form = CustomSignupForm(prefix="user_form")

    if request.method == "POST":
        form_email = request.POST.get("user_form-email", None)
        email_qs = dashModel.Tenant.objects.filter(email=form_email)
        if email_qs.exists():
            obj = email_qs[0]
            form = CustomSignupForm(request.POST, prefix="user_form")
            if form.is_valid():
                user = form.save(request)
                if ' ' in obj.name:
                    user.first_name = obj.name.split(' ')[0]
                    user.last_name = obj.name.split(' ')[1]
                else:
                    user.first_name = obj.name
                user.is_staff = obj.is_staff
                email_qs.update(user=user, pending=False)
                user_profile = user.profile
                user_profile.entity = obj.entity
                user.save() 
                user_profile.save()
                messages.success(request,"Account created successfully. Please login to proceed",
                )
                return HttpResponseRedirect(reverse("account_login"))
        else:
            messages.warning(request, f"Email does not have invitation to signup on this portal!")
            return HttpResponseRedirect(request.path_info)

    context = {"form": form}
    return render(request, "account/signup.html", context)



@login_required
def authLogout(request):
    logout(request)
    messages.success(request, "You have signed out.")
    return redirect('account_login')