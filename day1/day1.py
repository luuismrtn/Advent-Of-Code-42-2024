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
    
    while (len(listA) > 0 and len(listB) > 0):
        minA = find_min(listA)
        minB = find_min(listB)

        if (minA > minB):
            sum += minA - minB
        else:
            sum += minB - minA
        listA.remove(minA)
        listB.remove(minB)

    print("THE ANSWER IS:", sum)


def find_min(list):
    min = list[0]
    for i in list:
        if i < min:
            min = i
    return min


if __name__ == "__main__":
    main()
