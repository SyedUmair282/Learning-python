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

#type conversion

a = input("x:")
b = int(a) + 1
#c = float(a) + 1
#d = bool(a) + 1
print(f"a={a}, b={b}")

#Conditional operator

temprature = 35
if temprature >= 35:
    print("Today is so hot outside")
elif temprature < 35:
    print("Today is nice outside")
else:
    print("Cold outside")


#Ternary operator

age = 18
message = "Eligible" if age>19 else "Not eligible"
print(message)

#Logical operator

check=True
fit=True

if check and fit:
    print("Both true")
elif check or fit:
    print("One of them true")
else:
    print("None of them true")

#Loops
# i is regular variable and range is how many times to run the loops
#Same as nested loop
for i in range(5):
    print("message:",i)
