def cube(number):
    return number*number*number

def bythree(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False

number = int(input("Enter number: "))
print(bythree(number))

