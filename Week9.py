"""
word = input("Enter a word: ");
def reverse(words):
    reversed = word[::-1]
    print(reversed);
    
reverse(word)


########################


num = list(map(int, input("Enter numbers: ").split()))

def sum_all (numbers):
    return sum(numbers)

print(sum_all(num))


########################

num1 = list(set(map(int, input("Enter numbers: ").split())))

print(num1)


num1 = list(map(int, input("Enter numbers: ").split())) #List(map(int, input.split))

#map(function, value)
#"10","20","30" = 10 20 30
#SUM
def sum_all (numbers):
    return sum(numbers)

print(sum_all(num1))


#MIN

def minnum(numbers):
    return min(numbers)

print("Min:" ,minnum(num1))

#MAX

def maxnum(numbers):
    return max(numbers)

print("Max: ",maxnum(num1))

#AVG

def average(numbers):
    return sum(numbers) / len(numbers)

print("Average: ",average(num1))


#REMOVE DUPLICATE

num2 = list(set(map(int, input("Enter numbers: ").split())))

print(num2)

"""

#################################


import time
from datetime import datetime

#print(time.ctime())

#print(time.time())

import time


"""
for i in range(5, 0, -1):
    print(f"Time remaining: {i}")
    time.sleep(1)
    print("Time's up!")
    
    
    
    """
    
    
#while True:
#    time.sleep(2)
#    print(time.ctime())



    
"""
num = int(input("How many second to wait? "))

while True:
    print("Waiting...")
    time.sleep(num)
    print("Done waiting!")
    break
    """


"""
while True:
    time.sleep(1)
    print(time.ctime())
    """
    
"""
timern = int(input("What is the time?"))

if timern > 24:
    print("Invalid time")
elif timern >= 17:
    print("Good evening!")
elif timern >= 12:
    print("Good afternoon!")
else:
    print("Good morning")
"""



now = datetime.now()

#print(now.strftime("%d-%m-%y"))

"""
while True:
    time.sleep(5)
    print("Asleep for 5 second!")
    break
    """
    
#print(now.strftime("%H:%M:%S"))


"""
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

