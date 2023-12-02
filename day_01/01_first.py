with open('01_input_first.txt') as f:
    lines = [line.rstrip() for line in f]
    digits = "0123456789"
    res = 0

    for line in lines:
        num = ""
        i = 0
        while i < len(line):
            if line[i] in digits:
                num += line[i]
                break
            i += 1

        i = len(line) -1
        while i >= 0:
            if line[i] in digits:
                num += line[i]
                break
            i -= 1

        res += int(num)

    print(res)

