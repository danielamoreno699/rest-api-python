# city, time, temperaure, condition
import requests


def write_to_file(city, time, temperature, condition):
        with open('data.txt', 'a') as f:
            if f.tell() == 0:
                f.write("City, Time, Temperature, Condition\n")
            f.write(f'{city}, {time}, {temperature}, {condition}\n')

def get_weather(city, api_key='d3b5c8aad9b2c60db20bf20d3263fbfa'):
         url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric'
         r = requests.get(url)
         content = r.json()
         #return content
         weather = content['list']

         for forecast in weather:
                temperature = forecast['main']['temp']
                time = forecast['dt_txt']
                condition = forecast['weather'][0]['main']
                city = content['city']['name']
                write_to_file(city, time, temperature, condition)
        
            
print(get_weather(city='London'))
