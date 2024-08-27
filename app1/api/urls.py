from rest_framework.routers import DefaultRouter
from .viewsets import RickAndMorty

router = DefaultRouter()

router.register(r"api", RickAndMorty)



urlpatterns = router.urls
