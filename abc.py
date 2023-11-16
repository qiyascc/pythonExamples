import random

print({f'{i}:{i}': sum(random.randint(1, 6) == i for _ in range(100)) / 100 for i in range(1, 7)})