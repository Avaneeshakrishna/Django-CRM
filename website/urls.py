from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = 'home'),  #home page url which points to vews.home
    #path('login/',views.login_user, name = 'login'), # this creates separate login page
    path('logout/',views.logout_user, name = 'logout'),
    path('register/',views.register_user, name = 'register'),

]
