#coding=utf-8
from django import forms
from django.utils.translation import ugettext_lazy as _

from userena.forms import SignupForm
from captcha.fields  import CaptchaField
from django.shortcuts import get_object_or_404

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions


class SignupFormExtra(SignupForm):
    mobile = forms.CharField(label=_(u'手机号'),max_length=30,required=True)
    codesms = forms.CharField(label=_(u'手机验证码'),max_length=30,required=True)
    captcha = CaptchaField(label=_(u'验证码'))    #contact = forms.CharField(label=_(u'Contact'),max_length=30,required=False)

    helper = FormHelper()
    helper.form_id = 'register_form'
    helper.form_action = ''
    helper.layout = Layout(

        Field('username',id='UserName'),
        Field('password1',id='LoginPass'),
        Field('password2',id='LoginPass2'),
        Field('mobile', id='Mobile'),
        PrependedText('codesms', '<a href="#" id="GetCode" disabled="disabled">点击获取验证码</a>',css_class='span1',id='SMS'),
        Field('email',id='Email'),
        Field('captcha'),
        FormActions(
            Submit('save_changes', u'注册', css_class="span2 btn-primary"),
        )

        )

    def clean(self):
	#多字段验证
        cleaned_data=super(SignupFormExtra, self).clean()
        return cleaned_data

    def save(self):
        """
        Override the save method to save the first and last name to the user
        field.

        """
        # Original save method returns the user
        user = super(SignupFormExtra, self).save()
        return user
