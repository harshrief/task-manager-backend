from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tasks.urls')),  # Register API
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Login API
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh Token
]
