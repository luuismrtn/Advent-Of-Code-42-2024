from typing import Tuple
import re


def solve(button_a, button_b, prize) -> int:
    (button_a_x, button_a_y), (button_b_x, button_b_y), (prize_x, prize_y) = button_a, button_b, prize
    
    numerator = button_b_x * prize_y - button_b_y * prize_x
    denominator = button_b_x * button_a_y - button_b_y * button_a_x
    
    if numerator % denominator != 0:
        return 0
    
    button_a_tokens = numerator // denominator
    
    remaining_prize_x = prize_x - button_a_x * button_a_tokens
    if remaining_prize_x % button_b_x != 0:
        return 0
    
    button_b_tokens = remaining_prize_x // button_b_x
    
    return button_a_tokens * 3 + button_b_tokens


def parse_line(line: str) -> Tuple[int, int]:
    match = re.search(r"X\+(\d+), Y\+(\d+)", line)
    if match:
        return int(match.group(1)), int(match.group(2))
    
    match = re.search(r"X=(\d+), Y=(\d+)", line)
    if match:
        return int(match.group(1)) + 10000000000000, int(match.group(2)) + 10000000000000
    
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

            machines.append((button_a, button_b, prize))
                
            f.readline()

    total_tokens = sum(solve(*machine) for machine in machines)

    print("THE ANSWER IS:", total_tokens)

if __name__ == "__main__":
    main()
