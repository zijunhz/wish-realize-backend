from django.urls import path

from . import views

urlpatterns = [
    path('getAllWishes/', views.getAllWishes, name='getAllWishes'),
    path('getSingleWish/<str:wishId>/', views.getSingleWish, name='getSingleWish'),
    path('get_csrf_token/',views.get_csrf_token,name='get_csrf_token'),
    path('addNewWish/',views.addNewWish,name='addNewWish'),
    path('confirmWish/<str:wishID>/',views.confirmWish,name='confirmWish')
]
