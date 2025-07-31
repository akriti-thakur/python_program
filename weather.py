# pip install tkinter
# pip install requests
# pip install plyer

import time
from tkinter import *
from tkinter import messagebox as mb
import requests
from plyer import notification

# Function to get notification of weather report
def getNotification():
    cityName = place.get()
    baseUrl = "http://api.openweathermap.org/data/2.5/weather?"
    try:
        complete_url = baseUrl + "appid=" + 'd850f7f52bf19300a9eb4b0aa6b80f0d' + "&q=" + cityName
        response = requests.get(complete_url)
        x = response.json()

        if x.get("cod") != 200:
            raise Exception(x.get("message", "Failed to retrieve data."))

        y = x["main"]
        temp = y["temp"] - 273.15  # Kelvin to Celsius
        pres = y["pressure"]
        hum = y["humidity"]
        z = x["weather"]
        weather_desc = z[0]["description"]

        info = (
            f"Weather in {cityName}:\n"
            f"🌡️ Temperature: {temp:.2f} °C\n"
            f"🧭 Pressure: {pres} hPa\n"
            f"💧 Humidity: {hum}%\n"
            f"🌥️ Description: {weather_desc.capitalize()}"
        )

        # Showing the notification
        notification.notify(
            title="YOUR WEATHER REPORT",
            message=info,
            timeout=5
        )
        time.sleep(5)

    except Exception as e:
        mb.showerror('Error', str(e))  # Show error message if something goes wrong

# GUI window setup
wn = Tk()
wn.title("PythonGeeks Weather Alert")
wn.geometry('700x200')
wn.config(bg='azure')

Label(wn, text="PythonGeeks Weather Desktop Notifier", font=('Courier', 15), fg='grey19', bg='azure').place(x=100, y=15)
Label(wn, text='Enter the Location:', font=("Courier", 13), bg='azure').place(relx=0.05, rely=0.3)

place = StringVar()
place_entry = Entry(wn, width=50, textvariable=place)
place_entry.place(relx=0.5, rely=0.3)

Button(wn, text='Get Notification', font=7, fg='grey19', command=getNotification).place(relx=0.4, rely=0.75)

wn.mainloop()