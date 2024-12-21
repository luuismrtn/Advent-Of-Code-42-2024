import time
from collections import deque
from functools import cache
from itertools import pairwise

NUMBER_PAD = {
    "0": [("2", "^"), ("A", ">")],
    "1": [("2", ">"), ("4", "^")],
    "2": [("0", "v"), ("1", "<"), ("3", ">"), ("5", "^")],
    "3": [("2", "<"), ("6", "^"), ("A", "v")],
    "4": [("1", "v"), ("5", ">"), ("7", "^")],
    "5": [("2", "v"), ("4", "<"), ("6", ">"), ("8", "^")],
    "6": [("3", "v"), ("5", "<"), ("9", "^")],
    "7": [("4", "v"), ("8", ">")],
    "8": [("5", "v"), ("7", "<"), ("9", ">")],
    "9": [("6", "v"), ("8", "<")],
    "A": [("0", "<"), ("3", "^")],
}
ARROW_PAD = {
    "^": [("A", ">"), ("v", "v")],
    "<": [("v", ">")],
    "v": [("<", "<"), ("^", "^"), (">", ">")],
    ">": [("v", "<"), ("A", "^")],
    "A": [("^", "<"), (">", "v")],
}

PADS = [NUMBER_PAD, ARROW_PAD]


def bfs(u, v, g):
    q = deque([(u, [])])
    seen = {u}
    shortest = None
    res = []
    while q:
        cur, path = q.popleft()
        if cur == v:
            if shortest is None:
                shortest = len(path)
            if len(path) == shortest:
                res.append("".join(path + ["A"]))
            continue
        if shortest and len(path) >= shortest:
            continue
        for nei, d in g[cur]:
            seen.add(nei)
            q.append((nei, path + [d]))
    return res

@cache
def dfs(seq, level, i=0):
    g = PADS[i]
    res = 0
    seq = "A" + seq
    for u, v in pairwise(seq):
        paths = bfs(u, v, g)
        if level == 0:
            res += min(map(len, paths))
        else:
            res += min(dfs(path, level - 1, 1) for path in paths)
    return res


def main():
    file_path = 'input.txt'

    digits = []
    total_sum = 0

    with open(file_path, 'r') as f:
        for line in f:
            digits.append(line.strip())

    for digit in digits:
        num = int(digit[:3])

        total_sum += dfs(digit, 25) * num


    print("THE ANSWER IS:", total_sum)

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Tiempo de ejecución: {end - start:.3f} segundos")
