'''
altitude = [10.5, 12.3, 15.7, 14.2, 18.9]
battery = [12.1, 11.8, 11.5, 10.9, 10.5]
temperature = [31.2, 32.5, 34.1, 36.8, 39.2]


def analyse_sensor(readings):
    if not readings:
        print("Dataset is empty.")
        return None

    count = len(readings)
    min_val = min(readings)
    max_val = max(readings)
    avg_val = sum(readings) / count

    print(f"\n--- Sensor Analysis ---")
    print(f"Number of readings: {count}")
    print(f"Minimum: {min_val}")
    print(f"Maximum: {max_val}")
    print(f"Average: {avg_val:.2f}")

    return {
        "count": count,
        "minimum": min_val,
        "maximum": max_val,
        "average": avg_val,
    }


sensor_map = {
    "1": ("Altitude", altitude),
    "2": ("Battery", battery),
    "3": ("Temperature", temperature),
}

print("Select a sensor to analyse:")
print("1. Altitude")
print("2. Battery")
print("3. Temperature")

choice = input("Enter choice (1-3): ").strip()

if choice in sensor_map:
    name, data = sensor_map[choice]
    print(f"\nAnalysing {name}...")
    analyse_sensor(data)
else:
    print("Invalid selection. Please choose 1, 2, or 3.")

'''

altitude = [10.5, 12.3, 15.7, 14.2, 18.9]
battery = [12.1, 11.8, 11.5, 10.9, 10.5]
temperature = [31.2, 32.5, 34.1, 36.8, 39.2]


def analyse_sensor(readings, sensor_name):
    if not readings:
        print("Dataset is empty. ")
        return None

    minimum = min(readings)
    maximum = max(readings)
    average = sum(readings) / len(readings)

    print("Minimum:", minimum)
    print("Maximum:", maximum)
    print("Average:", round(average, 2))

    try:
        threshold = float(input("Enter threshold: "))
    except ValueError:
        print("Please enter a valid number.")
        return None

    count = 0

    for reading in readings:
        if sensor_name =="Battery":
            if reading < threshold:
                count += 1
        else:
            if reading > threshold:
                count += 1

        if sensor_name == "Battery" and reading < 10.8:
            print("Warning: Unsafe battery voltage!", reading)

        elif sensor_name == "Altitude" and reading > 20:
            print("Warning: Altitude limit exceeded!", reading)

        elif sensor_name == "Temperature" and reading > 40:
            print("Warning: Temperature limit exceeded!", reading)

    print("Readings crossing threshold:", count)

sensor_map = {
    "1": ("Altitude", altitude),
    "2": ("Battery", battery),
    "3": ("Temperature", temperature),
}

print("Select a sensor to analyse:")
print("1. Altitude")
print("2. Battery")
print("3. Temperature")

choice = input("Enter choice (1-3): ").strip()

if choice in sensor_map:
    name, data = sensor_map[choice]
    print(f"\nAnalysing {name}...")
    analyse_sensor(data, name)
else:
    print("Invalid selection. Please choose 1, 2, or 3.")



