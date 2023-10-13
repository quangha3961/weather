from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("890x470+320+150")

def getWeather():
    city=textfield.get()

    geolocator=Nominatim(user_agent="geiapiExercises")
    location=geolocator.geocode(city)
    obj=TimezoneFinder()

    result=obj.timezone_at(lng=location.longitude,lat=location.latitude)
    timezone.config(text=result)
    long_lat.config(text=f"{round(location.latitude,4)}°N,{round(location.longitude,4)}°E")

    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M %p")
    clock.config(text=current_time)

    #weather
    api="https://api.openweathermap.org/data/3.0/onecall?lat=33.44&lon=-94.04&exclude=hourly,daily&appid=49ae2e9c5214489d95f13b5e43087667"
    json_data=requests.get(api).json()

    #current
    temp=json_data['current']['temp']
    humidity=json_data['current']['humidity']

    print(humidity)
#backgr
bgimg= tk.PhotoImage(file = "weather\image\gr3.png")
limg= Label(root, i=bgimg)
limg.pack()
root.resizable(False,FALSE)

#icon
image_icon = PhotoImage(file="weather\image\logo.png")
root.iconphoto(False, image_icon)

Round_box=PhotoImage(file="weather\image\gr6.png")
Label(root,image=Round_box).place(x=70,y=86)
#label
label1=Label(root,text="Temperature",font=('Helvetica',11),fg="white",bg="#203243")
label1.place(x=90,y=100)

label2=Label(root,text="Humidity",font=('Helvetica',11),fg="white",bg="#203243")
label2.place(x=90,y=138)

label3=Label(root,text="Pressure",font=('Helvetica',11),fg="white",bg="#203243")
label3.place(x=90,y=176)

label4=Label(root,text="Wind Speed",font=('Helvetica',11),fg="white",bg="#203243")
label4.place(x=90,y=214)

label5=Label(root,text="Description",font=('Helvetica',11),fg="white",bg="#203243")
label5.place(x=90,y=252)

# Search
Search_img=PhotoImage(file="weather\image\gr10.png")
Label(root,image=Search_img).place(x=330,y=180)

textfield=tk.Entry(root,justify='center',width=20,font=('poppins',25,'bold'),bg="#131c24",border=0,fg="white")
textfield.place(x=360,y=193)
textfield.focus()

Search_icon=PhotoImage(file="image\srch.png")
myimg_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#131c24",command=getWeather)
myimg_icon.place(x=735,y=190)
#bottombox
frame=Frame(root,width=900,height=180,bg="#0d0e0f")
frame.place(x=0,y=320)
#bottom boxers
firstbox=PhotoImage(file="weather\image\c12.png")
secondbox=PhotoImage(file="weather\image\c13.png")

Label(frame,image=firstbox).place(x=30,y=20)
Label(frame,image=secondbox).place(x=320,y=9)
Label(frame,image=secondbox).place(x=416,y=9)
Label(frame,image=secondbox).place(x=512,y=9)
Label(frame,image=secondbox).place(x=608,y=9)
Label(frame,image=secondbox).place(x=704,y=9)
Label(frame,image=secondbox).place(x=800,y=9)

#clock
clock=Label(root,font=("Helvetica",30,'bold'),fg="white",bg="#406385")
clock.place(x=80,y=20)
#timezone
timezone=Label(root,font=("Helvetica",20,'bold'),fg="white",bg="#406385")
timezone.place(x=710,y=50)

long_lat=Label(root,font=("Helvetica",10,'bold'),fg="white",bg="#406385")
long_lat.place(x=730,y=80)










#label
Round_box2=PhotoImage(file="weather\image\gr12.png")
Label(root,image=Round_box2).place(x=720,y=10)
root.mainloop()