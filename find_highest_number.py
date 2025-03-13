numbers = []

while True:
    print("Input a number (or type a letter to stop)")
    try:
        num = int(input())
        numbers.append(num)
    except ValueError:
        if numbers:
            print("Highest number is:", max(numbers))
        else:
            print("No numbers entered.")
        break
