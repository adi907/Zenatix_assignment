from rest_framework import serializers
from .models import Event, Category, Registration, Venue

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)

    class Meta:
        model = Event
        fields = '__all__'

    def create(self, validated_data):
        categories_data = validated_data.pop('categories')
        event = Event.objects.create(**validated_data)
        for category_data in categories_data:
            category, _ = Category.objects.get_or_create(**category_data)
            event.categories.add(category)
        return event

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'

class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = '__all__'