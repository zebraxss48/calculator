
# This is simple calculator

first_num = int(input("Enter your first number:"))
oprator = input("Enter you options ('+','-','*','/','%' ):")
second_num = int(input("Enter your second number:"))

if oprator == '+':
    print(first_num+second_num)
if oprator == '*':
    print(first_num*second_num)
if oprator == '-':
    print(first_num-second_num)
if oprator == '/':
    print(first_num/second_num)
elif oprator == '%':
    print(first_num%second_num)

else:
    print("Enter valid oprator")