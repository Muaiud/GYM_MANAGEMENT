import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserManager(BaseUserManager):

    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True, **extra_fields)


class LowercaseEmailField(models.EmailField):
    """
    Override EmailField to convert emails to lowercase before saving.
    """

    def to_python(self, value):
        value = super(LowercaseEmailField, self).to_python(value)
        return value.lower()


class User(AbstractBaseUser, PermissionsMixin):
    """
    User Table, which will provide login functionality
    A fully featured User model with admin-compliant permissions that uses
    a full-length email field as the username.

    Required:
        email
        password
        first_name
        last_name
        phone_no
    """
    email = LowercaseEmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(_('staff status'), default=False)
    is_superuser = models.BooleanField(_('superuser'), default=False)
    is_active = models.BooleanField(_('active'), default=True)
    user_id = models.UUIDField(default=uuid.uuid4, unique=True)
    joined_on = models.DateTimeField(auto_now_add=True)
    sub_expired_on = models.DateTimeField(null=True, blank=True)

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['name']

    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return f'{self.email} {self.sub_expired_on}'