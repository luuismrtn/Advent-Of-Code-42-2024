import string

def main():

    file_path = 'input.txt'

    text = open(file_path).read()

    sum = 0
    do = True

    i = 0
    while i < len(text):
        ok = True
    
        next_function = pick_next_function(text, i)

        if "don't()" in next_function:
            do = False
        elif "do(" in next_function:
            do = True
        
        if "mul(" in next_function:
            if "," not in next_function:
                ok = False
            j = 0
            num1 = ""
            j = next_function.find("(") + 1
            while next_function[j] != ',' and ok and j < len(next_function) - 1:
                if next_function[j].isdigit():
                    num1 += next_function[j]
                else:
                    ok = False
                if (len(num1) > 3):
                    ok = False
                j += 1

            num2 = ""
            j += 1
            while next_function[j] != ')' and ok:
                if next_function[j].isdigit():
                    num2 += next_function[j]
                else:
                    ok = False
                if (len(num2) > 3):
                    ok = False
                j += 1

            if (ok and do and num1.isdigit() and num2.isdigit()):
                sum += int(num1) * int(num2)

        i = text.find(")", i) + 1
    
    print("THE ANSWER IS:", sum)


def pick_next_function(text, i):
    end = text.find(")", i)
    if end == -1:
        return ""
    
    start = end
    while start > i and text[start] not in ["m", "d"]:
        start -= 1
    
    if text[start] in ["m", "d"]:
        return text[start:end+1]
    
    return ""



if __name__ == "__main__":
    main()
