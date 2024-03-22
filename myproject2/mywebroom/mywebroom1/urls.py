from django.urls import path
from mywebroom1 import views

urlpatterns = [
    path('', views.home),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    # path('dashboard/', views.dashboard_view, name='dashboard'),

    path('main', views.index, name='main'),
    path('search', views.search, name='search'),
    path('form_room1', views.formroom1),
    path('form_room2', views.formroom2),
    path('form_room3', views.formroom3),
    path('form_room4', views.formroom4),
    path('form_room5', views.formroom5),
    path('form_room6', views.formroom6),
    path('roomlist', views.roomlist),
    path('edit/<person_id>',views.edit),
    path('delete/<person_id>',views.delete),
]
    # path('login/', views.login_user, name='login'),
    # path('logout', views.logout_user, name='logout'),
