numbers = []

while True:
    print("Input a number (or type a letter to stop)")
    try:
        num = int(input())
        numbers.append(num)
    except ValueError:
        if numbers:
            numbers.sort()
            print("Numbers sorted from lowest to highest:", numbers)
        else:
            print("No numbers entered.")
        break
