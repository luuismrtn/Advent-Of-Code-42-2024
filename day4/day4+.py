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
            if list[i][j] == 'A':
                if check_word(i, j, list):
                    sum += 1
    
    print("THE ANSWER IS:", sum)
    
def check_word(i, j, list):

    if j < 1 or i < 1:
        return False

    if i >= len(list) - 1 or j >= len(list[i]) - 2:
        return False
    
    if list[i - 1][j - 1] == 'M' and list[i + 1][j + 1] == 'S' and list[i - 1][j + 1] == 'M' and list[i + 1][j - 1] == 'S':
        return True

    if list[i - 1][j - 1] == 'S' and list[i + 1][j + 1] == 'M' and list[i - 1][j + 1] == 'S' and list[i + 1][j - 1] == 'M':
        return True
    
    if list[i - 1][j - 1] == 'M' and list[i + 1][j + 1] == 'S' and list[i - 1][j + 1] == 'S' and list[i + 1][j - 1] == 'M':
        return True
    
    if list[i - 1][j - 1] == 'S' and list[i + 1][j + 1] == 'M' and list[i - 1][j + 1] == 'M' and list[i + 1][j - 1] == 'S':
        return True


if __name__ == "__main__":
    main()
