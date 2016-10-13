The purpose of my application is to give the time of sunrise, sunset, moonrise, and moonset in my hometown of Taos, New Mexico. 

This application takes the users input of any date that they would like in the past, present, and future. It then asks the user if they would like to see the Sunrise/Sunset time OR the Moonrise/Moonset time of the specified date. After, it runs through some functions to calculate the date and it prints the date and times of either the Sunrise/Sunset or Moonrise/Moonset onto a screen with a picture of either a sunrise or sunset in Taos, New Mexico depending on the selection. The application then blanks out the screen and asks the user to pick another date. If the user inputs "-1", the application quits. Also if the user does not put a correct date as specified (yyyy-mm-dd), the application will break.

For the application, the libraries that i used were PyEphem (ephem), Python Turtle (turtle), and Python's Time. PyEphem was used to calculate the times of the sun or moon rise/set, Python Turtle was used to display the information and show a picture of Taos, and finally Python time was used on Turtle for the sleep function to give the user time to read the display before timing out. 

My application would be useful for people trying to determine the Sunrise/Sunset or Moonrise/Moonset of a certain period of time in Taos. This could maybe be useful for a farmer or someone who may be concerned with the Sunrise/Sunset or Moonrise/Moonset of this given area.

In the future, I will update this application so that a user could choose anywhere in the world using the latitude and longitude that they would like, and also use the horizon function of ephem a little more specifically to the region. 

I will also do another update to generate the location of certain star constellations at any given time and place.

