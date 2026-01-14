import time
from datetime import datetime

"""
num = int(input("How many second to wait? "))

while True:
    print("Waiting...")
    time.sleep(num)
    print("Done waiting!")
    break
    
    


while True:
    start = input("Press Enter to start thinking")
    secstart = time.time()
    print("Thinking....")
    input("Press enter to stop thinking")
    stopsec = time.time()
    secondused = print("Thought for = ", stopsec - secstart)
    break


while True:
    input("Press Enter to start activity");
    secstart1 = time.time();
    print("Start time: ",time.ctime())
    
    time.sleep(1.5)
    print("Activity in progress....")
    
    time.sleep(3.5)
    
    endtime1 = time.time();
    print("End time: ",time.ctime())
    
    seconds = endtime1 - secstart1
    time.sleep(0.5)
    print("Total duration: ",round(seconds,2)," seconds")
    break

""" 

#Run as device boots

#time.perf_counter() is monotonic  it only moves forward.#Monotonic (never goes backward)

#time.time() is NOT monotonic  it can jump backward or forward if:

#The system clock is changed

#NTP sync happens

#User manually changes the time

ctime = datetime.now()

print(ctime.strftime("%d-%m-%y %H:%M:%S"))


while True:
    
    start = time.perf_counter()
    
    
    start1 = time.perf_counter()
    n1 = int(input("Input duration(1): "))
    time.sleep(n1)
    end1 = time.perf_counter()
    
    
    start2 = time.perf_counter()
    n2 = int(input("Input duration(2): "))
    time.sleep(n2)
    end2 = time.perf_counter()
    
    start3 = time.perf_counter()
    n3 = int(input("Input duration(3): "))
    time.sleep(n3)
    end3 = time.perf_counter()
    
    
    
    end = time.perf_counter()
    
    print("Total durations: ", round(end - start ,2))
    print("Avg duration: ", round(((end1 - start1)+(end2 - start2)+(end3 - start3)) / 3,2))
    
    break


while True:
    print(time.perf_counter())
    time.sleep(5)
    
    print(time.perf_counter())
    time.sleep(1)
