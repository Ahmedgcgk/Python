import requests
import json
import pyautogui


while True:
    def details():
        print(">------------------------------------------------------------<")
        print(f">        {x["location"]["name"]},{x["location"]["region"]},{x["location"]["country"]}")
        print(f">        Time/Date : {x["location"]["localtime"]}")
        if CorF == "c":
            print(f">        Current Temperature : {x["current"]["temp_c"]} C°")
        elif CorF == "f":
            print(f">        Current Temperature : {x["current"]["temp_f"]} F°")
        print(f">        Wind Speed : {x["current"]["wind_kph"]} Km/h\n>        Direction : {x["current"]["wind_dir"]}")
        print(f">        Humidity : {x["current"]["humidity"]}%")
        print(f">        Precipitation : {x["current"]["precip_mm"]} mm")
        print(">-----------------------------------------------------------<")


    print("---------------------------")
    city = input("Enter city name> ")
    print("---------------------------")
    url = f"https://api.weatherapi.com/v1/current.json?key=67b4ae12787e409baea153000251707&q={city}"
    r = requests.get(url)

    x = json.loads(r.text)
    CorF = input("Fahrenheit (F) or Celsius (C)?> ").strip().lower()
    pyautogui.hotkey('shift', 'tab', 'l')
    details()
    choice = input("Continue? Y/N> ").lower().strip()
    if choice == "n":
        break
    else:
        pyautogui.hotkey('shift', 'tab', 'l')
        continue


