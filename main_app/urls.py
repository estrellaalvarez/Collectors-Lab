from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('skins/', views.SkinsList.as_view(), name="skins_list"),
    path('skins/new/', views.SkinCreate.as_view(), name="skin_create"),
    path('skins/<int:pk>/', views.SkinDetail.as_view(), name="skin_detail"),
    path('skins/<int:pk>/update',views.SkinUpdate.as_view(), name="skin_update"),
    path('skins/<int:pk>/delete',views.SkinDelete.as_view(), name="skin_delete"),
    # include the built-in auth urls for the built-in views
    path('accounts/', include('django.contrib.auth.urls')),
]