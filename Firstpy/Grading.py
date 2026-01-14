print("Hello world!")

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
    
