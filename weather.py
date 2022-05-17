import requests

if __name__ == "__main__":
    print("--------------------------------------------------------")
    location = input("Enter City name: ")
    print("--------------------------------------------------------")
    API_key = "2f22bf8c7584207f10a4cbcf2008134d"
    API_call = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_key}"
    data = requests.get(API_call).json()
    if data['cod'] == 404:
        print("Invalid city")
    else:
        temp = round(data['main']['temp']-273.15)
        description = data['weather'][0]['description']
        feels_like = round(data['main']['feels_like']-273.15)
        temp_min = round(data['main']['temp_min']-273.15)
        temp_max = round(data['main']['temp_max']-273.15)
        pressure = data['main']['pressure']
        humidity = data['main']['humidity']
        visibility = (data['visibility'])/1000
        print("********************************************************")
        print(
            f"City: {location}\nCurrent temperature: {temp}°C\nFeels like: {feels_like}°C\nMin - Max temperature: {temp_min}°C - {temp_max}°C\nDescription: {description}\nPressure: {pressure}hPa\nHumidity: {humidity}%\nVisibility: {visibility}km")
        print("********************************************************")
