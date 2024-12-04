def main():

    sum = 0

    file_path = 'input.txt'

    list = []

    with open(file_path) as f:
        line = f.readline()
        while line:
            list.append(line)
            line = f.readline()
    
    for i in range(len(list)):
        for j in range(len(list[i])):
            if list[i][j] == 'X':
                total = check_word(i, j, list)
                if total > 0:
                    sum += total
    
    print("THE ANSWER IS:", sum)
    
def check_word(i, j, list):
    total = 0

    if j >= 3 and check_left(i, j, list):
        total += 1

    if j <= len(list[i]) - 3 and check_right(i, j, list):
        total += 1

    if i >= 3 and check_up(i, j, list):
        total += 1

    if i <= len(list) - 4 and check_down(i, j, list):
        total += 1

    if i >= 3 and j >= 3 and check_up_left(i, j, list):
        total += 1
    
    if i >= 3 and j <= len(list[i]) - 3 and check_up_right(i, j, list):
        total += 1
    
    if i <= len(list) - 4  and j >= 3 and check_down_left(i, j, list):
        total += 1
    
    if i <= len(list) - 4 and j <= len(list[i]) - 3 and check_down_right(i, j, list):
        total += 1
    
    return total

def check_left(i, j, list):
    if list[i][j - 1] == 'M' and list[i][j - 2] == 'A' and list[i][j - 3] == 'S':
        return True
    else:
        return False

def check_right(i, j, list):
    if list[i][j + 1] == 'M' and list[i][j + 2] == 'A' and list[i][j + 3] == 'S':
        return True
    else:
        return False

def check_up(i, j, list):
    if list[i - 1][j] == 'M' and list[i - 2][j] == 'A' and list[i - 3][j] == 'S':
        return True
    else:
        return False

def check_down(i, j, list):
    if list[i + 1][j] == 'M' and list[i + 2][j] == 'A' and list[i + 3][j] == 'S':
        return True
    else:
        return False

def check_up_left(i, j, list):
    if list[i - 1][j - 1] == 'M' and list[i - 2][j - 2] == 'A' and list[i - 3][j - 3] == 'S':
        return True
    else:
        return False

def check_up_right(i, j, list):
    if list[i - 1][j + 1] == 'M' and list[i - 2][j + 2] == 'A' and list[i - 3][j + 3] == 'S':
        return True
    else:
        return False
    
def check_down_left(i, j, list):
    if list[i + 1][j - 1] == 'M' and list[i + 2][j - 2] == 'A' and list[i + 3][j - 3] == 'S':
        return True
    else:
        return False
    
def check_down_right(i, j, list):
    if list[i + 1][j + 1] == 'M' and list[i + 2][j + 2] == 'A' and list[i + 3][j + 3] == 'S':
        return True
    else:
        return False


if __name__ == "__main__":
    main()
