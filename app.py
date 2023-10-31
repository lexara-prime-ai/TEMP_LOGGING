import os
import datetime

# Global variables
temperature_ranges: [int, str] = {
    0: "COLD",
    1: "WARM",
    2: "HOT"
}

temperature_range_values: [int, float] = {
    0: 18.0,
    1: 33.0,
    2: 40.0
}

adjectives: [str] = []
range_values: [int] = []

log_file_path = open("temp_logs.log", "a")
time_stamp = datetime.datetime.utcnow()


def respond_to_temperature_changes(temp: str):
    print(f"\n{print(os.fstat(1))}")

    for i in range(0, len(temperature_range_values)):
        adjectives.append(temperature_ranges.get(i))
        range_values.append(temperature_range_values.get(i))

    print(f"Weather: {adjectives}")
    print(f"Temperature range values: {range_values}\n* * * * * * * * * * * *")
    print(f"Current status: {temp.upper()}")

    for i in range(0, len(adjectives)):
        if temp.upper() == adjectives[i]:
            print(f"Temperature reading: {range_values[i]}")
            log_temperature(temp.upper(), f"Temperature reading: {range_values[i]}", time_stamp)


def log_temperature(temp: str, temperature_reading, log_time):
    print("Writing logs...")
    log_file_path.write(f"Weather: {temp.upper()}, {temperature_reading}, {log_time}\n")


print(os.popen('vcgencmd measure_temp').readline())
