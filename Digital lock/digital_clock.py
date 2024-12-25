import time
from datetime import datetime

def digital_clock():
    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Current Time:", current_time, end="\r")
        time.sleep(1)

if __name__ == "__main__":
    digital_clock()
