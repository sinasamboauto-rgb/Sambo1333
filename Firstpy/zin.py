num1 = 10
num2 = 20
numc = num1 * num2
print("The value of numc is: ",numc)

name = "Sina Sambo"
print(name)
print(name[0])
print(name[0:4])

name = "Votey"
age = 18
province = "Phnom Penh"
print("My name is ",name,", I am ",age," Years old"," and I live in ",province,".")

fruits = ["Apple","Orange","Banana","Mango","Papaya"]
print(fruits)

fruits[1] = "Strawberry"
print(fruits)


fruits.append("Tomato")
print(fruits)

fruits.extend(["Guiva","Carrot"])
print(fruits)

fruitexten = (["Apple1","Banana1"])
fruits.extend(fruitexten)
print(fruits)

fruits.remove("Apple1")
print(fruits)

student7 = {
    "name":"Sina Sambo",
    "age":20,
    "province":"Phnom Penh" 
}
print(student7["name"], student7["age"], student7["province"])
print(student7.keys())
print(student7.values())

