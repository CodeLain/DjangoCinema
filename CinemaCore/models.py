from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from CinemaCore import constants as const
from django.contrib.auth.models import UnicodeUsernameValidator


class User(AbstractUser):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    avatar = models.ImageField(upload_to='avatars', default=const.DEFAULT_PROFILE_IMAGE_USER)
    email = models.EmailField(unique=True, db_index=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    is_active = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)


    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        # min_length=4,
        max_length=20,
        unique=True,
        help_text='Required. 20 characters or fewer. Letters, digits and @/./+/-/_ only.',
        validators=[username_validator],
        error_messages={
            'unique': "A user with that username already exists.",
        },
    )

    @property
    def is_employee(self):
        return False

    @property
    def is_client(self):
        return False

    def save(self, *args, **kwargs):
        """
        Save user and if user is superuser, activate it.
        """
        if not self.id and self.is_superuser:
            self.is_active = True
        super(User, self).save(*args, **kwargs)


class Employee(User):
    administrator = models.BooleanField(default=False, help_text='Tick to give access to the admin page.',)

    class Meta:
        verbose_name = "Employee"

    @property
    def is_employee(self):
        return True

    def is_staff(self):
        "Will the employee have access to the admin?"
        return self.administrator


class Client(User):
    is_special_client = models.BooleanField(default=False, help_text='Tick to mark as a special client.',)

    class Meta:
        verbose_name = "Client"

    @property
    def is_client(self):
        return True