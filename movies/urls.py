from django.urls import path
from movies import views

urlpatterns = [
	path('view_movies/<str:city>/',views.view_movies),
	path('view_cinemas/<int:movie_id>/',views.view_cinemas),
	path('view_seats/<int:showtime_id>/',views.view_seats),
	path('book_ticket/',views.book_ticket)
]