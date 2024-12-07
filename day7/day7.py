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
    
    for binary_mask in range(1 << (len(numbers) - 1)):
        result = numbers[0]
        for i in range(len(numbers) - 1):
            if (binary_mask >> i) & 1:
                result += numbers[i + 1]
            else:
                result *= numbers[i + 1]

        if result == target:
            return True

    return False


if __name__ == "__main__":
    main()
