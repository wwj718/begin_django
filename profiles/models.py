#coding:utf-8

from django.db import models
from django.utils.translation import ugettext_lazy as _

from userena.models import UserenaBaseProfile
from userena.utils import user_model_label
import datetime

#添加角色
class Profile(UserenaBaseProfile):
    """ Default profile """
    GENDER_CHOICES = (
        (1, _('Male')),
        (2, _('Female')),
    )

    user = models.OneToOneField(user_model_label,
                                unique=True,
                                verbose_name=_('user'),
                                related_name='profile')

    gender = models.PositiveSmallIntegerField(_('gender'),
                                              choices=GENDER_CHOICES,
                                              blank=True,
                                              null=True)
    mobile = models.CharField(max_length=20,unique=True)
    #不可编辑！隐藏字段，只读
    role = models.CharField(blank=True,max_length=20)

