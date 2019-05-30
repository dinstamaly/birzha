from django.urls import path, include

from .views import UserDeatilAPIView
# UserProfileUpdate

urlpatterns = [
    path('<username>/', UserDeatilAPIView.as_view(), name='user-detail'),
    # path('<username>/update/', UserProfileUpdate.as_view(), name='profile-update'),
]
