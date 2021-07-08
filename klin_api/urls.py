from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'klin_api'

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('create-user/', views.UserCreate.as_view(), name='account-create'),
    path('create-agency/', views.AgencyCreate.as_view(), name='agent-create'),
    path('profile/', views.ProfileView.as_view(), name='view-profile'),
    path('update-profile/', views.ProfileUpdateView.as_view(), name='update-profile'),
    path('update-user/', views.UserUpdateView.as_view(), name='update-user'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



