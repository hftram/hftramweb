from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from article import views as article_views

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^all/$', article_views.articles),
    url(r'^get/(?P<article_id>\d+)/$', article_views.article),
    url(r'^commands/$', article_views.commands),
    url(r'^last/$', article_views.last_entry),
    url(r'^last_id/$', article_views.last_entry_id),

    url(r'^file_upload/$', article_views.file_upload),
    url(r'^all_files/$', article_views.files),
    url(r'^get_file/(?P<article_id>\d+)/$', article_views.file_),

    url(r'^get_tram_file/$', article_views.tram_file),
    url(r'^tram_file_upload/$', article_views.tram_file_upload),
    #url(r'^download/$', 'article.views.file_'),
]

urlpatterns += staticfiles_urlpatterns()