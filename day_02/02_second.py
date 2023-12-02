with open('02_input.txt') as f:
    lines = [line.rstrip() for line in f]
    digits = "0123456789"
    res = 0

    d = {"red": 0, "green": 1, "blue": 2}

    for line in lines:
        words = line.split(" ")
        tab = [0, 0, 0]
        for idx, elem in enumerate(words):
            if idx >= 2 and idx % 2 == 0:
                if idx < len(words)-2 and int(elem) > tab[d[words[idx + 1][:-1]]]:
                    tab[d[words[idx + 1][:-1]]] = int(elem)
                elif idx == len(words)-2 and int(elem) > tab[d[words[idx + 1]]]:
                    tab[d[words[idx + 1]]] = int(elem)

        res += tab[0]*tab[1]*tab[2]

    print(res)
