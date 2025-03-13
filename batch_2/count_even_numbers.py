even_count = 0

for i in range(10):
    print("Input a number:")
    num = int(input())
    if num % 2 == 0:  
        even_count += 1

print("Total even numbers:", even_count)
