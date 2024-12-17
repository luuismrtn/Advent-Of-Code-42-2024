import time

def adv(ra, opcombo):
    return int(ra / (2 ** opcombo))

def bxl(rb, l):
    return rb ^ l

def bst(l):
    return l % 8

def jnz(ra, l):
    if  ra != 0:
        return l
    return 1

def bxc(rb, rc):
    return rb ^ rc

def get_combo(value, ra, rb, rc):
    match value:
        case 0 | 1 | 2 | 3:
            return value
        case 4:
            return ra
        case 5:
            return rb
        case 6:
            return rc
        case 7:
            return 0

def output(ra, instructions):
    rb = 0
    rc = 0
    ip = 0
    result = []

    while ip < len(instructions):
        if ip + 1 >= len(instructions):
            break

        opcode = instructions[ip]
        operand = instructions[ip + 1]
        opcombo = get_combo(operand, ra, rb, rc)

        match opcode:
            case 0:
                ra = adv(ra, opcombo)
            case 1:
                rb = bxl(rb, operand)
            case 2:
                rb = bst(opcombo)
            case 3:
                next_ip = jnz(ra, operand)
                if next_ip != 1:
                    ip = next_ip
                    continue
            case 4:
                rb = bxc(rb, rc)
            case 5:
                result.append(opcombo % 8)
            case 6:
                rb = adv(ra, opcombo)
            case 7:
                rc = adv(ra, opcombo)
        
        ip += 2

    return result

def find_same_output(instructions):
    
    ra = 0

    possibilities = {0: [x for x in range(8)]}

    for exponent in range(1, len(instructions)):
        possibilities[exponent] = []
        for p in possibilities[exponent - 1]:
            for q in range(8):
                if p == 0:
                    continue
                ra = 8 * p + q
                out = output(ra, instructions)
                if out == instructions[len(instructions) - len(out):]:
                    possibilities[exponent].append(ra)
                if out == instructions:
                    return ra
                
    return None


def main():
    file_path = 'input.txt'

    instructions = []

    with open(file_path, 'r') as f:
        f.readline()
        f.readline()
        f.readline()
        f.readline()

        instructions = list(map(int, f.readline().strip().split(": ")[1].split(",")))
    
    result = find_same_output(instructions)

    print("THE ANSWER IS:", result)


if __name__ == "__main__":
    start_time = time.time()

    main()

    end_time = time.time()
    print(f"Tiempo de ejecución: {end_time - start_time:.2f} segundos")
