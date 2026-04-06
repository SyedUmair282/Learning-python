#Intodunction
print('Welcome to python')
print('*' * 10)
print("hello")

x = 1
y = 2
sum = x+y
print(sum)

name = "umair"
length_of_name = len(name)
print(length_of_name)

print(name[0:3])

#String methods
first = "   umair        "
last = "syed"
full = f"{first} {last}"
print(full)

print(full.title()) #capitalize
print(full.lower()) #lower char
print(full.upper()) #upper char
print(full.lstrip()) #remove left stripe
print(full.rstrip()) #remove right stripe
print(full.find("ye")) #find the index of letter
print(full.replace("d","im")) #replace char with another
print("air" in full) #return bool either it is exist on string
print("air" not in full) #return bool either it is exist on string

#Airthmetic operation
print(10+3)
print(10-3)
print(10*3)
print(f"{(10/3):.2f}")
print(10//3)
print(10**3)

#Math lib
import math
print(round(10/3))
print(abs(-12))
print(math.factorial(5))