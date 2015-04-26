from django.conf.urls import patterns, url
import views

urlpatterns = patterns('work.views',
  url(r'^workcategory/$', views.ListWorkCategory.as_view(), name='list-workcategory'),
  url(r'^work/$', views.ListWork.as_view(), name='list-work'),
  url(r'^work/(?P<pk>\d+)/$', views.WorkDetail.as_view(), name='work-detail'),
  url(r'^applywork/$', views.ApplyWork.as_view(), name='apply-work'),
  url(r'^region/$', views.ListRegion.as_view(), name='list-region'),
  url(r'^adv/$', views.ListAdvertise.as_view(), name='list-advertise'),
)