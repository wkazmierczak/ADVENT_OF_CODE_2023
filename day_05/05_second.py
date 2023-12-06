def second_05(file):
    lines = [line.rstrip() for line in file]
    n = len(lines)
    visited = [False for _ in range(n)]
    seeds = lines[0].split(' ')[1:]
    to_remove = []
    cut = []
    to_add = []

    intervals = []
    for i in range(0, len(seeds), 2):
        intervals.append((int(seeds[i]), int(seeds[i]) + int(seeds[i + 1])))
    print(f"init: {intervals}")

    for k in range(len(lines)):
        line = lines[k].split(' ')
        if len(line) != 3:
            for to_a in to_add:
                intervals.append(to_a)
            to_add = []
            # print(f"intervals: {intervals}")
            continue

        to_remove = []
        cut = []

        for j in range(len(line)):
            line[j] = int(line[j])

        diff = line[0] - line[1]
        # print(f"diff: {diff}")

        for elem in intervals:
            s, e = elem
            # print(f'read: {(s, e)}')

            if line[1] <= s < e <= line[1] + line[2]:
                to_remove.append((s, e))
                to_add.append((s + diff, e + diff))
                # print(f'in: {(s, e)}')

            elif line[1] <= s < line[1] + line[2] < e:
                to_remove.append((s, e))
                to_add.append((s + diff, line[1] + line[2] + diff))
                cut.append((line[1] + line[2], e))

            elif s < line[1] < e <= line[1] + line[2]:
                to_remove.append((s, e))
                to_add.append((line[1] + diff, e + diff))
                cut.append((s, line[1]))

            elif s < line[1] < line[1] + line[2] < e:
                to_remove.append((s, e))
                to_add.append((line[1] + diff, line[1] + line[2] + diff))
                cut.append((s, line[1]))
                cut.append((line[1] + line[2], e))

        for to_r in to_remove:
            intervals.remove(to_r)

        for c in cut:
            intervals.append(c)

        # print(intervals)
        # print(cut)
        # print(to_add)
        # print(to_remove)
    for to_a in to_add:
        intervals.append(to_a)

    return min(intervals)[0]


if __name__ == '__main__':
    with open("05_input") as f:
        res = second_05(f)
        print(res)
