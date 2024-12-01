def main():

    sum = 0

    file_path = 'input.txt'

    listA = []
    listB = []

    with open(file_path) as f:
        line = f.readline()
        while line:
            values = line.strip().split("   ")
            listA.append(int(values[0]))
            listB.append(int(values[1]))
            line = f.readline()

    i = 0
    while i < len(listA):
        num = listA[i]
        sum += num * count_numbers(listB, num)
        i += 1

    print("THE ANSWER IS:", sum)

    
def count_numbers(list, num):
    count = 0
    i = 0
    
    while i < len(list):
        if list[i] == num:
            count += 1
        i += 1
    
    return count


if __name__ == "__main__":
    main()
