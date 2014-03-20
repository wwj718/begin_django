#coding:utf-8
from django.db import models
#https://github.com/zhangfisher/DjangoUeditor/tree/master/TestApp
#看testapp学习使用



class Message(models.Model):
    '''留言'''
    #id = models.AutoField(primary_key=True) #不可改
    name = models.CharField(blank=True,max_length=20, verbose_name=u'姓名')
    email = models.EmailField()
    content = models.CharField(max_length=100, verbose_name=u'内容')
    response = models.CharField(blank=True,max_length=100, verbose_name=u'回复')
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True, editable=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['-create_time']
        verbose_name_plural = verbose_name = u"留言"
        #verbose_name_plural 复数形式
