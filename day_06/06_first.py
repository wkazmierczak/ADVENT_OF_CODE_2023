import math


def first_06(file):
    lines = [line.rstrip() for line in file]
    times = lines[0].split(' ')[1:]
    dist = lines[1].split(' ')[1:]
    n_times = []
    n_dist = []
    res = 1
    for t in times:
        if t != '':
            n_times.append(int(t))

    for d in dist:
        if d != '':
            n_dist.append(int(d))

    # print(n_times)
    # print(n_dist)

    for t, d in zip(n_times, n_dist):
        a, b, c = 1, -t, d
        delta = b ** 2 - 4 * a * c
        x1 = (-b - delta ** (1 / 2)) / (2 * a)
        x2 = (-b + delta ** (1 / 2)) / (2 * a)
        # print(x1, x2)
        res *= (math.ceil(x2 - 1) - math.floor(x1 + 1) + 1)
        # print(math.ceil(x2 - 1) - math.floor(x1 + 1) + 1)

    return res


if __name__ == '__main__':
    with open("06_input") as f:
        res = first_06(f)
        print(res)
