print("Input the first number:")
num1 = int(input())

total = num1  

for i in range(9):  
    print("Input the next number:")
    num = int(input())
    total -= num  

print("Result is:", total)
