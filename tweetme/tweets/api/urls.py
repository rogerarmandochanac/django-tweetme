from rest_framework import routers
from .views import TweetViewSet

router = routers.DefaultRouter()
router.register('tweet', TweetViewSet)

urlpatterns = router.urls