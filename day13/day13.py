import re
from typing import Tuple


class Machine:
    def __init__(self, button_a: Tuple[int, int], button_b: Tuple[int, int], prize: Tuple[int, int]):
        self.button_a = button_a
        self.button_b = button_b
        self.prize = prize

    def calculate_min_tokens(self) -> int:
        MAX_ITERATIONS = 1000
        
        for total_tokens in range(MAX_ITERATIONS):
            for tokens_a in range(total_tokens + 1):
                tokens_b = total_tokens - tokens_a
                
                x_coord = tokens_a * self.button_a[0] + tokens_b * self.button_b[0]
                y_coord = tokens_a * self.button_a[1] + tokens_b * self.button_b[1]
                
                if x_coord == self.prize[0] and y_coord == self.prize[1]:
                    return tokens_a * 3 + tokens_b
        
        return 0
    

def parse_line(line: str) -> Tuple[int, int]:
    match = re.search(r"X\+(\d+), Y\+(\d+)", line)
    if match:
        return int(match.group(1)), int(match.group(2))
    
    match = re.search(r"X=(\d+), Y=(\d+)", line)
    if match:
        return int(match.group(1)), int(match.group(2))
    
    return None


def main():
    file_path = 'input.txt'

    machines = []
    
    with open(file_path, 'r') as f:
        while True:
            button_a_line = f.readline().strip()
            if not button_a_line:
                break
                
            button_a = parse_line(button_a_line)
                
            button_b_line = f.readline().strip()
            button_b = parse_line(button_b_line)
                
            prize_line = f.readline().strip()
            prize = parse_line(prize_line)
                
            machines.append(Machine(button_a, button_b, prize))
                
            f.readline()

    total_tokens = sum(machine.calculate_min_tokens() for machine in machines)

    print("THE ANSWER IS:", total_tokens)

if __name__ == "__main__":
    main()