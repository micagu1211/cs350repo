import ephem
import turtle
from turtle import *

def location(date):
	taos = ephem.Observer()
	taos.pressure = 0 
	taos.horizon = '-0:34'
	taos.lat, taos.lon = '36.4','-105.6'
	taos.elevation= 2124
	taos.date = date
	return taos

def setlocaltime(date):
	lt = ephem.localtime(date)
	return lt

def sunrise(location):
	sunrise = taos.previous_rising(ephem.Sun())
	localtime = ephem.Date(sunrise)
	return localtime

def sunset(location):
	sunset = taos.next_setting(ephem.Sun())
	localtime = ephem.Date(sunset)
	return localtime

def moonrise(location):
	moonrisee= taos.next_rising(ephem.Moon())
	localtime = ephem.Date(moonrisee)
	return localtime

def moonset(location):
	moonset = taos.previous_setting(ephem.Moon())
	localtime = ephem.Date(moonset)
	return localtime

def turtle_sunset():
	window=turtle.Screen()
	window.bgpic('taos_sunset.gif')
	window.title("Sunrise/Sunset")
	window.setup(1000,1000)
	m=turtle.Turtle()
	m.color('black')
	m.penup()
	m.setpos(-275,100)
	m.pendown()
	m.write("Sunrise in Taos, New Mexico==> " + str(sunrising) + ' am',font=("Arial",20,"bold"))
	m.penup()
	m.setpos(-275,-100)
	m.pendown()
	m.write("Sunset in Taos, New Mexico==> " + str(sunsetting) + ' pm',font=("Arial",20,"bold"))

	window.exitonclick()

def turtle_moon():
	window=turtle.Screen()
	window.bgpic('moon.gif')
	window.title("Sunrise/Sunset")
	window.setup(1000,1000)
	m=turtle.Turtle()
	m.color('black')
	m.penup()
	m.setpos(-275,100)
	m.pendown()
	m.write("Moonrise in Taos, New Mexico==> " + str(moonrising) + ' pm',font=("Arial",20,"bold"))
	m.setpos(-275,-100)
	m.pendown()
	m.write("Moonsetting in Taos, New Mexico==> " + str(moonsetting) + ' pm',font=("Arial",20,"bold"))

	window.exitonclick()

#MAIN 
while 1:
	print("This is a Simulation for the Sunrise and Sunset in Taos, New Mexico!!!\n(ALL TIMES ARE MST)\n")
	date = raw_input(str("Please Enter a Date (Enter as yyyy-mm-dd)\nType -1 to exit\n: "))

	if date == '-1':
		print "Thank you for using! Goodbye! :)"
		break
	else:
		date += ' 17:00:00'
		moonOrsun = raw_input(str("If you want Sunrise/Sunset press 1: \n If you want Moonrise press 2: \n"))
		if moonOrsun == '1':
			taos = location(date)
			sunrising = sunrise(taos)
			sunrising = setlocaltime(sunrising)
			#print( "Sunrise for Taos, New Mexico : \n " + str(sunrising) + 'am')
			sunsetting = sunset(taos)
			sunsetting = setlocaltime(sunsetting)
			#print("Sunset for Taos, New Mexico : \n " + str(sunsetting) + 'pm')
			turtle_sunset()

		elif moonOrsun == '2':
			taos = location(date)
			moonrising = moonrise(taos)
			moonrising = setlocaltime(moonrising)
			#print("Moonrise for Taos, New Mexico : \n" + str(moonrising) + 'pm')
			moonsetting = moonset(taos)
			moonsetting = setlocaltime(moonsetting)
			#print ("Moonset of Taos, New Mexico : \n " + str(moonsetting) + 'am')

			turtle_moon()

		else:
			print("That was not a choice! ")


	