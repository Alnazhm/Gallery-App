from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from api.serializers import ImageSerializer
from webapp.models import Image

# class IsAuthorOrReadOnly(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if request.method in ('GET', 'HEAD', 'OPTIONS'):
#             return True
#         elif request.method in ('PUT', 'PATCH', 'DELETE'):
#             return obj.author == request.user
#         elif request.user.is_authenticated and request.method == "POST":
#             return True
#
# class AddORDeleteLike(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if request.method in ("POST", 'DELETE'):
#             return True

class ImageView(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def image_favorite(self, request, *args, **kwargs):
        photo_by_pk = self.get_object()
        user = request.user
        user.images.add(photo_by_pk)
        return JsonResponse({'result': 'Photo added to favorite'})

    def image_remove_favorite(self, request, *args, **kwargs):
        photo_by_pk = self.get_object()
        user = request.user
        user.favourited_photos.remove(photo_by_pk)
        return JsonResponse({'result': 'Photo removed to favorite'})





