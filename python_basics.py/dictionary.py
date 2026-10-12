# drone = dict()
drone = {
    "drone_id": "SWARM007",
    "Model_name": "FlyHigh 400",
    "Current_altitude": "546",
    "Battery_percentage": "89",
    "flight_mode": "MANUAL"
}


'''
drone.get("drone_id")

print(drone["drone_id"])

#len()
drone.keys()
drone.values()
drone.items()

height = drone.pop("current_altitude")
drone.popitem()

del drone["flight_mode"]


Method	    What it does
del d[key]	Deletes an entry
d.pop(key)	Deletes an entry and returns its value
d.popitem()	Deletes and returns the last inserted pair
d.clear()	Removes all entries
'''