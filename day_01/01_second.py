with open('01_input_first.txt') as f:
    lines = [line.rstrip() for line in f]
    digits = "0123456789"
    digs = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    res = 0

    for line in lines:
        num = ""
        i = 0
        flag = False
        while i < len(line):
            for idx, elem in enumerate(digs):
                if elem in line[:i+1]:
                    num += f"{idx+1}"
                    flag = True
                    break

            if flag:
                break

            if line[i] in digits:
                num += line[i]
                break
            i += 1

        flag = False
        i = len(line) - 1
        while i >= 0:
            for idx, elem in enumerate(digs):
                if elem in line[i:]:
                    num += f"{idx + 1}"
                    flag = True
                    break

            if flag:
                break

            if line[i] in digits:
                num += line[i]
                break
            i -= 1

        res += int(num)

    print(res)

