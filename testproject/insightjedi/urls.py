from rest_framework import routers


from .views import DocumentViewSet

router = routers.DefaultRouter()
router.register(r'documents', DocumentViewSet, basename='document')

urlpatterns = [
    *router.urls
]
