import requests

base_usl = 'http://weather.livedoor.com/forecast/webservice/json/v1'
city_code = '130010'
url = '{}?city={}'.format(base_usl, city_code)
r = requests.get(url)
weather_data = r.json()
print('-- 返却 --')
print(weather_data)