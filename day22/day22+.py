import time

def gen_num(num, n):
    num = int(num)
    result = num
    sol = []
    for _ in range(n):
        result = (result * 64) ^ result
        result %= 16777216
        
        result = (result // 32) ^ result
        result %= 16777216
        
        result = (result * 2048) ^ result
        result %= 16777216
        result = str(result)
        sol.append(int(result[-1]))
        result = int(result)
    return sol


def calculate_changes(numbers):
    return [numbers[i] - numbers[i-1] for i in range(1, len(numbers))]


def find_sequence_occurrences(numbers, changes):
    sequence_values = {}
    max_index = len(changes) - 3
    
    for i in range(max_index):
        sequence = tuple(changes[i:i + 4])
        value = numbers[i + 3]
        
        if sequence not in sequence_values or value > sequence_values[sequence]:
            sequence_values[sequence] = value
            
    return sequence_values


def find_best_sequence(all_numbers):
    sequence_total_values = {} 
    
    for numbers in all_numbers:
        changes = calculate_changes(numbers)
        buyer_sequences = find_sequence_occurrences(numbers, changes)
        
        for sequence, value in buyer_sequences.items():
            if sequence not in sequence_total_values:
                sequence_total_values[sequence] = 0
            sequence_total_values[sequence] += value
    
    best_sequence = max(sequence_total_values.items(), key=lambda x: x[1])
    return best_sequence


def main():
    file_path = 'input.txt'
    secret_nums = []
    all_numbers = []

    with open(file_path, 'r') as f:
        for line in f:
            secret_nums.append(line.strip())
    
    for secret in secret_nums:
        numbers = gen_num(secret, 2000)
        all_numbers.append(numbers)
    
    _, total_bananas = find_best_sequence(all_numbers)

    print("THE ANSWER IS:", total_bananas)
    

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Tiempo de ejecución: {end - start:.3f} segundos")