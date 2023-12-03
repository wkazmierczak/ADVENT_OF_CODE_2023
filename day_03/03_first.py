with open("03_input") as f:
    digits = "0123456789"
    lines = [line.rstrip() for line in f]
    res = 0

    for k in range(len(lines)):
        curr_num = ""
        start = 0
        end = 0
        line = lines[k]
        for i in range(len(line)):
            if line[i] in digits and curr_num == "":
                curr_num += line[i]
                start = i
            elif line[i] in digits and curr_num != "":
                curr_num += line[i]
                if i == len(lines[k])-1:
                    flag = False
                    if start > 0 and line[start - 1] not in digits and line[start - 1] != ".":
                        flag = True

                    if k - 1 >= 0:
                        for j in range(max(start - 1, 0), len(lines[k])):
                            if lines[k-1][j] not in digits and lines[k - 1][j] != ".":  # lines[k-1][j] not in digits and
                                flag = True
                    if k + 1 < len(lines):
                        for j in range(max(start - 1, 0), len(lines[k])):
                            if lines[k+1][j] not in digits and lines[k + 1][j] != ".":
                                flag = True

                    if flag:
                        res += int(curr_num)

            elif line[i] not in digits and curr_num != "":
                flag = False
                end = i
                if start>0 and line[start-1] not in digits and line[start-1] !=".":
                    flag = True
                if end<len(line) and line[end] not in digits and line[end] !=".":
                    flag = True
                if k-1 >= 0:
                    for j in range(max(start-1, 0), end+1):
                        if lines[k-1][j] not in digits and lines[k-1][j] != ".": #lines[k-1][j] not in digits and
                            flag = True
                if k+1 < len(lines):
                    for j in range(max(start-1, 0), end+1):
                        if lines[k+1][j] not in digits and lines[k+1][j] != ".":
                            flag = True

                if flag:
                    res += int(curr_num)

                curr_num = ""
                start = end
                end = start

    print(res)

