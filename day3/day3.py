def main():

    file_path = 'input.txt'

    text = open(file_path).read();

    sum = 0

    i = 0
    while i < len(text):
        ok = True
        if (text[i] == 'm' and text[i + 1] == 'u' and text[i + 2] == 'l' and text[i + 3] == '('):
            i += 4
            num1 = ""
            while text[i] != ',' and ok:
                num1 += text[i]
                if (len(num1) > 3):
                    ok = False
                i += 1
            
            i += 1

            num2 = ""
            while text[i] != ')' and ok:
                num2 += text[i]
                if (len(num2) > 3):
                    ok = False
                i += 1

            if (ok and is_number(num1) and is_number(num2)):
                sum += int(num1) * int(num2)
            else:
                i -= (len(num2) + len(num1) + 1 + 4)
        i += 1
    
    print("THE ANSWER IS:", sum)

def is_number(s):
    i = 0
    while i < len(s):
        if (not(s[i] >= '0' and s[i] <= '9')):
            return False
        i += 1
    
    return True


if __name__ == "__main__":
    main()
