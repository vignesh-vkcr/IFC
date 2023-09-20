import time

def decorator(func):
    def wrapper():
        print("---starts---")
        func()
        print("---ends---")
    return wrapper

def duration(func):
    def wrapper():
        #print("Time Starts")
        start_time=time.time()
        func()
        duration=time.time()-start_time
        print(f"duration {duration}")
    return wrapper


def printer():
    print("Second Printer")
    time.sleep(2)

printer=duration(printer) # now this printer refers wrapper function of decorator
#printer()
#print(printer)

printer=decorator(printer) 


printer()

print(printer)


