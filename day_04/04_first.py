with open("04_input") as f:
    lines = [line.rstrip() for line in f]
    res = 0


    for line in lines:
        cnt = 0
        first, your_nums = line.split(" | ")
        card, winning = first.split(': ')

        winning = winning.split(" ")
        your_nums = your_nums.split(" ")
        for elem in winning:
            if elem != "" and elem in your_nums:
                cnt += 1

        if cnt > 0:
            res += 2 ** (cnt - 1)

    print(res)
