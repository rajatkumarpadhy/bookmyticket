from django.urls import path
from movies import views

urlpatterns = [
	path('view_movies/<str:city>/',views.MovieView.as_view()),
	path('view_cinemas/<int:movie_id>/',views.CinemaView.as_view()),
	path('view_seats/<int:showtime_id>/',views.SeatView.as_view()),
	path('book_ticket/',views.TicketView.as_view())
]