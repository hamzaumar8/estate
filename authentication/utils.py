from django.conf import settings
from itsdangerous import TimedSerializer, URLSafeSerializer
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from django.template.loader import get_template
# from .models import Logs

email_from = settings.EMAIL_FROM_ADDRESS

def gen_model_id(moduleName):
    moduleInstance = moduleName.objects.last()
    if moduleInstance is not None:
        return (moduleInstance.id + 1)
    return 1


def generate_signup_token(email):
    serializer = TimedSerializer(
        settings.ITSDANGEROUS_KEY,
        serializer=URLSafeSerializer(settings.ITSDANGEROUS_KEY),
    )
    return serializer.dumps(email, salt="signup")



def generate_ip_address(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def quarter_email(request,email, subject, message):
    # url = request.build_absolute_uri(reverse("account_login"))
    # html = get_template("dashboard/emails/quatermail.html")
    # content = html.render({"url": url, "content": message})
    # "Quarterly Report for OAG Asset Management Portal",
    try :
        mail = EmailMessage(
            subject,
            message,
            email_from,
            to=[email],
            headers={'MY-UNIQUE-HEAD':  'Administrator General Office'},
        )
        mail.content_subtype = "html"
        mail.send(fail_silently=False)
    except:
        messages.warning(request, f"Either the attachment's size is big or corrupt")
        return HttpResponseRedirect(request.path_info)


def quarter_email_attachment(request,email, subject, message, attachment):
    try :
        mail = EmailMessage(
            subject,
            message,
            email_from,
            to=[email],
            headers={'MY-UNIQUE-HEAD':  'Administrator General Office'},
        )
        mail.attach(attachment.name, attachment.read(), attachment.content_type)
        mail.content_subtype = "html"
        mail.send(fail_silently=False)
    except:
        messages.warning(request, f"Either the attachment's size is big or corrupt")
        return HttpResponseRedirect(request.path_info)


def signup_invite_email(request, email):
    url = request.build_absolute_uri(reverse("authentication:signup", kwargs={"token": generate_signup_token(email)}))
    html = get_template("authentication/emails/registration.html")
    content = html.render({"url": url})
    msg = "Kindly visit %s to create an account" % url
    send_mail(
        "Registration for OAG Asset Management Portal ",
        msg,
        email_from,
        [email],
        fail_silently=False,
        html_message=content,
    )




