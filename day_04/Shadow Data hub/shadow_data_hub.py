import json 

data = {}
data["name"] = input("Name: ")
data["hours_slept"] = int(input("Hours slept: "))
data["hours_coded"] = int(input("Hours coded: "))

if data["hours_coded"] < 1:
    data["status"] = "You can’t build dreams on 30 mins"
if data["hours_slept"] < 6:
    data["status"] = "You need to recover"

with open("Shadow Data hub/data_hub.json", "w") as file:
    json.dump(data, file, indent=4)
