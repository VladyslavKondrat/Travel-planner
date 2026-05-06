from rest_framework import serializers
from .models import Project, Place
from .utils import validate_external_place

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ['id', 'project', 'external_id', 'notes', 'is_visited', 'created_at']
        read_only_fields = ['project']

    def validate_external_id(self, value):
        validate_external_place(value)
        return value

class ProjectSerializer(serializers.ModelSerializer):
    places = PlaceSerializer(many=True, required=False)

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'start_date', 'is_completed', 'places']
        read_only_fields = ['is_completed']

    def validate_places(self, places_data):
        if places_data and len(places_data) > 10:
            raise serializers.ValidationError("A project cannot have more than 10 places.")
        return places_data

    def create(self, validated_data):
        places_data = validated_data.pop('places', [])
        project = Project.objects.create(**validated_data)
        
        for place_data in places_data:
            Place.objects.create(project=project, **place_data)
            
        return project