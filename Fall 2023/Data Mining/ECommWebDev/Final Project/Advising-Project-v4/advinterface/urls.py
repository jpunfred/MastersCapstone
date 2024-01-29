from django.urls import path
from .views import profile_creation, submission_successful

urlpatterns = [
    path('profile_creation/', profile_creation, name='profile_creation'),
    path('submission_successful/', submission_successful, name='submission_successful'),
]
