import random
import string
from django.utils import timezone
from django.utils.text import slugify
from django.template.loader import get_template
from django.core.mail import EmailMessage

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


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, new_slug=None):
    slug = new_slug or getattr(instance, "name") or getattr(instance, "title")
    if slug:
        slug = slugify(slug)
    else:
        slug = str(instance.id)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug,
            randstr=random_string_generator(size=5)
        )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug
