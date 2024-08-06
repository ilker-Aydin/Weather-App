import requests
import turtle
api_key ='e4a528c2a3d2b761341caeea6e6e4f12'
city = input('Enter city name: ')
api_key2="b4a080075a71eb5f544866fa9eae978c"

codes_url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

response1=requests.get(codes_url)

if response1.status_code== 200:
    data1=response1.json()
    lat_code=data1["coord"]["lat"]
    lon_code=data1["coord"]["lon"]



    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat_code}&lon={lon_code}&appid={api_key}'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        description = data["weather"][0]["description"]
        temp_Celcius = temp - 273.15
        feel_temp=data["main"]["feels_like"]
        feel_temp_Celcious= feel_temp - 273.15
        win_speed=data["wind"]["speed"]
        temp_min=data["main"]["temp_min"]
        temp_min_Celcius=temp_min-273.15
        temp_max=data["main"]["temp_max"]
        temp_max_Celcius=temp_max-273.15

        print(f"max temp : {temp_max_Celcius} C")
        print(f"min temp : {temp_min_Celcius} C")
        print(f"wind speed : {win_speed}")
        print(f'Temperature: {temp_Celcius} C')
        print(f"feels temp: {feel_temp_Celcious} C")
        print(f"Description: {description}")

    else:
        print('Error fetching weather data')
else:
    print("error codes data url")