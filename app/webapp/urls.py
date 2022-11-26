from webapp.views import IndexView, ImageCreateView, ImageDeleteView, ImageUpdateView,\
    ImageView, ImageFavoriteView
from django.urls import path

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('product/<int:pk>', ImageView.as_view(), name='image_detail'),
    path('images/add/', ImageCreateView.as_view(), name='image_add'),
    path('image/<int:pk>/delete', ImageDeleteView.as_view(), name="image_delete"),
    path('image/<int:pk>/edit', ImageUpdateView.as_view(), name="image_edit"),
    path('image/<int:pk>/favorite', ImageFavoriteView.as_view(), name="image_favorite"),
    # path('image/<int:pk>/favorite-remove', ImageFavoriteView.as_view(), name="image_favorite_remove"),

    # path('products/deleted/<int:pk>', ProductDeleteView.as_view(), name='confirm_delete'),
    # path('products/<int:pk>/product_add_basket', IndexView.as_view(), name='products'),
    # path('products/<int:pk>/review/add/', ReviewAddView.as_view(), name='review_create'),
    # path('reviews/edit/<int:pk>', ReviewEditView.as_view(), name='review_edit'),
    # path('reviews/deleted/<int:pk>', ReviewDeleteView.as_view(), name='review_delete'),
    # path('reviews/deleted/<int:pk>', ReviewDeleteView.as_view(), name='confirm_delete_review'),
    # path('reviews/add/', ReviewAddView.as_view(), name='review_create')
]