#add two iNUmber
def add_two(num1,num2):
    return num1 + num2
    
a = float(input("ENter the first number"))
b = float(input("ENter second number"))
total = add_two(a,b)
print(total)

#add two string
def add_string(str1,str2):
    return str1 + str2

first_name = str(input("ENter your first name"))
last_name = str(input("Enter your last name"))
print(add_string(first_name,last_name))
