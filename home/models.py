# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    position = models.TextField(max_length=255, null=True, blank=True)
    role = models.TextField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Booking(models.Model):

    #__Booking_FIELDS__
    event = models.TextField(max_length=255, null=True, blank=True)
    event_time = models.DateTimeField(blank=True, null=True, default=timezone.now)
    requested_model = models.ForeignKey(Model, on_delete=models.CASCADE)

    #__Booking_FIELDS__END

    class Meta:
        verbose_name        = _("Booking")
        verbose_name_plural = _("Booking")


class Staff(models.Model):

    #__Staff_FIELDS__
    first_name = models.TextField(max_length=255, null=True, blank=True)
    last_name = models.TextField(max_length=255, null=True, blank=True)

    #__Staff_FIELDS__END

    class Meta:
        verbose_name        = _("Staff")
        verbose_name_plural = _("Staff")



#__MODELS__END
