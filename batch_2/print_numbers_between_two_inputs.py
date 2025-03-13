print("Input the first number:")
num1 = int(input())
print("Input the second number:")
num2 = int(input())

if num1 > num2:
    num1, num2 = num2, num1  

for num in range(num1, num2 + 1):
    print(num)
