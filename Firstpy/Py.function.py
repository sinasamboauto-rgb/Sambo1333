
"""
print("Hello world!")

def hisay(age):
    if age <= 1:
        print("Im ",age," Year old!")
    else:
        print("Im ",age," Years old!")
        
hisay(10)




def sayhi(name):
    print("Hi ",name,"!")
    
sayhi("Zin")

"""
"""
def check_odd_even(num):
    return num % 2 == 0;

num = int(input("Pick a number\n"))

if check_odd_even(num):
    print("This is an Even number")
else:
    print("This is an Odd number")
    
"""

"""

def printnumber(n):
    for n in range(1,n+1):
        print(n)


picknumber = int(input("Pick a range of number\n"))

printnumber(picknumber)
"""

def add_num(x):
    x.extend(["50","60"])

y = [20,30,40]

add_num(y)
print(y)


