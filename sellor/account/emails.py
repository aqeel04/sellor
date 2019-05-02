from celery import shared_task
from django.conf import settings
from django.urls import reverse
from templated_email import send_templated_mail
from django.core.mail import send_mail, EmailMultiAlternatives, EmailMessage
from django.template.loader import get_template, render_to_string
from django.utils.crypto import get_random_string

from ..core.emails import get_email_base_context
from ..core.utils import build_absolute_uri


def send_email_verification_mail(recipient):
    conf_url = build_absolute_uri(
        reverse(
            'account:email-verified'
        )
    )
    context = get_email_base_context()
    context['conf_url'] = conf_url
    send_templated_mail(
        template_name="account/verify_email",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[recipient],
        context=context
    )


@shared_task
def send_password_reset_email(context, recipient):
    reset_url = build_absolute_uri(
        reverse(
            'account:reset-password-confirm',
            kwargs={
                'uidb64': context['uid'],
                'token': context['token']}))
    context = get_email_base_context()
    context['reset_url'] = reset_url
    send_templated_mail(
        template_name='account/password_reset',
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[recipient],
        context=context)


@shared_task
def send_account_delete_confirmation_email(token, recipient_email):
    delete_url = build_absolute_uri(
        reverse('account:delete-confirm', kwargs={'token': token}))
    ctx = get_email_base_context()
    ctx['delete_url'] = delete_url
    send_templated_mail(
        template_name='account/account_delete',
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[recipient_email],
        context=ctx)
