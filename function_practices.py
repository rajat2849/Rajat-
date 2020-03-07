#Return last value of a String 
str1 = input("ENter a string")
def last_char(name):
    return name[-1]

print(last_char(str1))

#Cheack Number is odd or even using Function
number = int(input("Enter a Number"))
def odd_even(num):
    if num%2 == 0:
        return "Even"
    else:
        return "Odd"

print(odd_even(number))

#Pythonic way to use Function and return values 
num1 = int(input("Enter the number"))
def is_even(no):
    return no%2 == 0
    
print(is_even(num1))    

#Function without Paramters 
def song():
    return "Happy brdy to you"

print(song())

#Find grestest number among three digit
no1,no2,no3 = input("Enter three digit").split(",")

def grestest_number(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c

print(grestest_number(int(no1),int(no2),int(no3)))
                