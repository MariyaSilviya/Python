print('Enter the numbers to perform calculation')
num1=float(input(('Enter number 1')))
num2=float(input(('Enter number 2')))

print('Enter 1 for add')
print('Enter 2 for sub')
print('Enter 3 for mul')
print('Enter 4 for div')

op=input('Enter the choice')

def add(num1,num2):
      return num1+num2
      
def sub(num1,num2):
      return num1-num2
def mul(num1,num2):
      return num1*num2
def div(num1,num2):
      return num1/num2

if op == '1':
      print('Result',add(num1,num2))
elif op == '2':
      print('Result',sub(num1,num2))
elif op == '3':
      print('Result',mul(num1,num2))
elif op == '4':
      print('Result',div(num1,num2))
else:
      print('Invalid choice')