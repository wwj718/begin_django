#coding=utf-8
from django.db import models
from sorl.thumbnail import ImageField


# Create your models here.

class HomePic(models.Model):
	'''建一个模型,每次编辑'''
	name = models.CharField(max_length=40, verbose_name=u'图片名称')
	order = models.IntegerField(default=0, verbose_name=u'图片顺序')
	pic =  ImageField(blank=True,upload_to='home_img', verbose_name=u'图片')
	create_time = models.DateTimeField(u'创建时间', auto_now_add=True)
	update_time = models.DateTimeField(u'更新时间', auto_now=True)

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['-create_time']
		verbose_name_plural = verbose_name = u"首页图片"
