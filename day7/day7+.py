def main():
    file_path = 'input.txt'

    results = []
    operators = []
    sum = 0

    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            line_split = line.split(": ")
            results.append(int(line_split[0]))
            operators.append(line_split[1])

    for i in range(len(results)):
        if evaluate_expression(operators[i], results[i]):
            sum += results[i]

    print("THE ANSWER IS:", sum)


def evaluate_expression(expression, target):
    numbers = list(map(int, expression.split()))

    num_operations = len(numbers) - 1
    total_combinations = 3 ** num_operations

    for mask in range(total_combinations):
        result = (int(numbers[0]))
        current_mask = mask

        for i in range(num_operations):
            op = current_mask % 3
            current_mask //= 3 

            if op == 0:
                result += numbers[i + 1]
            elif op == 1:
                result *= numbers[i + 1]
            elif op == 2:
                result = str(result) + str(numbers[i + 1])
                result = int(result)

        if result == target:
            return True

    return False



if __name__ == "__main__":
    main()
