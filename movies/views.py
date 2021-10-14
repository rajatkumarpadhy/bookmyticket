from django.shortcuts import render
from movies.models import Movie, Cinema, ShowTime, Ticket
from movies.serializers import (MovieSerializer, CinemaSerializer, ShowTimeSerializer,
		TicketSerializer)
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView


class MovieView(APIView):
	def get(self, request, city):
		try:
			movies = Movie.objects.prefetch_related("cinema").filter(
				cinema__city__name=city).distinct()
			serializer = MovieSerializer(movies, many=True)
			return Response(serializer.data)
		except Exception as e:
			print (e)
			return Response({"message":"Something went wrong!!"})

class CinemaView(APIView):
	def get(self, request, movie_id):
		try:
			cinema = Cinema.objects.filter(movies=movie_id)
			serializer = CinemaSerializer(cinema, many=True)
			return Response(serializer.data)
		except Exception as e:
			print (e)
			return Response({"message":"Something went wrong!!"})

class SeatView(APIView):
	def get(self, request, showtime_id):
		try:
			show = ShowTime.objects.get(id=showtime_id)
			serializer = ShowTimeSerializer(show)
			return Response(serializer.data)
		except Exception as e:
			print (e)
			return Response({"message":"Something went wrong!!"})

class TicketView(APIView):
	def post(self,request):
		try:
			serializer = TicketSerializer(data=request.data)
			if serializer.is_valid():
				validated_data  =serializer.validated_data
				if not Ticket.objects.filter(showtime=validated_data["showtime"],
					seat_number=validated_data["seat_number"]):
					serializer.save()
				else:
					return Response({"message":"This seat is already booked"})
				return Response(serializer.data)
			else:
				return Response(serializer.errors)
		except Exception as e:
			print (e)
			return Response({"message":"Something went wrong!!"})