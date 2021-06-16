from django.db import models


# Create your models here.
class Population(models.Model):
	population_gender = (('Male', 'Male'), ('Female', 'Female'))
	zero_to_six_population_gender = (('Male', 'Male'), ('Female', 'Female'))
	literate_gender = (('Male literate', 'Male literate'), ('Female literate', 'Female literate'))
	effective_rate_over_age_seven_gender = (('Male', 'Male'), ('Female', 'Female'))
	graduate_gender = (('Male Graduates ', 'Male Graduates '), ('Female Graduates ', 'Female Graduates '))
	Total_population = models.CharField(max_length=100, choices=population_gender)
	zero_to_six_total_population = models.CharField(max_length=100, choices=zero_to_six_population_gender)
	Total_literate = models.CharField(max_length=100, choices=literate_gender)
	sex_ratio = models.CharField(max_length=100)
	child_sex_ratio = models.CharField(max_length=100)
	literate_rate_over_seven = models.CharField(max_length=100, choices=effective_rate_over_age_seven_gender)
	total_graduate = models.CharField(max_length=100, choices=graduate_gender)


class City(models.Model):
	city_location = (('Lag', 'Lag'), ('Log', 'Log'))
	city_name = models.CharField(max_length=100, unique=True)
	Total_population = models.ForeignKey(Population, on_delete=models.CASCADE)
	location = models.CharField(max_length=100, choices=city_location)

	def __str__(self):
		return self.city_name


class State(models.Model):
	state_location = (('Lag', 'Lag'), ('Log', 'Log'))
	state_name = models.CharField(max_length=100)
	city_name = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True, unique=True)
	Total_population = models.ForeignKey(Population, on_delete=models.CASCADE)
	location = models.CharField(max_length=100, choices=state_location)

	def __str__(self):
		return self.state_name
