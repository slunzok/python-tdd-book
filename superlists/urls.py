from django.urls import include, path, re_path
from lists import views as list_views
from lists import api_urls
from lists import urls as list_urls
from accounts import urls as account_urls
from lists.api import router

urlpatterns = [
    re_path(r'^$', list_views.HomePageView.as_view(), name='home'),
    re_path(r'^lists/', include(list_urls)),
    re_path(r'accounts/', include(account_urls)),
    re_path(r'^api/', include(router.urls)),
]
