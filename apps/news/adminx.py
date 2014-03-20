#coding:utf-8

import xadmin
from xadmin import views
from models import News,NewsSubject,NewsCommittee,NewsCategory
# from xadmin.layout import Main, TabHolder, Tab, Fieldset, Row, Col, AppendedText, Side
# from xadmin.plugins.inline import Inline
# from xadmin.plugins.batch import BatchChangeAction
from django import forms
#在django xadmin中使用 Ueditor
#http://blog.csdn.net/u012762088/article/details/14497105


class MainDashboard(object):
    widgets = [
        # [
        #     {"type": "html", "title": "Test Widget", "content": "<h3> Welcome to Xadmin! </h3><p>Join Online Group: <br/>QQ Qun : 282936295</p>"},
        #     {"type": "chart", "model": "app.accessrecord", 'chart': 'user_count', 'params': {'_p_date__gte': '2013-01-08', 'p': 1, '_p_date__lt': '2013-01-29'}},
        #     {"type": "list", "model": "app.host", 'params': {
        #         'o':'-guarantee_date'}},
        # ],
        [
            {"type": "qbutton", "title": "Quick Start", "btns": [{'model': News}, {'model':NewsSubject}, {'model':NewsCommittee}, {'model':NewsCategory}, {'title': "Google", 'url': "http://www.google.com"}]},
        ]
    ]
xadmin.site.register(views.website.IndexView, MainDashboard)


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True
xadmin.site.register(views.BaseAdminView, BaseSetting)


class GlobalSetting(object):
    global_search_models = [News,NewsSubject,NewsCommittee,NewsCategory]
    # global_models_icon = {
    #     Host: 'laptop', IDC: 'cloud'
    # }
xadmin.site.register(views.CommAdminView, GlobalSetting)


# class MaintainInline(object):
#     model = MaintainLog
#     extra = 1
#     style = 'accordion'


# class NewsForm(forms.ModelForm):
#     class Meta:
#         model = News
#     attribute = forms.MultipleChoiceField(label=u'新闻属性', choices=ATTRIBUTE, widget=forms.CheckboxSelectMultiple())
#文章属性
ATTRIBUTE=(
    (0, u'标红'),
    (1, u'加粗'),
    (2, u'首页'),
    (3, u'置顶'),
    (4, u'推荐'),
    (5, u'头条'),
)

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
    attribute = forms.MultipleChoiceField(label=u'新闻属性', choices=ATTRIBUTE, widget=forms.CheckboxSelectMultiple())
    #content_html=forms.CharField(label="内容",widget=UEditorWidget(width=800,height=500, imagePath='aa', filePath='bb',toolbars={}))
    
class NewsAdmin(object):
    form = NewsForm
    search_fields = ('title',)
    fields = ('category', 'title', 'subtitle', 'summary', 'content_html', 'keyword',
              'attribute', 'pic_url', 'attachments', 'subject', 'committee')
    list_display = ('category', 'title', 'view_times', 'create_time')
    ordering = ('-pub_time', )
    save_on_top = True
    #富文本，依赖于插件 xcms


    def save_model(self, request, obj, form, change):
        #obj.author = request.user
        if not obj.summary:
             obj.summary = obj.content_html
        # if not obj.is_old:
        #     obj.content_html = restructuredtext(obj.content)
        else:
            obj.content_html = obj.content_html.replace('\r\n', '<br/>')
            import re
            obj.content_html = re.sub(r"\[cc lang='\w+?'\]", '<pre>', obj.content_html)
            obj.content_html = obj.content_html.replace('[/cc]', '</pre>')
        obj.save()


class NewsCategoryAdmin(object):
    search_fields = ('name',)
    list_display = ('name', 'parent', 'desc', 'create_time', 'status')

class NewsSubjectAdmin(object):
    search_fields = ('name',)
    list_display = ('name', 'create_time', 'update_time')

class NewsCommitteeAdmin(object):
    search_fields = ('name',)
    list_display = ('name', 'create_time', 'update_time')
        

xadmin.site.register(News, NewsAdmin)
xadmin.site.register(NewsSubject, NewsSubjectAdmin)
xadmin.site.register(NewsCommittee, NewsCommitteeAdmin)
xadmin.site.register(NewsCategory, NewsCategoryAdmin)
