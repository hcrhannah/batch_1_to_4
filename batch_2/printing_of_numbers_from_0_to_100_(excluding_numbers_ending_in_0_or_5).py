print("Numbers from 0 to 100 (excluding numbers ending in 0 or 5):")

for num in range(101):  
    if num % 10 != 0 and num % 10 != 5:  
        print(num)
