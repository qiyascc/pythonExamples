while True:
    try:
        total_numbers = int(input("How many numbers will you enter: "))
        break
    except ValueError:
        print("Invalid input, please enter a number.")

numbers_list = []

for i in range(1, total_numbers + 1):
    while True:
        try:
            number = float(input(f"Enter number {i}: "))
            numbers_list.append(number)
            break
        except ValueError:
            print("Invalid input, please enter a number.")

print(f"List: {numbers_list}")
print(f"Largest number in the list: {max(numbers_list)}")
