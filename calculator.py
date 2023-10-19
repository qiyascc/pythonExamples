get_num = lambda prompt: float(input(prompt))
get_op = lambda: input("Which operation do you want to perform? (+, -, /, x): ")
calc = {
    '+': lambda nums: sum(nums),
    '-': lambda nums: nums[0] - sum(nums[1:]),
    '/': lambda nums: nums[0] / (nums[1] if nums[1] != 0 else 1),
    'x': lambda nums: nums[0] * nums[1]
}

def run_calculator():
    while (n := int(input("How many numbers will you enter? (At least 2): "))) < 2:
        print("You need to enter at least two numbers. Please try again.")
    nums = [get_num(f"Enter number {i + 1}: ") for i in range(n)]
    while (op := get_op()) not in calc:
        print("Invalid operation. Please try again.")
    print(f"Result: {calc[op](nums)}")

run_calculator()