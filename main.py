import eel
import pyowm

owm = pyowm.OWM("921ff53f10100c24957c6387f91b96c4")


@eel.expose
def get_weather(place):
    mgr = owm.weather_manager()
    city = place
    observation = mgr.weather_at_place(city)
    w = observation.weather

    temp = w.temperature('celsius')['temp']

    return "In " + city + " now " + str(temp) + "*"


eel.init("web")
eel.start("index.html", size=(700, 700))

'''city = "Karagandy, KZ"

owm = pyowm.OWM("921ff53f10100c24957c6387f91b96c4")
mgr = owm.weather_manager()

observation = mgr.weather_at_place(city)
w = observation.weather

temp = w.temperature('celsius')['temp']

print("In " + city + " now " + str(temp) + "*")'''
