with open('02_input.txt') as f:
    lines = [line.rstrip() for line in f]
    digits = "0123456789"
    res = 0
    val = [12, 13, 14]

    d = {"red": 0, "green": 1, "blue": 2}

    for line in lines:
        words = line.split(" ")
        flag = True
        for idx, elem in enumerate(words):
            if idx >= 2 and idx % 2 == 0:
                if idx < len(words)-2 and int(elem) > val[d[words[idx + 1][:-1]]]:
                    flag = False
                    break
                elif idx == len(words)-2 and int(elem) > val[d[words[idx + 1]]]:
                    flag = False
                    break
        if flag:
            res += int(words[1][:-1])

    print(res)
