numbers = []

while True:
    print("Input a number (or type a letter to stop)")
    try:
        num = int(input())
        numbers.append(num)
    except ValueError:
        if numbers:
            print("Lowest number is:", min(numbers))
        else:
            print("No numbers entered.")
        break
