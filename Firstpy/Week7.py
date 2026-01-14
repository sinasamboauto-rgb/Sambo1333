"""
#TASK 1, PAGE 6
print("Hello world!")

name = str(input("What's your name?\n"));
age = int(input("How old are you?\n"));
birthplace = str(input("Where are you from?\n"))

print(name,age,birthplace)

"""





"""

#TASK 2 & 3, PAGE 7 & 8

num1 = int(input("Input number: "))
calc = input("Choose an Operator Ex, +-*/:  ")
num2 = int(input("Input number: "))

def calculator (num1,calc,num2):
    if calc == "+":
        result = num1 + num2;
    elif calc == "-":
        result = num1 - num2;
    elif calc == "*":
        result = num1 * num2;
    elif calc == "/":
        result = num1 / num2;
        
        
    return result


(calculator (num1,calc,num2))


"""





"""
#TASK 4 PAGE 9

conv = int(input("Chose your Temp. data type:\nChoose 1.°C , 2.°F\n"))

if conv == 1:
    temp = float(input("Input temperature(°C): "))
    result = (temp - 32) * 5/9
    final = result,"°C"
elif conv == 2:
    temp = float(input("Input temperature(°C): "))
    result = (temp * 9/5) + 32
    final = result,"°F"
    
print(final)
"""


"""
#TASK 5, PAGE 10

grade = int(input("Input your score!\n"))

if grade >= 90:
    print("You've passed!, Grade A");
elif grade >= 80:
    print("You've passed, Grade B");
elif grade >= 70:
    print("You've passed, Grade C");
elif grade >= 55:
    print("You've passed, Grade D");
elif grade >= 40:
    print("You've passed, Grade E");
else:
    print("You've Failed, Grade F");
"""



"""
#TASK 6, PAGE 11

num = float(input("Input a number\n"));

def check_even (num):
    if num % 2 != 0:
        print("This is an odd number"); #COULD ALSO USE JUST SIMPLE IF/ELSE INSTEAD OF A FUNCTION.
    else:
        print("This is an Even number");
        
print(check_even(num))
"""




"""
#TASK 7 & 12 PAGE 13 & 18

age = int(input("How old are you?\n"));

def age_check(age):  #SLIDE N.O. 13 & 18
    if age >=65:
        print("Senior");
    elif age >= 18:
        print("Adult");
    elif age >= 12:
        print("Teenage");
    else:
        print("Child");
    if age > 18:
        print("Indiviual is ellegible to Vote")

        
print(age_check(age))

"""




"""
#TASK 8, PAGE 14

num = {
    float(input("Input number(1)")),
    float(input("Input number(2)")),
    float(input("Input number(3)")),
    float(input("Input number(4)")),
}
for numcheck in (num):
    highest = max(num);

print(highest)

"""






"""
#TASK 9, PAGE 15


num2 = int(input("Enter a number: "))

for num_multiplyer in range(1,11):
    print(num2,"x",num_multiplyer,"=",num2 * num_multiplyer)

"""




"""

#TASK 10, PAGE 16

num = int(input("Input a number: "))
fac = 1

for factorial in range(1,num+1):
    fac = fac * factorial
    print("Factorial of",num,"is",fac)
    
    
"""
    
    
    
# BONUS CHALLENGE #########

"""
#STAR PATTERN PRINTING

inputstar = int(input("Input a number: "))

for star in range(1,inputstar+1):
    print("*" * star) #SAME IDEA AS FACTORIAL
"""




#ATM MENU#######



actual_balance = 1000

while True:
    
    print("1.Check balance");
    print("2.Deposit");
    print("3.Withdraw");
    print("4.Exit")
    button = int(input(""))
    
    import time
    
    
    if button == 1:
        print("Your balance is:",actual_balance);
        time.sleep(1.5)
    elif button == 2:
        deposit1 = int(input("How much do you want to deposit?\n"));
        actual_balance = actual_balance + deposit1
        time.sleep(1.5)
        print("Deposit Succeed!")
        time.sleep(0.7)
        
    elif button == 3:
        withdraw1 = int(input("How much do you want to Withdraw?\n"));
        actual_balance = actual_balance - withdraw1
        time.sleep(1.5)
        print("Withdrawed:",withdraw1)
        time.sleep(0.7)
        
    elif button == 4:
        break
    else:
        print("Invalid code#")





#PASSWORD SYSTEM#########


"""


while True:
    password = input("Input your password: ")
    if len(password) <8:
        print("Password must be above 8 Characters")
    elif not any(char.isdigit() for char in password):
        print("Password must contain Numbers")
    elif not any(char.isupper() for char in password):
        print("Password must contain Uppercase Letters")
    else:
        print("Password saved!")
        break
        
        
"""