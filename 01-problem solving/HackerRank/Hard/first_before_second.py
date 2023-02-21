def first_before_second(s,first,second):
    indices_of_first = list()
    for c in range(len(s)):
        if s[c] == first:
            indices_of_first.append(c)
    indices_of_second = list()
    for c in range(len(s)):
        if s[c] == second:
            indices_of_second.append(c)
    flag = True
    for n in indices_of_first:
        for j in indices_of_second:
            if n > j:
                flag = False
            else:
                continue
    return flag


    # print(indices_of_first)
    # print(indices_of_second)
print(first_before_second("a rabbit jumps joyfully", "a", "j"))
print(first_before_second("happy birthday", "a", "y"))