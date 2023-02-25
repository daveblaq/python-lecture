num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
op = input('Enter Operator')

if op == '+':
    print('The addition is', num1+num2)
elif op == '-':
    print('The Subtraction is ', num1-num2)
elif op == '*':
    print('The Multiplication is ',  num1*num2)
elif op == '/':
    print('The Division is ',  abs(num1/num2))
else:
    print('Invalid Operator')
