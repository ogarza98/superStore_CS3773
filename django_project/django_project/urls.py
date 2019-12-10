from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('change-password/', auth_views.PasswordChangeView.as_view(template_name='users/change-password.html'),
         name='change-password'),
    path('password_change_done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='users/change-password_done.html'),
         name='password_change_done'),
    path('', include('superStore_website.urls')),
    path('login/', include('superStore_website.urls')),
    path('checkout/', include('superStore_website.urls')),
    path('search/', include('superStore_website.urls')),
    path('home/', include('superStore_website.urls')),
    path('gallery/', include('superStore_website.urls')),
    path('none/', include('superStore_website.urls')),
    path('cart/', include('cart.urls')),
]
