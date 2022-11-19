from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
import pytz
from datetime import datetime
import requests

class MeteoData():

    def __init__(self, cityname):

        self.cityname = cityname

        geolocalisation = Nominatim(user_agent="geoapiExercices")
        location = geolocalisation.geocode(self.cityname)
        obj = TimezoneFinder()
        resultat = obj.timezone_at(lng=location.longitude, lat=location.latitude)
        home = pytz.timezone(resultat)
        locat_time = datetime.now(home)
        self.actual_time = locat_time.strftime("%H:%M:%S")

        apicle = "96e5845ca3da53f5a1f19e2b3a15157f"

        api = "https://api.openweathermap.org/data/2.5/weather?q=" + self.cityname + "&appid=" + apicle + "&lang=en"

        json_data = requests.get(api).json()
        self.description = json_data["weather"][0]["description"]
        self.temp = int(json_data["main"]["temp"] - 273.15)
        self.pressure = json_data["main"]["pressure"]
        self.humidity = json_data["main"]["humidity"]
        self.wind = json_data["wind"]["speed"]

