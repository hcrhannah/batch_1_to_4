print("Input the First Digit/Number") 
num1 = int(input())
print("Input the Second Digit/Number")
num2 = int(input())
print("Input the Third Digit/Number") 
num3 = int(input())
print("Input the Fourth Digit/Number")
num4 = int(input())
print("Input the Fifth Digit/Number") 
num5 = int(input())
print("Input the Sixth Digit/Number")
num6 = int(input())
print("Input the Seventh Digit/Number") 
num7 = int(input())
print("Input the Eighth Digit/Number")
num8 = int(input())
print("Input the Ninth Digit/Number") 
num9 = int(input())
print("Input the Tenth Digit/Number")
num10 = int(input())

numbers = [num1, num2, num3, num4, num5, num6, num7, num8, num9, num10]
seen = []
output_numbers = []

for num in numbers:
    if num not in seen:
        output_numbers.append(num)
        seen.append(num)

print("Numbers with first occurrence only:", output_numbers)
