numbers = []

while True:
    print("Input a number (or type a letter to stop)")
    try:
        num = int(input())
        numbers.append(num)
    except ValueError:
        if numbers:
            most_frequent = max(set(numbers), key=numbers.count)
            print("Number with the most duplicates:", most_frequent)
        else:
            print("No numbers entered.")
        break
