from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT
from rest_framework.views import APIView
from .models import State, City, Population
from .serializers import StateSerializer, PopulationSerializer, CitySerializer


class PopulationListAV(APIView):
	def get(self, request):
		population = Population.objects.all()
		serializer = PopulationSerializer(population, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = PopulationSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors)


class PopulationDetail(APIView):
	def get(self, request, pk):
		try:
			population = Population.objects.get(pk=pk)
		except Population.DoesNotExist:
			return Response({'error': 'Population Not found'}, status=HTTP_404_NOT_FOUND)
		serializer = PopulationSerializer(population)
		return Response(serializer.data)

	def put(self, request, pk):
		population = Population.objects.get(pk=pk)
		serializer = PopulationSerializer(population, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

	def delete(self, request, pk):
		population = Population.objects.get(pk=pk)
		population.delete()
		return Response(status=HTTP_204_NO_CONTENT)


class CityListAV(APIView):
	def get(self, request):
		city = City.objects.all()
		serializer = CitySerializer(city, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = CitySerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors)


class CityDetail(APIView):

	def get(self, request, pk):
		try:
			city = City.objects.get(pk=pk)
		except City.DoesNotExist:
			return Response({'error': 'State Not found'}, status=HTTP_404_NOT_FOUND)
		serializer = CitySerializer(city)
		return Response(serializer.data)

	def put(self, request, pk):
		city = City.objects.get(pk=pk)
		serializer = CitySerializer(city, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

	def delete(self, request, pk):
		city = City.objects.get(pk=pk)
		city.delete()
		return Response(status=HTTP_204_NO_CONTENT)


class StateListAV(APIView):
	def get(self, request):
		state = State.objects.all()
		serializer = StateSerializer(state, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = StateSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors)


class StateDetailAV(APIView):
	def get(self, request, pk):
		try:
			state = State.objects.get(pk=pk)
		except State.DoesNotExist:
			return Response({'error': 'State Not found'}, status=HTTP_404_NOT_FOUND)
		serializer = StateSerializer(state)
		return Response(serializer.data)

	def put(self, request, pk):
		state = State.objects.get(pk=pk)
		serializer = StateSerializer(state, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

	def delete(self, request, pk):
		state = State.objects.get(pk=pk)
		state.delete()
		return Response(status=HTTP_204_NO_CONTENT)
