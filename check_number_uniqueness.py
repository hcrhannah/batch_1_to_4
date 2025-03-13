numbers = []

while True:
    print("Input a number (or type a letter to stop)")
    try:
        num = int(input())
        if num in numbers:
            print("Duplicate")
        else:
            print("Unique")
            numbers.append(num)
    except ValueError:
        print("Invalid input detected. Program stopped.")
        break
