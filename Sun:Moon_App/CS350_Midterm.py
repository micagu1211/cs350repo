import ephem
import turtle
import time


def location(date):
	taos = ephem.Observer()
	taos.pressure = 0 
	taos.horizon = '-0:34'
	taos.lat, taos.lon = '36.4','-105.6'
	taos.elevation= 2124
	taos.date = date
	#print taos
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

def turtle_sun_moon(moonOrsun,sunrising,sunsetting,moonrising,moonsetting):
	window=turtle.Screen()
	m=turtle.Turtle()
	m.color('black')
	window.setup(1000,1000)

	if moonOrsun == '1':
		window.bgpic('taos_sunset.gif')
		window.title("Sunrise/Sunset")
		window.setup(1000,1000)

		m.penup()
		m.setpos(-275,100)
		m.pendown()
		m.write("Sunrise in Taos, New Mexico==> " + str(sunrising) + ' AM',font=("Arial",20,"bold"))
		m.penup()
		m.setpos(-275,-100)
		m.pendown()
		m.write("Sunset in Taos, New Mexico==> " + str(sunsetting) + ' PM',font=("Arial",20,"bold"))

		time.sleep(15)
		window.clear()
		window.reset()

		window.bgcolor('black')
		m.color('white')
		m.penup()
		m.setpos(-275,100)
		m.pendown()
		m.write("Enter more information into the terminal please!!!!! ",move=False,align="left",font=("Arial",30,"normal"))

		time.sleep(3)
		window.clear()
		window.bgcolor('black')



		

	elif moonOrsun == '2':
		window.bgpic('moon.gif')
		window.title("Moonrise/Moonset")
		window.setup(1000,1000)

		m.color('white')

		m.penup()
		m.setpos(-275,100)
		m.pendown()
		m.write("Moonrise in Taos, New Mexico==> " + str(moonrising) + ' PM',font=("Arial",20,"bold"))
		m.penup()
		m.setpos(-275,-100)
		m.pendown()
		m.write("Moonset in Taos, New Mexico==> " + str(moonsetting) + ' AM',font=("Arial",20,"bold"))
		
		time.sleep(15)
		window.clear()
		window.reset()

		window.bgcolor('black')
		m.color('white')
		m.penup()
		m.setpos(-275,100)
		m.pendown()
		m.write("Enter more information into the terminal please!!!!!",move=False,align="left",font=("Arial",30,"normal"))

		time.sleep(3)
		window.clear()
		window.bgcolor('black')

		
		



#MAIN 

while 1:
	print("*====================================================================*")
	print("This is a Simulation for the Sunrise/Sunset and Moonrise/Moonset in Taos, New Mexico!!!\n              (ALL TIMES ARE MST)            \n")
	date = raw_input(str("Please Enter a Date (Enter as yyyy-mm-dd)\n(Type -1 to exit)\n: "))

	if date == '-1':
		print("Thank you for using!!!!\nGoodbye!")
		break
		

	else:
		date += ' 17:00:00'
		moonOrsun = raw_input(str("If you want Sunrise/Sunset press 1:\nIf you want Moonrise press 2:\n"))
		taos = location(date)
		sunrising = sunrise(taos)
		sunrising = setlocaltime(sunrising)
		sunsetting = sunset(taos)
		sunsetting = setlocaltime(sunsetting)
		moonrising = moonrise(taos)
		moonrising = setlocaltime(moonrising)
		moonsetting = moonset(taos)
		moonsetting = setlocaltime(moonsetting)

		turtle_sun_moon(moonOrsun,sunrising,sunsetting,moonrising,moonsetting)
	