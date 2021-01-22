from dateutil import parser
import json
import csv, io
import mimetypes
import os
from django.conf import settings
from django.views.static import serve
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import get_template
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from dashboard import forms, models
from django.db.models import Count, Q
from authentication.utils import signup_invite_email
from dashboard.decorators import check_admin


def pretty_date(date):
    d = parser.parse(date)
    return d.strftime("%Y-%m-%d")

# @login_required
# @check_admin
# def ResendInviteEmail(request, *args, **kwargs):
#     register_email = get_object_or_404(models.Entity, pk=kwargs["id"])
#     email = register_email.admin_email
#     if email is not None:
#         signup_invite_email(request, email)
#         messages.success(
#             request, "Invitation email has been re-sent successfully!"
#         )
#     else:
#         messages.warning(request, "An error occured while sending email")
#     return redirect(reverse("dashboard:entities"))


# HOME List View
@login_required
# @check_admin
def Homes(request):
    homes = models.Home.objects.all()
    context = {
        'dash_title': 'Homes',
        'homes': homes,
    }
    return render(request, 'dashboard/home/home.html', context)

# ADD HOME VIEW
@login_required
@check_admin
def AddHome(request, *args, **kwargs):
    form = forms.HomeForm()
    if request.method == 'POST':
        form = forms.HomeForm(request.POST)
        if form.is_valid():
            owner_email = form.cleaned_data['owner_email']
            owner_name = form.cleaned_data['owner_name']
            phone_number = form.cleaned_data['phone_number']

            signup_invite_email(request, owner_email)
            instance = form.save()
            home = models.Home.objects.get(pk=instance.id)

            tenantObj = models.Tenant.objects.create(
                home=home,
                name=owner_name, 
                email=owner_email,
                phone_number=phone_number,
                is_staff=True 
            )
            tenantObj.save()

            messages.success(
                request, f"Home has been added and a registration invite email has been sent this email {owner_email}!"
            )
            return redirect('dashboard:homes')
    context = {
        'dash_title': 'Add New Home',
        "form": form,
    }
    return render(request, 'dashboard/home/add.html', context)







# @login_required
# @check_admin
# def ViewEntity(request, *args, **kwargs):
#     _id = kwargs["id"]
#     entity = get_object_or_404(models.Entity, pk=kwargs["id"])
    
#     context = {
#         "dash_title": 'View Entity',
#         "entity": entity
#     }
#     return render(request, "dashboard/view-entity.html", context)


# Delte Entity View
@login_required
@check_admin
def DeleteHome(request, *args, **kwargs):
    _id = kwargs["id"]
    home = get_object_or_404(models.Home, pk=kwargs["id"])
    tenant_qs = models.Tenant.objects.filter(home=home, email=home.owner_email)
    if tenant_qs.exists():
        tenant = tenant_qs[0]
        if tenant.user is not None:
            get_object_or_404(User, pk=tenant.user.id).delete()
    home.delete()

    messages.success(request, "Home deleted successfully")
    return redirect(reverse("dashboard:homes"))


# Edit Home View
@login_required
@check_admin
def EditHome(request, *args, **kwargs):
    home = get_object_or_404(models.Home, pk=kwargs["id"])
    old_email = home.owner_email
    form = forms.HomeForm(instance=home)
    if request.method == 'POST':
        form = forms.HomeForm(request.POST, instance=home)
        if form.is_valid():
            owner_email = form.cleaned_data['owner_email']
            owner_name = form.cleaned_data['owner_name']
            phone_number = form.cleaned_data['phone_number']

            if old_email != owner_email:
                signup_invite_email(request, owner_email)
            instance = form.save()

            models.Tenant.objects.filter(user=request.user).update(
                home=instance,
                email=owner_email,  
                name=owner_name,  
                phone_number=phone_number
            )

            messages.success(request, 'Home has been updated!')
            return redirect('dashboard:homes')

    context = {
        'dash_title': 'Edit Home',
        'form': form,
        # 'entity': entity,
    }
    return render(request, 'dashboard/home/edit.html', context)


