from rest_framework import serializers
from movies.models import Movie, Cinema, ShowTime, Ticket

class MovieSerializer(serializers.ModelSerializer):
	class Meta:
		model = Movie
		fields = ['id', 'name', 'cinema']
		depth = 1

class CinemaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Cinema
		fields = ['id', 'name', 'city', 'cinema_showtimes']
		depth = 1

class ShowTimeSerializer(serializers.ModelSerializer):
	class Meta:
		model = ShowTime
		fields = ['id', 'start_time', 'end_time', 'seats']

class TicketSerializer(serializers.ModelSerializer):
	class Meta:
		model = Ticket
		fields = ['user', 'showtime', 'seat_number']