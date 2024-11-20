from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),  # Root URL for landing page
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.logged_in_home, name='logged_in_home'),
    path('predict-price/', views.predict_price_view, name='predict_price'),# Other URL patterns...
]