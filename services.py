import colorama
import requests
from settings import API_KEY


def get_weather(city_name):
    if not API_KEY:
        print(colorama.Fore.RED + "You must provide an API_KEY!")
        print(colorama.Fore.GREEN, end='', flush=True)
        return

    params = {
        'appid': API_KEY,
        'q': city_name,
        'units': 'metric'
    }

    r = requests.get('http://api.openweathermap.org/data/2.5/weather', params=params)

    if r.status_code == 200:
        body = r.json()
        name = body.get('name')
        temperature = body.get('main').get('temp')
        country_code = body.get('sys').get('country')
        description = body.get("weather")[0].get('main')

        print(colorama.Fore.LIGHTBLUE_EX +
              f"Weather for {body.get('name')} \n"
              f"Country code - {country_code}\n"
              f"Description - {description}\n"
              f"Temperature - {body.get('main').get('temp')}°C", flush=True)
    elif r.status_code == 401:
        print(colorama.Fore.RED + f"Invalid API_KEY!", flush=True)
    elif r.status_code == 404:
        print(colorama.Fore.RED + f"City not found! ({city_name})", flush=True)
    else:
        print(colorama.Fore.RED + "Something went wrong!", flush=True)

    print(colorama.Fore.GREEN, end='', flush=True)
