from django.conf.urls import patterns, url 
from designer import views 
from designer.new_views import new_view

urlpatterns = patterns('', 
        url(r'^$', views.index, name='index'), 
        url(r'^test$', new_view.test, name='name'), 
)  

