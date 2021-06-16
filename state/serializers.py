from rest_framework import serializers

from .models import Population, City, State


class PopulationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Population
		fields = "__all__"


class CitySerializer(serializers.ModelSerializer):
	class Meta:
		model = City
		fields = "__all__"


class StateSerializer(serializers.ModelSerializer):
	class Meta:
		model = State
		fields = "__all__"
