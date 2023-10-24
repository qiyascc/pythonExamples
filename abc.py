def process_numbers(first_digit, second_digit):
    result = []

    result.append(first_digit ** 2)

    for i in range(1, 6):
        second_digit *= 2
        result.append(second_digit + 2)

    return result

first_digit = 3
second_digit = 4
result_list = process_numbers(first_digit, second_digit)
print(result_list)