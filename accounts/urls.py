from django.urls import path
from .views import (
    signupView, 
    signinView, 
    signoutView, 
    ProfileView, 
    employerSignupView,
    UpdateProfileView,
    profileUpdate,
)

urlpatterns = [
    path('signup/', signupView, name='signup'),
    path('employer-signup', employerSignupView, name='emp_signup'),
    path('login/', signinView, name='signin'),
    path('logout/', signoutView, name='signout'),
    path('profile/', ProfileView, name='profile'),
    path('profile/update/', profileUpdate, name='profile_update'),
]