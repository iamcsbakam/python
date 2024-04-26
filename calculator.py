import sys
import os
import functionexample as basic_calc

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
operation = sys.argv[3]

if operation == "add":
 output = basic_calc.add(num1,num2)
 print(output)
elif operation == "sub":
 output = basic_calc.sub(num1,num2)
 print(output)
elif operation == "mul":
 output = basic_calc.mul(num1,num2)
 print(output)
else:
    print("Invalid operation")

print(os.getenv("password"))
print(os.getenv("token"))
print(os.getenv("apikey"))
print(os.getenv("certificate"))


