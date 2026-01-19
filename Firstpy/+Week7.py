print("Hello World")
"""
number = int(input("Input a number: "))

def checkd(number):
    if number % 7 == 0:
        print("Number /7 = 0");
    else:
        print("Number /7 != 0")
        
checkd(number)

num = {
    float(input("Input number(1)")),
    float(input("Input number(2)")),
    float(input("Input number(3)")),
}
for numcheck in (num):
    highest = max(num);

print(highest)


country = [
    "Cambodia" == "PhnomPenh",
    "France" == "Paris",
    "Japan" == "Tokyo",
    "Korea" == "Seoul",
]
userc = str(input("Where are you from?\n")).strip().title()


def check(userc):
    if userc in country:
        print(f"Country:{country}, City:{userc}")
        


n=int(input("Height of tree: "))
for i in range(n):
    print(" "*(n-i-1)+"*"*(2*i+1))
for _ in range(n//3):
    print(" "*(n-1)+"I")

import string
text = "i loVe INstitude of teCHnology of cambodia"

print(text.upper())
print(text.lower())
print(text.title())

for ccheck in text:
    if text == "Cambodia":
        print(text)
        


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


print(calculator (num1,calc,num2))

num = {
    float(input("Input number(1)")),
    float(input("Input number(2)")),
    float(input("Input number(3)")),
    float(input("Input number(4)")),
}
def numcheck(num):
    highest = max(num);
    print(highest)

numcheck(num)

num3 = int(input("Enter a number: "))


calc = int(input("Choose an Operator\n1.Add\n2.Subtract\n3.Multiply\n"))  
num1 = int(input("Input number(a): "))
num2 = int(input("Input number(b): "))
def calculator (num1,calc,num2):
    if calc == 1:
        result = num1 + num2;
    elif calc == 2:
        result = num1 - num2;
    elif calc == 3:
        result = num1 * num2;
    else:
        print("Error")
        
    return result


print(calculator (num1,calc,num2))

word = input("Enter a word: ");
def reverse(words):
    reversed = word[::-1]
    print(reversed);
    
reverse(word)


#num = list(map(int, input("Enter numbers: ").split()))

def sum_all (numbers):
    return sum(numbers)

#print(sum_all(num))


num1 = list(set(map(int, input("Enter numbers: ").split())))

print(num1)

"""
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