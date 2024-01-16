import requests
import json
import os

city = input("Enter City Name :- ")

url = f"https://api.weatherapi.com/v1/current.json?key=ba7fc3bede69429699a31242241601&q={city}"

r = requests.get(url)

# print(r.text)

dict = json.loads(r.text)

# print(dict)

# print(dict["current"]["temp_c"])


for key1 in dict :
    for key2 in dict[key1] :
        print(key2,dict[key1][key2])
        command = f"say {city} {key2} is {dict[key1][key2]}"
        os.system(command)