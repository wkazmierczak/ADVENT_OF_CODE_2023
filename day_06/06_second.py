import math


def second_06(file):
    lines = [line.rstrip() for line in file]
    times = lines[0].split(' ')[1:]
    dist = lines[1].split(' ')[1:]

    curr_t = ''
    curr_d = ''

    for t in times:
        curr_t += t

    for d in dist:
        curr_d += d

    # print(curr_t, curr_d)

    a, b, c = 1, -int(curr_t), int(curr_d)
    delta = b ** 2 - 4 * a * c
    x1 = (-b - delta ** (1 / 2)) / (2 * a)
    x2 = (-b + delta ** (1 / 2)) / (2 * a)
    # print(x1, x2)

    return math.ceil(x2 - 1) - math.floor(x1 + 1) + 1

if __name__ == '__main__':
    with open("06_input") as f:
        res = second_06(f)
        print(res)
