import time

def gen_num(num, n):
    num = int(num)
    n = int(n)
    result = num
    for _ in range(n):
        result = (result * 64) ^ result
        result %= 16777216
        
        result = (result // 32) ^ result
        result %= 16777216
        
        result = (result * 2048) ^ result
        result %= 16777216

    return result


def main():
    file_path = 'input.txt'

    secret_num = []
    total_sum = 0

    with open(file_path, 'r') as f:
        for line in f:
            secret_num.append(line.strip())
    
    for i in range(len(secret_num)):
        num_gen = gen_num(secret_num[i], 2000)
        total_sum += num_gen

    print("THE ANSWER IS:", total_sum)
    

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Tiempo de ejecución: {end - start:.3f} segundos")
