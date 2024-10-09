import random
from datetime import datetime, timedelta
current_temperature = 25  
current_humidity = 60      
current_wind_speed = 10   
current_rain_chance = 20   
hours_to_simulate = 24
def simulate_temperature(temp):
    change = random.uniform(-2, 2)
    new_temp = temp + change
    return round(new_temp, 2)
def simulate_humidity(humidity):
    change = random.uniform(-5, 5)
    new_humidity = humidity + change
    return max(0, min(100, round(new_humidity)))
def simulate_wind_speed(wind_speed):
    change = random.uniform(-2, 3)
    new_wind_speed = wind_speed + change
    return max(0, round(new_wind_speed, 2))
def simulate_rain_chance(rain_chance):
    change = random.uniform(-10, 10)
    new_rain_chance = rain_chance + change
    return max(0, min(100, round(new_rain_chance)))
def simulate_weather_over_time(start_time, hours):
    weather_data = []
    current_time = start_time
    for _ in range(hours):
        global current_temperature, current_humidity, current_wind_speed, current_rain_chance
        current_temperature = simulate_temperature(current_temperature)
        current_humidity = simulate_humidity(current_humidity)
        current_wind_speed = simulate_wind_speed(current_wind_speed)
        current_rain_chance = simulate_rain_chance(current_rain_chance)
        weather_data.append({
            'Time': current_time.strftime('%Y-%m-%d %H:%M'),
            'Temperature (°C)': current_temperature,
            'Humidity (%)': current_humidity,
            'Wind Speed (km/h)': current_wind_speed,
            'Rain Chance (%)': current_rain_chance
        })
        current_time += timedelta(hours=1)
    return weather_data
start_time = datetime.now()
simulated_weather = simulate_weather_over_time(start_time, hours_to_simulate)
for weather in simulated_weather:
    print(weather)
