print("Input the first Digit/Number") 
num1 = int(input())
print("Input the second Digit/Number")
num2 = int(input())
print("Input the third Digit/Number") 
num3 = int(input())
print("Input the fourth Digit/Number")
num4 = int(input())
print("Input the fifth Digit/Number") 
num5 = int(input())
print("Input the sixth Digit/Number")
num6 = int(input())
print("Input the seventh Digit/Number") 
num7 = int(input())
print("Input the eighth Digit/Number")
num8 = int(input())
print("Input the ninth Digit/Number")
num9 = int(input())
print("Input the tenth Digit/Number")
num10 = int(input())


odd_count = 0


if num1 % 2 != 0:
    odd_count += 1
if num2 % 2 != 0:
    odd_count += 1
if num3 % 2 != 0:
    odd_count += 1
if num4 % 2 != 0:
    odd_count += 1
if num5 % 2 != 0:
    odd_count += 1
if num6 % 2 != 0:
    odd_count += 1
if num7 % 2 != 0:
    odd_count += 1
if num8 % 2 != 0:
    odd_count += 1
if num9 % 2 != 0:
    odd_count += 1
if num10 % 2 != 0:
    odd_count += 1


print("Total odd numbers:", odd_count)
