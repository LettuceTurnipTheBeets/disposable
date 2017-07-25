from django.shortcuts import render
from django.http import HttpResponse
import random
from .forms import RoomForm
from api.models.rooms import Room
from datetime import datetime, timedelta

"""
Index/Home/Landing Page
"""
def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RoomForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            room_alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
            url_alphabet = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            room_length = 4
            url_length = 10
            room_code = ""
            url = ""

            for i in range(room_length):
                next_index = random.randrange(len(room_alphabet))
                room_code = room_code + room_alphabet[next_index]

            for i in range(url_length):
                next_index = random.randrange(len(url_alphabet))
                url = url + url_alphabet[next_index]
            
            Room.objects.create(
                admin=form.cleaned_data['username'],
                name=form.cleaned_data['room_name'],
                code=room_code,
                url=url,
            )

            print (room_code)
            print (url)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RoomForm()

    return render(request, 'index.html', {'form': form})

"""
About Page
"""
def about(request):
     return render(request, 'about.html')

"""
Room Detail Page
"""
def room(request, room_id):
    return HttpResponse("ID:    {}\nURL:    {}\nName:    {}".format(room_id, 'test', 'test'))
