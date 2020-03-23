from django.urls import path, include
from django.contrib import admin

# from rest_framework import routers
from blog import views

# router = routers.DefaultRouter()
# router.register(r'authors', views.AutherV, basename='t')

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        '',
        include(('insightjedi.urls', 'insightjedi'), namespace='insightjedi')
    ),
    path('test/', views.AutherV.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls'))
]
