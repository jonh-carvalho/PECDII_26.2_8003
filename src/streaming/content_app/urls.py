from rest_framework.routers import DefaultRouter
from .views import CommentViewSet, ContentViewSet

router = DefaultRouter()
router.register(r'contents', ContentViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = router.urls