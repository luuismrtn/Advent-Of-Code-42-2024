import time

def and_gate(a, b):
    return int(a) & int(b)

def or_gate(a, b):
    return int(a) | int(b)

def xor_gate(a, b):
    return int(a) ^ int(b)


def get_all_values(inputs, output, wrong_wires=None):

    highest_z = "z00"
    for _, _, _, res in output:
        if res.startswith("z") and int(res[1:]) > int(highest_z[1:]):
            highest_z = res

    if wrong_wires is None:
        wrong_wires = set()
        for op1, op, op2, res in output:
            if res.startswith("z") and op != "XOR" and res != highest_z:
                wrong_wires.add(res)
            
            if (op == "XOR" and 
                not any(res.startswith(x) for x in ["x", "y", "z"]) and
                not any(op1.startswith(x) for x in ["x", "y", "z"]) and
                not any(op2.startswith(x) for x in ["x", "y", "z"])):
                wrong_wires.add(res)
            
            if op == "AND" and "x00" not in [op1, op2]:
                for sub_op1, sub_op, sub_op2, _ in output:
                    if (res == sub_op1 or res == sub_op2) and sub_op != "OR":
                        wrong_wires.add(res)
            
            if op == "XOR":
                for sub_op1, sub_op, sub_op2, _ in output:
                    if (res == sub_op1 or res == sub_op2) and sub_op == "OR":
                        wrong_wires.add(res)


    return inputs, wrong_wires


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

    inputs, wrong_wires = get_all_values(inputs, output)

    result = ",".join(sorted(wrong_wires))

    print("THE ANSWER IS:", result)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Tiempo de ejecución: {end - start:.3f} segundos")