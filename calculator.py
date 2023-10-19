def calculator():
    ops = {'+': sum, '-': lambda ns: ns[0]-sum(ns[1:]), '/': lambda ns: ns[0]/ns[1] if ns[1] else 'Error', 'x': lambda ns: ns[0]*ns[1]}
    while (n := int(input("How many numbers will you enter? (At least 2): "))) < 2: print("At least two numbers are required.")
    nums = [float(input(f"Enter number {i + 1}: ")) for i in range(n)]
    while (op := input("Which operation do you want to perform? (+, -, /, x): ")) not in ops: print("Invalid operation.")
    print(f"Result: {ops[op](nums)}")

calculator()