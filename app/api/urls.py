from django.urls import path, include
from rest_framework import routers
from api.views import ImageView

router = routers.DefaultRouter()
router.register('images', ImageView)
urlpatterns = [
    path('', include(router.urls)),
    path('image/<int:pk>/tofav/', ImageView.as_view({'get': 'image_favorite'})),
    path('image/<int:pk>/removefav/', ImageView.as_view({'get': 'image_remove_favorite'})),
]






