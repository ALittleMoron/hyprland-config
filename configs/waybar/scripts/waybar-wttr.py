#!/usr/bin/env python

import json
import sys
from datetime import datetime
try:
    import requests
except Exception:
    data = dict(
        text='error',
        tooltip='cant import requests.'
    )
    print(json.dumps(data))
    sys.exit(1)


try:
    WEATHER_CODES = {
        '113': '☀️ ',
        '116': '⛅ ',
        '119': '☁️ ',
        '122': '☁️ ',
        '143': '☁️ ',
        '176': '🌧️',
        '179': '🌧️',
        '182': '🌧️',
        '185': '🌧️',
        '200': '⛈️ ',
        '227': '🌨️',
        '230': '🌨️',
        '248': '☁️ ',
        '260': '☁️ ',
        '263': '🌧️',
        '266': '🌧️',
        '281': '🌧️',
        '284': '🌧️',
        '293': '🌧️',
        '296': '🌧️',
        '299': '🌧️',
        '302': '🌧️',
        '305': '🌧️',
        '308': '🌧️',
        '311': '🌧️',
        '314': '🌧️',
        '317': '🌧️',
        '320': '🌨️',
        '323': '🌨️',
        '326': '🌨️',
        '329': '❄️ ',
        '332': '❄️ ',
        '335': '❄️ ',
        '338': '❄️ ',
        '350': '🌧️',
        '353': '🌧️',
        '356': '🌧️',
        '359': '🌧️',
        '362': '🌧️',
        '365': '🌧️',
        '368': '🌧️',
        '371': '❄️',
        '374': '🌨️',
        '377': '🌨️',
        '386': '🌨️',
        '389': '🌨️',
        '392': '🌧️',
        '395': '❄️ '
    }

    data = {}


    weather = requests.get("https://wttr.in/?format=j1").json()

    def old_format_time(time: str):
        return time.replace('00', "").zfill(2)

    def format_time(time: str):
        filled = time.zfill(4)
        return f'{filled[:2]}:{filled[2:]}'

    def am_pm_to_normal_time(time: str):
        try:
            tm, tm_type = time.split(' ')
            if tm_type == 'AM':
                plus = 0
            else:
                plus = 12
            left_tm, rigth_tm = tm.split(':')
            return f'{str(int(left_tm)+plus).zfill(2)}:{rigth_tm}'
        except Exception:
            return time


    def format_temp(hour):
        return (hour+"°").ljust(3)


    def format_chances(hour):
        chances = {
            "chanceoffog": "Fog",
            "chanceoffrost": "Frost",
            "chanceofovercast": "Overcast",
            "chanceofrain": "Rain",
            "chanceofsnow": "Snow",
            "chanceofsunshine": "Sunshine",
            "chanceofthunder": "Thunder",
            "chanceofwindy": "Wind"
        }

        conditions = []
        for event in chances.keys():
            if int(hour[event]) > 0:
                conditions.append(chances[event]+" "+hour[event]+"%")
        return ", ".join(conditions)

    tempint = int(weather['current_condition'][0]['FeelsLikeC'])
    extrachar = ''
    if tempint > 0 and tempint < 10:
        extrachar = '+'


    data['text'] = f" 󰖐 {weather['current_condition'][0]['FeelsLikeC']}°C" 

    nearest = weather['nearest_area'][0]
    current_condition = weather['current_condition'][0]
    data['tooltip'] = '<b>Geolocation:</b>\n'
    data['tooltip'] += f'City: {nearest["areaName"][0]["value"]}\n'
    data['tooltip'] += f'Latitude: {nearest["latitude"]}\n'
    data['tooltip'] += f'Longitude: {nearest["longitude"]}\n\n'
    data['tooltip'] += '<b>Weather:</b>\n'
    data['tooltip'] += f"{current_condition['weatherDesc'][0]['value']}"
    data['tooltip'] += f" {current_condition['temp_C']}°\n"
    data['tooltip'] += f"Feels like: {weather['current_condition'][0]['FeelsLikeC']}°\n"
    data['tooltip'] += f"Wind: {weather['current_condition'][0]['windspeedKmph']}Km/h\n"
    data['tooltip'] += f"Humidity: {weather['current_condition'][0]['humidity']}%\n"
    for i, day in enumerate(weather['weather']):
        data['tooltip'] += "\n<b>"
        if i == 0:
            data['tooltip'] += "Today, "
        if i == 1:
            data['tooltip'] += "Tomorrow, "
        elif i == 2:
            data['tooltip'] += "The day after tomorrow, "
        data['tooltip'] += f"{day['date']}</b>\n"
        data['tooltip'] += f"⬆️ {day['maxtempC']}° ⬇️ {day['mintempC']}° "
        data['tooltip'] += f"🌅 {am_pm_to_normal_time(day['astronomy'][0]['sunrise'])}"
        data['tooltip'] += f" 🌇 {am_pm_to_normal_time(day['astronomy'][0]['sunset'])}\n"
        for hour in day['hourly']:
            if i == 0:
                if int(old_format_time(hour['time'])) < datetime.now().hour-2:
                    continue
            data['tooltip'] += f"{format_time(hour['time'])}"
            data['tooltip'] += f" {WEATHER_CODES[hour['weatherCode']]}"
            data['tooltip'] += f" {format_temp(hour['FeelsLikeC'])}"
            data['tooltip'] += f" {hour['weatherDesc'][0]['value']}"
            data['tooltip'] += f" {format_chances(hour)}\n"


    print(json.dumps(data))
except Exception as exc:
    data = dict(
        text='󰖐 error',
        tooltip=str(exc),
    )
    print(json.dumps(data))
