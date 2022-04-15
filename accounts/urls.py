from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
    path('detail/', views.detail, name='detail'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout')
]
