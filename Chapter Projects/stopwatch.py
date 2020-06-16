#! python3
# stopwatch.py - A simple stopwatch program.


import time


# Display instructions.
print('Press ENTER to begin. Press ENTER again to lap. Press Ctrl-C to quit.')
input()  # Press ENTER to begin.
print('Stopwatch started.')
start_time = time.time()  # Get the first lap's start time.
last_time = start_time
lap_number = 1

# Track lap times.
try:
    while True:
        input()
        lap_time = round(time.time() - last_time, 2)
        total_time = round(time.time() - start_time, 2)
        print(f"Lap {lap_number}: {total_time} ({lap_time}))", end = '')
        lap_number += 1
        last_time = time.time()  # Resets the last lap time.
        
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print('\nStopwatch stopped.')