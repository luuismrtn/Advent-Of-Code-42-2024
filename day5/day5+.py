def main():
    file_path = 'input.txt'

    rules = []
    orders = []
    total_sum = 0

    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if "|" in line:
                rules.append(line)
            elif "," in line:
                orders.append(line)
    
    result = process_orders(orders, rules, total_sum)
    print("THE ANSWER IS:", result)


def process_orders(orders, rules, total_sum):
    while orders:
        order_done = []
        order_valid = True
        current_order = orders.pop(0)
        order_nums = current_order.split(",")

        for order_num in order_nums:
            if check_rule(order_done, order_num, order_nums, rules) or is_in_rule(order_nums, rules):
                order_valid = False
            else:
                order_valid = True
                order_nums = order_correct(order_nums, rules)
                break

        if order_valid:
            middle_index = len(order_nums) // 2
            total_sum += int(order_nums[middle_index])

    return total_sum


def order_correct(order_nums, rules):
    new_order_nums = []
    index = 0
    
    while len(new_order_nums) < len(order_nums) and index < len(order_nums):
        order_num = order_nums[index]

        if order_num in new_order_nums:
            index += 1
        elif (check_rule(new_order_nums, order_num, order_nums, rules) or is_in_rule(order_nums, rules)):
            new_order_nums.append(order_num)
            index = 0
        else:
            index += 1
        
    if new_order_nums == order_nums:
        return [0]
    return new_order_nums

def check_rule(order_done, order_num, order_nums, rules):
    okey = True
    for rule in rules:
        rule_split = rule.split("|")
        if order_num in rule_split[1] and rule_split[0] not in order_nums:
            okey = True
        elif order_num in rule_split[1] and rule_split[0] in order_nums and rule_split[0] not in order_done:
            okey = False
            break
    
    return okey


def is_in_rule(order_nums, rules):
    for rule in rules:
        rule_split = rule.split("|")
        if any(order_num in rule_split[1] for order_num in order_nums):
            return False
    return True


if __name__ == "__main__":
    main()