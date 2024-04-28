from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('info/', views.info, name='info'),
    path('test/', views.test, name='test'),
    path('oppo/', views.oppo, name='oppo')
]


#from django.urls import path
#from . import views
#from news import views as v

#urlpatterns = [
    #path('', v.news_home, name='home'),
    #path('info/', views.info, name='info'),
    #path('test/', views.test, name='test'),
    #path('oppo/', views.oppo, name='oppo')
#]