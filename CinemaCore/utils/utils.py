import urllib.parse
from django.utils import timezone

from django.template.loader import render_to_string, get_template
from django.template import Context
from django.core.mail import send_mail, EmailMessage

from CinemaCore import constants as const
def send_activation_account_email(new_user):
    server = 'localhost:8000/'
    token = str(new_user.token.value)
    url = server + token

    ctx = {
        'url': url,
    }
    message = get_template('email.html').render(ctx)
    # message = render_to_string('email.html', ctx)
    msg = EmailMessage('TEST EMAIL', message, 'account@cinema_app.com',
                       [new_user.email, ])
    msg.content_subtype = 'html'
    msg.send()


def default_expiration_delta():
    """
    Generates the default expiration delta
    :return: Default time delta
    """
    return timezone.now() + const.EXPIRY_TOKEN_DELTA
