import random

result = (lambda rolls: {f'{i}:{i}': rolls.count(i) for i in range(1, 7)})([random.randint(1, 6) for _ in range(100)])
print(result)
print(f"Mirror number probality: {sum(result.values()) / 100}")