def first_05(file):
    lines = [line.rstrip() for line in file]
    n = len(lines)
    visited = [False for _ in range(n)]

    seeds = lines[0].split(' ')[1:]
    for i in range(len(seeds)):
        seeds[i] = int(seeds[i])

    for i in range(1, n):
        line = lines[i].split(' ')
        if len(line) != 3:
            visited = [False for _ in range(n)]
            continue

        for j in range(len(line)):
            line[j] = int(line[j])

        for idx, elem in enumerate(seeds):

            if line[1] <= elem < line[1]+line[2] and not visited[idx]:
                diff = line[0] - line[1]
                seeds[idx] = elem + diff
                visited[idx] = True

    return min(seeds)


if __name__ == '__main__':
    with open("05_input") as f:
        res = first_05(f)
        print(res)