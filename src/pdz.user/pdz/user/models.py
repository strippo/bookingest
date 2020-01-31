# coding:utf-8
import datetime
from pdz.user.validators import validate_email_admin
from django.core import validators

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import PermissionsMixin, \
                                             AbstractBaseUser, UserManager, AbstractUser
from django.utils import timezone




class EmailUserManager(UserManager):
    def create_superuser(self, email, password, **extra_fields):
        return super(EmailUserManager, self).create_superuser(email,
                                                               email,
                                                               password,
                                                              **extra_fields)

    def create_user(self, username, email=None, password=None,*args, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        now = timezone.now()
        if not username:
            raise ValueError('The given username must be set')
        email = UserManager.normalize_email(email)
        user = self.model(email=username,
                       is_active=True, is_superuser=False,
                          last_login=now, date_joined=now, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'email'
    is_staff = True
    objects = EmailUserManager()

    email = models.CharField(_('email address'), max_length=75, unique=True, validators=[validate_email_admin])
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    is_active = models.BooleanField(_('active'), default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    @property
    def username(self):
        return self.email
    get_short_name = AbstractUser.get_short_name
    get_full_name = AbstractUser.get_full_name


    class Meta:
        verbose_name_plural = _("Membri")
