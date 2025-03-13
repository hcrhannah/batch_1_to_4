numbers = []

while True:
    print("Input a number (or type a letter to stop)")
    try:
        num = int(input())
        numbers.append(num)
    except ValueError:
        if numbers:
            average = sum(numbers) / len(numbers)
            print("Average of the numbers:", average)
        else:
            print("No numbers entered.")
        break
