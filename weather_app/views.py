from django.shortcuts import render
import json
import urllib.request
from django.views import View
from django.conf import settings

class IndexView(View):
	def post(self, request):
		city = request.POST['city']
		url = 'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={settings.WEATHERAPI_KEY}'
		source = urllib.request.urlopen(url).read()
		datalist = json.loads(source)
		data = {
			"country_code": str(datalist['sys']['country']),
			"coordinate": str(datalist['coord']['lon']) + ' ' + str(datalist['coord']['lat']),
			"temp": str(datalist['main']['temp']) + 'k',
			"pressure": str(datalist['main']['pressure']),
			"humidity": str(datalist['main']['humidity']),
		}
		print(data)
		return render(request, 'weather_app/index.html', data)

	def get(self, request):
		data = {}
		return render(request, 'weather_app/index.html', data)