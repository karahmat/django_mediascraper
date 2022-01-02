from django.urls import path
from django.urls.conf import include
from account import views

app_name = "account"

urlpatterns = [
    # path('', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout")
]
