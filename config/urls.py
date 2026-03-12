from django.contrib import admin
from django.urls import path, include
from Authentication import views
from allauth.account.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    
    # These two lines make your original 'login' and 'logout' names work
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    path('accounts/', include('allauth.urls')),
]