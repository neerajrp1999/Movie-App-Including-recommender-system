# Movie-App-Including-recommender-system
This is a Movie Application which Includes recommender system.
# Reqirement
visual studio 2019 - python 	

python libraries - surprise, tkinter, heapq, socket, os, csv, sys, re

# Note
This Application is based on client-server structure with is connected to each other by "socket".

the Login folder contain the client side and other folders contains server side.

ml-latest-small folder contain csv files.

In every server side program there is a MovieLens.py file, change the url in code
    ratingsPath = 'E:\\Neeraj\\ml-latest-small\\Testratings.csv'
    moviesPath = 'E:\\Neeraj\\ml-latest-small\\movies.csv' 
	also this maybe present in other part of code , change it.
	
Change the socket ip-adress every time you run.
# disadvantage
Gui is not too much good looking.

slow.

you have to run all code at the time(client-server)
# Advantage
1. work properly

2. give 91% and more prediction
