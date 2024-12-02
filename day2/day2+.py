def main():

    sum = 0

    file_path = 'input.txt'

    list = []

    with open(file_path) as f:
        line = f.readline()
        while line:
            list.append(line)
            line = f.readline()
    
    i = 0
    while i < len(list):
        j = 0
        nums = list[i].split(" ")
        while j < len(nums):
            if (all_decreasing(nums) and difference_level(nums, "decreasing")):
                sum += 1
            elif (all_increasing(nums) and difference_level(nums, "increasing")):
                sum += 1
            j += 1
        i += 1


    print("THE ANSWER IS:", sum)

def all_decreasing(nums):
    for i in range(len(nums) - 1):
        if int(nums[i]) > int(nums[i+1]):
            return False
    return True

def all_increasing(nums):
    for i in range(len(nums) - 1):
        if int(nums[i]) < int(nums[i+1]):
            return False
    return True

def difference_level(nums, direction):
    if (direction == "increasing"):
        for i in range(len(nums) - 1):
            if (int(nums[i]) > int(nums[i+1]) + 3) or (int(nums[i]) < int(nums[i+1]) + 1):
                return False
    else:
        for i in range(len(nums) - 1):
            if (int(nums[i]) < int(nums[i+1]) - 3) or (int(nums[i]) > int(nums[i+1]) - 1):
                return False
    return True


if __name__ == "__main__":
    main()
