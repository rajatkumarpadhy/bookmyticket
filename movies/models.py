from django.db import models
from django.contrib.auth.models import User
from userprofile.models import City

class Cinema(models.Model):
	name = models.CharField(max_length=128)
	city = models.ForeignKey(City, related_name="cinemas_in_city", null=True, 
		on_delete=models.SET_NULL)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

class Movie(models.Model):
	name = models.CharField(max_length=128, null=False)
	cinema = models.ManyToManyField(Cinema, related_name="movies")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

class ShowTime(models.Model):
	start_time = models.DateTimeField(null=False)
	end_time = models.DateTimeField(null=False)
	cinema = models.ForeignKey(Cinema, related_name="cinema_showtimes", null=False, 
		on_delete=models.CASCADE)
	movie = models.ForeignKey(Movie, related_name="movie_showtimes", null=False,
		on_delete=models.CASCADE)
	seats = models.JSONField(null=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Ticket(models.Model):
	user = models.ForeignKey(User, related_name="tickets", null=True, 
		on_delete=models.SET_NULL)
	showtime = models.ForeignKey(ShowTime, related_name="booked_tickets", null=True,
		on_delete=models.SET_NULL)
	seat_number = models.PositiveIntegerField(null=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.id)