from django.urls import path

from .views import StateListAV, StateDetailAV, CityListAV, CityDetail, PopulationListAV, PopulationDetail

urlpatterns = [
	path('list1/', PopulationListAV.as_view(), name='population_list'),
	path('list1/<int:pk>', PopulationDetail.as_view()),
	path('list2/', CityListAV.as_view(), name='City_list'),
	path('list2/<int:pk>', CityDetail.as_view()),
	path('list3/', StateListAV.as_view(), name='state_list'),
	path('list3/<int:pk>', StateDetailAV.as_view()),

]
