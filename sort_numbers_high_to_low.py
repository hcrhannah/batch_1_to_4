numbers = []

while True:
    print("Input a number (or type a letter to stop)")
    try:
        num = int(input())
        numbers.append(num)
    except ValueError:
        if numbers:
            numbers.sort(reverse=True)
            print("Numbers sorted from highest to lowest:", numbers)
        else:
            print("No numbers entered.")
        break
