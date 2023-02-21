def evenly_divide(n):
    leap = True
    if n % 4 == 0 :
        if n % 100 == 0:
            if n % 400 == 0:
                return leap
            else:
                return not leap
        else:
            return not leap
print(evenly_divide(16))
# evenly_divide(17)