import tkinter
from PIL import Image,ImageTk
import requests
from tkinter import *

window = Tk()
window.title("weather")
window.config(bg="white")


photo=PhotoImage(file="weather_logo.png")
canvas= Canvas(height=200,width=200)
canvas.create_image(100,100,image=photo)
canvas.pack()
canvas.pack(fill="both")
canvas.pack(expand="1")

label=Label(text="enter city name: ")
label.pack()


city_entry=Entry()
city_entry.pack()

api_key ='e4a528c2a3d2b761341caeea6e6e4f12'



def weather():

    codes_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_entry.get()}&appid={api_key}"
    response1 = requests.get(codes_url)

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
            win_speed_km=win_speed * 3,6

            weather_wind_speed_results=Label(text=f"{city_entry.get()}'s wind speed : {win_speed_km} km/h")

            print(f"{city_entry.get()}'s wind speed : {round(win_speed,2)}")
            weather_tempature_result=Label(text=f"{city_entry.get()}'s Temperature: {round(temp_Celcius,2)} C")

            print(f"{city_entry.get()}'s Temperature: {temp_Celcius} C")
            weather_feel_tempature=Label(text=f"{city_entry.get()}'s feels temp: {round(feel_temp_Celcious,2)} C")

            print(f"{city_entry.get()}'s feels temp: {feel_temp_Celcious} C")
            weather_descriptions_result=Label(text=f"{city_entry.get()}'s weather Description: {description}")

            print(f"{city_entry.get()}'s weather Description: {description}")
            weather_tempature_result.pack()
            weather_feel_tempature.pack()
            weather_descriptions_result.pack()
            weather_wind_speed_results.pack()

        else:
            print('Error fetching weather data')
    else:
        print("error codes data url enter information correctly!!!")

my_button=tkinter.Button(text="touch for see weather",command=weather)
my_button.pack()


window.mainloop()