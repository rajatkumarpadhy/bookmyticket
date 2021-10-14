from django.contrib import admin
from movies.models import Cinema, Movie, ShowTime, Ticket

# Register your models here.
admin.site.register(Cinema)
admin.site.register(Movie)
admin.site.register(ShowTime)
admin.site.register(Ticket)