from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('categoryCreate/', views.categoryCreate, name="categoryCreate"),
    path('categoryCreate/create', views.Create_category, name="Create_category"),
    path('categoryCreate/delete', views.Delete_category, name='cateDelete'),

    path('restaurantDetail/delete', views.Delete_restaurant, name="resDelete"),
    path('restaurantDetail/<str:res_id>', views.restaurantDetail, name="resDetailPage"),
    path('restaurantDetail/updatePage/update', views.Update_restaurant, name="Update_restaurant"),
    path('restaurantDetail/updatePage/<str:res_id>', views.restaurantUpdate, name="resUpdatePage"),


    path('restaurantCreate/', views.restaurantCreate, name="restaurantCreate"),
    path('restaurantCreate/create', views.Create_restaurant, name='Create_restaurant')
]