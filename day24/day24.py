import time

def and_gate(a, b):
    return int(a) & int(b)

def or_gate(a, b):
    return int(a) | int(b)

def xor_gate(a, b):
    return int(a) ^ int(b)

def get_all_values(inputs, output):
    while len(output) > 0:
        first = inputs.get(output[0][0], None)
        second = inputs.get(output[0][2], None)

        if first is not None and second is not None:
            if output[0][1] == "AND":
                inputs[output[0][3]] = and_gate(first, second)
            elif output[0][1] == "OR":
                inputs[output[0][3]] = or_gate(first, second)
            elif output[0][1] == "XOR":
                inputs[output[0][3]] = xor_gate(first, second)
            output.pop(0)
        else:
            output.append(output.pop(0))

    return inputs


def find_z(inputs):
    z_list = {}
    for key, value in inputs.items():
        if key.startswith("z"):
            z_list[key] = value
    return sorted(z_list.items(), key=lambda x: x[0])


def bin_to_decimal(z_list):
    decimal_num = 0
    z_list = z_list[::-1]
    for i in range(len(z_list)):
        decimal_num += int(z_list[i][1]) * (2 ** (len(z_list) - i - 1))
    return decimal_num


def main():
    inputs = {}
    output = []
    with open('input.txt', 'r') as f:
        for line in f:
            if line == "\n":
                break
            line = line.strip().split(": ")
            inputs[line[0]] = line[1]

        for line in f:
            line = line.strip().split(" ")
            output.append((line[0], line[1], line[2], line[4]))


    inputs = get_all_values(inputs, output)

    z_list = find_z(inputs)

    decimal_num = bin_to_decimal(z_list)

    print("THE ANSWER IS:", decimal_num)
    

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Tiempo de ejecución: {end - start:.3f} segundos")