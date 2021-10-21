from rest_framework.routers import DefaultRouter
from .views import TagViewSet, TaskViewSet

router = DefaultRouter()
router.register('tag', TagViewSet)
router.register('task', TaskViewSet)

urlpatterns = [
    *router.urls
]
