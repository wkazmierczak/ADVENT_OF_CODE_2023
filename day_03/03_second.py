with open("03_input") as f:
    digits = "0123456789"
    lines = [line.rstrip() for line in f]
    res = 0

    for k in range(len(lines)):
        # curr_num = ""

        line = lines[k]
        n = len(line)
        for i in range(n):
            if line[i] == "*":
                curr_res = 1
                visited = set()
                cnt = 0

                for j in range(max(0, i - 1), min(i + 2, n)):
                    curr_num = ""
                    if k >= 1 and lines[k - 1][j] in digits and (k - 1, j) not in visited:
                        curr_num = lines[k - 1][j]

                        t = j + 1
                        while t < n and lines[k - 1][t] in digits:
                            curr_num += lines[k - 1][t]
                            visited.add((k - 1, t))
                            t += 1

                        t = j - 1
                        while t >= 0 and lines[k - 1][t] in digits:
                            curr_num = lines[k - 1][t] + curr_num
                            visited.add((k - 1, t))
                            t -= 1

                        if curr_num != "":
                            # print(curr_num)
                            cnt += 1
                            curr_res *= int(curr_num)

                    visited.add((k - 1, j))

                    curr_num = ""

                    if k + 1 < n and lines[k + 1][j] in digits and (k + 1, j) not in visited:
                        curr_num = lines[k + 1][j]

                        t = j + 1
                        while t < n and lines[k + 1][t] in digits:
                            curr_num += lines[k + 1][t]
                            visited.add((k + 1, t))
                            t += 1

                        t = j - 1
                        while t >= 0 and lines[k + 1][t] in digits:
                            curr_num = lines[k + 1][t] + curr_num
                            visited.add((k + 1, t))
                            t -= 1

                        if curr_num != "":
                            # print(curr_num)
                            cnt += 1
                            curr_res *= int(curr_num)

                    visited.add((k + 1, j))

                curr_num = ""

                t = i+1
                while t < n and line[t] in digits:
                    curr_num += line[t]
                    t += 1
                if curr_num != "":
                    cnt += 1
                    # print(curr_num)
                    curr_res *= int(curr_num)

                curr_num = ""

                t = i - 1
                while t >=0 and line[t] in digits:
                    curr_num = line[t] + curr_num
                    t -= 1
                if curr_num != "":
                    # print(curr_num)
                    cnt += 1
                    curr_res *= int(curr_num)

                if cnt == 2:
                    res += curr_res

    print(res)
