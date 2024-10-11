from rest_framework import serializers
from .models import (
    Product, ProductCategory, ProductReview, Cart, CartItem, Order, 
    OrderItem, UserProfile, UserAddress, Payment
)
from django.contrib.auth.models import User

# Serializer for User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

# Serializer for User Profile
class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = ['user', 'image', 'phone', 'updated_at']

# Serializer for User Address
class UserAddressSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = UserAddress
        fields = ['user', 'house_number', 'street', 'city', 'postal_code', 'country', 'updated_at']

# Serializer for ProductCategory
class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['id', 'name', 'description', 'created_at', 'updated_at']

# Serializer for ProductReview
class ProductReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = ProductReview
        fields = ['id', 'product', 'user', 'rating', 'created_at', 'updated_at']

# Serializer for Product
class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=ProductCategory.objects.all())
    reviews = ProductReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock_quantity', 'category', 'image_url', 'reviews', 'created_at', 'updated_at']
    
    def validate(self, attrs):
        # Example validation for price
        if attrs.get('price') <= 0:
            raise serializers.ValidationError("Price must be greater than zero.")
        return attrs

# Serializer for CartItem
class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity']

# Serializer for Cart
class CartSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items', 'created_at', 'updated_at']

# Serializer for OrderItem
class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity', 'ordered_price']

# Serializer for Order
class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    order_items = OrderItemSerializer(many=True, read_only=True)
    billing_address = UserAddressSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'billing_address', 'order_items', 'created_at', 'updated_at', 'delivery']

# Serializer for Payment
class PaymentSerializer(serializers.ModelSerializer):
    order = OrderSerializer(read_only=True)

    class Meta:
        model = Payment
        fields = ['id', 'order', 'status', 'updated_at']
