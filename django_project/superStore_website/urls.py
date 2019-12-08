from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('change-password/', auth_views.PasswordChangeView.as_view(template_name='users/change-password.html'),name='change-password'),
    path('password_change_done/',auth_views.PasswordChangeDoneView.as_view(template_name='users/change-password_done.html'),name='password_change_done'),
    path('home/', views.home, name='home'),
    path('checkout/', views.checkout, name='checkout'),
    path('search/', views.search_results, name='search_results'),
    path('gallery/', views.gallery, name='gallery'),
    path('none/search/', views.no_results, name='none'),
    path('cart/', views.Cart, name='cart'),
    path('receipt/', views.receipt, name='receipt'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)