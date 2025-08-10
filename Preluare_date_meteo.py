import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

url = "https://wttr.in/Bucharest?format=j1"

response = requests.get(url)
data = response.json()

val_curenta = data["current_condition"][0]
temperatura = val_curenta["temp_C"]
temp_resimtita = val_curenta["FeelsLikeC"]
umiditate = val_curenta["humidity"]
desc = val_curenta["weatherDesc"][0]["value"]

weather_data = {
    "Data": [datetime.now().strftime("%Y-%m-%d %H:%M")],
    "Temperatura (C)": [temperatura],
    "Temperatura resmtita (C)": [temp_resimtita],
    "Umiditate (%)": [umiditate],
    "Descriere": [desc],

}

df = pd.DataFrame(weather_data)
df.to_excel("Vremea.xlsx", index = False)
print("Raport meteo salvat!")

