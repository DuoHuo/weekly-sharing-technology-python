from django.conf.urls import patterns, url
import views

urlpatterns = patterns('social.views',
    url(r'^read/$', views.ListRead.as_view(), name='list-read'),
    url(r'^activity/$', views.ListActivity.as_view(), name='list-activity'),
    url(r'^exam/$', views.ListExam.as_view(), name='list-exam'),
    url(r'^schoolinfo/$', views.ListSchoolInfo.as_view(), name='list-school-info'),
    url(r'^readcategory/$', views.ListReadCategory.as_view(), name='list-read-cat'),
    url(r'^activitycategory/$', views.ListActivityCategory.as_view(), name='list-activity-cat'),
    url(r'^examcategory/$', views.ListExamCategory.as_view(), name='list-exam-cat'),
    url(r'^schoolinfocategory/$', views.ListSchoolInfoCategory.as_view(), name='list-school-info-cat'),

    # url(r'^/(?P<pk>\d+)/$', views.WorkDetail.as_view(), name='work-detail'),
    url(r'^search/$', views.search_book),
    url(r'^book-detail/(?P<id>\d+)/$', views.book_detail),

)