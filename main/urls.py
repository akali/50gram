from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.login_, name='login'),
    url(r'^logout/', views.logout_, name='logout'),
    url(r'^signup/', views.signup_view, name='signup'),
    url(r'^signup_action/', views.signup_, name='signup_action'),
    url(r'^new_post_view/', views.new_post_view, name='new_post'),
    url(r'^new_post', views.new_post, name='new_post_action'),
    url(r'^user/(?P<username>[a-zA-Z0-9]+)', views.get_user, name='get_user'),
    url(r'^new_follow/(?P<username>[a-zA-Z0-9]+)', views.new_follow, name='new_follow_action'),
    url(r'^wall/', views.wall, name='wall'),
    url(r'like_action/(?P<post_id>[0-9]+)', views.like_action, name='like_action'),
]

