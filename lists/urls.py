from django.urls import path, re_path
from lists import views

urlpatterns = [
    re_path(r'^new$', views.NewListView.as_view(), name='new_list'),
    re_path(r'^(\d+)/$', views.view_list, name='view_list'),
    re_path(r'^(\d+)/share$', views.share_list, name='share_list'),
    re_path(r'^users/(.+)/$', views.my_lists, name='my_lists'),
]
