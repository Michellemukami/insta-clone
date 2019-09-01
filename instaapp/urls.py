from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
   
    url('^$',views.login_page,name = 'come'),
    url(r'^new/profile$', views.profile, name='profile'),
    url(r'^user/', views.user, name='user'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^new/article$', views.new_article, name='new-article'),
    url(r'^home/', views.home, name='home'),
    url(r'^comment/', views.comment, name='comment'),
   
   
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
