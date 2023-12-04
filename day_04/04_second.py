with open("04_input") as f:
    lines = [line.rstrip() for line in f]
    res = 0
    n = len(lines)

    multi_cards = [1 for _ in range(n)]
    curr_res = [0 for _ in range(n)]

    for idx, line in enumerate(lines):
        cnt = 0
        first, your_nums = line.split(" | ")
        card, winning = first.split(': ')

        winning = winning.split(" ")
        your_nums = your_nums.split(" ")
        for elem in winning:
            if elem != "" and elem in your_nums:
                cnt += 1

        if cnt > 0:
            curr_res[idx] = 2 ** (cnt - 1)
            for i in range(idx + 1, cnt + idx + 1):
                multi_cards[i] += multi_cards[idx]

    print(multi_cards)
    print(curr_res)


    print(sum(multi_cards))