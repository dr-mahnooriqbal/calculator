num1=int(input("enter a number"))
print(" + \n - \n / \n * \n % ")
operand=input("select any operand from the list above")
num2=int(input("write a number"))
if operand=="+":
         print (num1+num2)
elif operand=="-":
         print(num1-num2)
elif operand=="/":
         print(num1/num2)
elif operand=="*":
         print(num1*num2)
elif operand=="%":
         print(num1%num2)
         
else:
         print("Invalid input!")
