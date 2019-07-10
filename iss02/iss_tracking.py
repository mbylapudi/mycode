import turtle
import urllib.request
import json
import time
eoss = 'http://api.open-notify.org/iss-now.json'

trackiss = urllib.request.urlopen(eoss)

ztrack = trackiss.read()

result = json.loads(ztrack.decode('utf-8'))

print("\n\nConverted python data")
print(result)
input('\nISS data retrieved & converted. Press the ENTER key to continue')

location = result['iss_position']
lat = location['latitude']
lon = location['longitude']
print('\nLatitude: ', lat)
print('Longitude: ', lon)

screen = turtle.Screen()
screen.setup(720, 360)

screen.setworldcoordinates(-180,-90,180,90)

screen.bgpic('iss_map.gif')

screen.register_shape('spriteiss.gif')
iss = turtle.Turtle()
iss.shape('spriteiss.gif')
iss.setheading(90)

lon = round(float(lon))
lat = round(float(lat))

iss.penup()
iss.goto(lon, lat)
la = input('Please enter latitude')
lo = input('Please enter longitude')
x = round(float(la))
y = round(float(lo))
#yellowlat = 17.6868
#yellowlon = 83.2185
mylocation = turtle.Turtle()
mylocation.penup()
mylocation.color('red')
mylocation.goto(str(x), str(y))
mylocation.dot(5)
mylocation.hideturtle()
passiss = 'http://api.open-notify.org/iss-pass.json'
passiss - passiss + '?lat=' + str(x) + '&lon=' + str(y)
response = urllib.request.urlopen(passiss)
result - json.loads(response.read().decode('utf-8'))
print(result)
over = result['response'][1]['risetime']
style = ('Arial', 6, 'bold')
mylocation.write(time.ctime(over), font=style)
turtle.mainloop()
