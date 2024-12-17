
def adv(ra, opcombo):
    return int(ra / (2 ** opcombo))

def bxl(rb, l):
    return rb ^ l

def bst(l):
    return l % 8

def jnz(ra, l):
    return l if ra != 0 else 1

def bxc(rb, rc):
    return rb ^ rc

def get_combo(value, ra, rb, rc):
    if value == 0:
        return 0
    elif value == 1:
        return 1
    elif value == 2:
        return 2
    elif value == 3:
        return 3
    elif value == 4:
        return ra
    elif value == 5:
        return rb
    elif value == 6:
        return rc
    elif value == 7:
        return 0

def main():
    file_path = 'input.txt'

    ra = 0
    rb = 0
    rc = 0
    instructions = []

    with open(file_path, 'r') as f:
        ra = int(f.readline().strip().split(": ")[1])
        rb = int(f.readline().strip().split(": ")[1])
        rc = int(f.readline().strip().split(": ")[1])
        
        f.readline()

        instructions = list(map(int, f.readline().strip().split(": ")[1].split(",")))

    output = []
    
    ip = 0

    while ip < len(instructions):
        if ip + 1 >= len(instructions):
            break

        opcode = instructions[ip]
        operand = instructions[ip + 1]
        opcombo = get_combo(operand, ra, rb, rc)

        if opcode == 0:
            ra = adv(ra, opcombo)
        elif opcode == 1:
            rb = bxl(rb, operand)
        elif opcode == 2:
            rb = bst(opcombo)
        elif opcode == 3:
            next_ip = jnz(ra, operand)
            if next_ip != 1:
                ip = next_ip
                continue
        elif opcode == 4:
            rb = bxc(rb, rc)
        elif opcode == 5:
            output.append(opcombo % 8)
        elif opcode == 6:
            rb = adv(ra, opcombo)
        elif opcode == 7:
            rc = adv(ra, opcombo)

        ip += 2

    answer = ','.join(map(str, output))
    
    print("THE ANSWER IS:", answer)

if __name__ == "__main__":
    main()