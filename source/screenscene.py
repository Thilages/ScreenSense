import psutil
import win32gui
import win32process
import time
from datetime import datetime

data = {}
hour_data = {}

while True:
    # returns window handle
    hwnd = win32gui.GetForegroundWindow()

    # returns the process id of that handle
    try:
        _, pid = win32process.GetWindowThreadProcessId(hwnd)
        process_name = psutil.Process(pid).name()
        data[process_name] = data.get(process_name, 0) + 20
        hour_data[datetime.now().hour] = hour_data.get(datetime.now().hour, 0) + 20
        print("unupdated data:", data,hour_data)

        # Ensure we only update the file once every 10 minutes
        if datetime.now().minute % 10 == 0:
            try:
                with open(f"{datetime.today().date()}.txt", "r+") as file:
                    file_data = eval(file.read() or "{}")
            except FileNotFoundError:
                file_data = {}
            try:
                with open(f"{datetime.today().date()}-hour.txt", "r+") as file:
                    file_hour_data = eval(file.read() or "{}")
            except FileNotFoundError:
                file_hour_data = {}

            with open(f"{datetime.today().date()}.txt", "w") as file:
                for process in data:
                    file_data[process] = file_data.get(process, 0) + data[process]
                file.write(str(file_data))

            with open(f"{datetime.today().date()}-hour.txt", "w") as file:
                for hour in hour_data:
                    file_hour_data[hour] = file_hour_data.get(hour, 0) + hour_data[hour]
                file.write(str(file_hour_data))
                print(file_hour_data)

            # Reset the data dictionary
            data = {}
            hour_data = {}
            print("file updated")
            print("data:", file_data)

        # Wait for 20 seconds before repeating the loop
        time.sleep(20)
    except Exception as e:
        print("windows is currently sleeping")
        print(e)
        time.sleep(20)
