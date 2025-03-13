print("Numbers from 0 to 100 (excluding numbers ending in 0):")

for num in range(0, 101):  
    if num % 10 != 0:  
        print(num)  
