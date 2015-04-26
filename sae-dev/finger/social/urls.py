from django.conf.urls import patterns, url
import views

urlpatterns = patterns('social.views',
  url(r'^$', views.ListUser.as_view(), name='list-user'),
  url(r'^check_username/$', views.check_username),
  url(r'^user/$', views.RetrieveUpdateDestroyUser.as_view(), name='detail-user'),
  url(r'^register/$', views.UserRegiter.as_view(), name='register-user'),
  url(r'^login/$', views.UserLogin.as_view(), name='login-user'),
  url(r'^logout/$', views.UserLogout.as_view(), name='logout-user'),
  # url(r'^bind/$', views.OauthUserBind.as_view(), name='bind-user'),
  url(r'^shop/$', views.ListShop.as_view(), name='list-shop'),
  url(r'^shop/(?P<pk>\d+)/$', views.ShopDetail.as_view(), name='shop-detail'),
  url(r'^shopcategory/$', views.ListShopCategory.as_view(), name='list-shopcategory'),
  url(r'^workcategory/$', views.ListWorkCategory.as_view(), name='list-workcategory'),
  url(r'^work/$', views.ListWork.as_view(), name='list-work'),
  url(r'^work/(?P<pk>\d+)/$', views.WorkDetail.as_view(), name='work-detail'),
  url(r'^applywork/$', views.ApplyWork.as_view(), name='apply-work'),
  url(r'^region/$', views.ListRegion.as_view(), name='list-region'),
  url(r'^adv/$', views.ListAdvertise.as_view(), name='list-advertise'),
  url(r'^get_username/$', views.get_info),
)

