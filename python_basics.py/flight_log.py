with open("flight_log.txt", "w") as file:
          file.write("Drone ID: DR001\n")
          file.write("Flight duration: 15 minutes\n")
          file.write("Status: Completed\n")

try:
    with open("flight_log.txt", "r") as file:
        contents = file.read()
        print(contents)

except FileNotFoundError:
    print("Flight log file not found.")

try:
    with open("flight_log.txt", "a") as file:
        file.write("Drone ID: DR002\n")
        file.write("Flight duration: 12 minutes\n")
        file.write("Status: Completed\n")

except OSError as error:
    print("File error:", error)


