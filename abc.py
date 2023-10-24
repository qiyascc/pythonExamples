def generate_sequence(first_digit, second_digit, length):
    sequence = []
    for i in range(length):
        if i % 2 == 0:
            sequence.append(first_digit)
            first_digit = first_digit ** 2
        else:
            sequence.append(second_digit)
            second_digit = 2 * second_digit
    return sequence

first_digit = 3
second_digit = 4
sequence_length = 6

result_sequence = generate_sequence(first_digit, second_digit, sequence_length)
print(result_sequence)