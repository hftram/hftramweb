from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from data import views as data_views

urlpatterns = [
    # Examples:
     #url(r'^$', 'mysite.views.home', name='home'),
     #url(r'^blog/', include('blog.urls')),
    url(r'^json_upload/$', data_views.json_upload),#Check
	url(r'^tram_data_upload/$', data_views.tram_data_upload),#check
   	url(r'^graph/(?P<data_id>\d+)/$', data_views.graph),#C
	url(r'^graph/(?P<start>\d+)/(?P<end>\d+)/$', data_views.graph_multi),#C
	url(r'^table/$', data_views.table),
	url(r'^get_latest_graph_id/$', data_views.get_latest_graph_id),#check
	url(r'^get_latest_traminfo_id/$', data_views.get_latest_traminfo_id),
	url(r'^get_latest_tram_data/$', data_views.get_latest_tram_data),# check
	url(r'^tram_info/$', data_views.tram_info),#C
	url(r'^graph/(?P<data_id>\d+)/miserables.json/$', data_views.test)#C
]

urlpatterns += staticfiles_urlpatterns()
