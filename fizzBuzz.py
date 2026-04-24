
def fizzBuzz(start,end):
    for i in range(start,end):
        if i%3==0 and i%5==0:
            print("FizzBuzz")
        elif i%3==0:
            print("Fizz")
        elif i%5==0:
            print("Buzz")
        else:
            print(i)

fizzBuzz(1,51)