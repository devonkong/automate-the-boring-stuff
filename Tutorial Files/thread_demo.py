import threading, time


print("Start program.")

def take_nap():
    time.sleep(5)
    print("Computer has woken up.")
    
thread_obj = threading.Thread(target = take_nap)
thread_obj.start()

print("End of program.")