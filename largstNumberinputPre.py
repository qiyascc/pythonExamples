numbers_list = []

while True:
    user_input = input("Write number (press 'q' to quit): ")
    if user_input.lower() == 'q':
        break
    
    try:
        number = float(user_input)
        numbers_list.append(number)
    except ValueError:
        print("This is not a num.")
    
    if numbers_list:
        print(f"num: {max(numbers_list)}")
