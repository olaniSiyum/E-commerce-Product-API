from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import (
    ProductCategoryViewSet, ProductViewSet, ProductReviewViewSet, 
    CartViewSet, CartItemViewSet, OrderViewSet, OrderItemViewSet, 
    UserProfileViewSet, UserAddressViewSet, PaymentViewSet
)

# Initialize the router
router = DefaultRouter()

# Register the ViewSets with the router
router.register(r'product-categories', ProductCategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'product-reviews', ProductReviewViewSet)
router.register(r'carts', CartViewSet)
router.register(r'cart-items', CartItemViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet)
router.register(r'user-profiles', UserProfileViewSet)
router.register(r'user-addresses', UserAddressViewSet)
router.register(r'payments', PaymentViewSet)

# Include the router.urls in urlpatterns
urlpatterns = [
    path('', include(router.urls)),  # DRF's router handles all registered ViewSets
]
