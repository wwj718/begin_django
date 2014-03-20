#coding:utf-8
from django.db import models
#https://github.com/zhangfisher/DjangoUeditor/tree/master/TestApp
#看testapp学习使用
from django.db.models import permalink
from DjangoUeditor.models import UEditorField

from BeautifulSoup import BeautifulSoup


#新闻属性
ATTRIBUTE=(
    (0, u'标红'),
    (1, u'加粗'),
    (2, u'首页'),
    (3, u'置顶'),
    (4, u'推荐'),
    (5, u'头条'),
)


##url:https://github.com/the5fire/django_selfblog

class NewsCategory(models.Model):
    '''栏目名称,作为新闻的外键'''
    name = models.CharField(max_length=40, verbose_name=u'栏目名称')
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True)

    def __unicode__(self):
            return '%s' % (self.name)
    class Meta:
        ordering = ['-create_time']
        verbose_name_plural = verbose_name = u"新闻栏目"


class News(models.Model):
    '''新闻'''
    #id = models.AutoField(primary_key=True) #不可改
    order = models.IntegerField(default=0, verbose_name=u'新闻顺序')
    category = models.ForeignKey(NewsCategory, verbose_name=u'新闻栏目')
    title = models.CharField(max_length=100, verbose_name=u'新闻标题')
    summary = models.TextField(blank=True,verbose_name=u'摘要')
    content_html = UEditorField('新闻内容',height=200,width=500,default='test',imagePath='content_img',imageManagerPath="bb",toolbars="mytoolbars",options={"elementPathEnabled":True},filePath='bb',blank=True)
    content_pic = models.CharField(blank=True,max_length=200, verbose_name=u'展示图片')
    view_times = models.IntegerField(default=1,verbose_name=u'点击量')
    
    keyword = models.CharField(max_length=100, null=True, blank=True, verbose_name=u'新闻关键字', help_text=u'用英文逗号分割')
    attribute = models.CharField(max_length=100, null=True, blank=True, verbose_name=u'新闻属性')
    status = models.IntegerField(default=0, choices=ATTRIBUTE, verbose_name=u'状态')
    pic_url =  models.URLField(blank=True, verbose_name=u'首页图片地址')
    attachments  = models.FileField(blank=True,upload_to='news_attachments', verbose_name=u'附件') #附件
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True)

    
    def save(self):
        #取出第一张图片的html，使用正则
        soup = BeautifulSoup(self.content_html) 
        self.content_pic = str(soup.first("img")) #soup.first("img") #只返回第一个pic,需要转化为str，否则是对象
        if not self.content_pic : 
            self.content_pic = ''
        super(News, self).save() 

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-create_time']
        verbose_name_plural = verbose_name = u"新闻"

    @permalink
    def get_absolute_url(self):
        return ('news_news_details', None, {'id': self.id})


