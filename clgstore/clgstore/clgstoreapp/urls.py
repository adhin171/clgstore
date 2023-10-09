from django.urls import path
from clgstoreapp import views

app_name = 'clgstoreapp'

urlpatterns = [
    path('',views.home,name='home'),
    path('apply/',views.submit_form,name='submit_form'),
    path('list/', views.list_view, name='list'),
    path('login_view/',views.login_view,name='login_view'),
    path('register/',views.register,name='register'),
]
