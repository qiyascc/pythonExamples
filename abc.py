import random

def dice_roll_simulation(roll_count):
    double_six_count = 0
    for _ in range(roll_count):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        if die1 == 6 and die2 == 6:
            double_six_count += 1
    probability_of_double_six = double_six_count / roll_count
    return probability_of_double_six

probability = dice_roll_simulation(100)
print(f"İki zarın da altı gelme olasılığı: {probability}")