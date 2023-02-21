# def consecutive_combo(lst1,lst2):
#     lst3 = sorted((lst1 + lst2))
#     for i in range(len(lst3) - 1):
#         if lst3[i] + 1 == lst3[i+1]:
#             return True
#         else:
#             return False

def consecutive_combo(lst1,lst2):
    flag = False
    count = 0
    lst3 = sorted((lst1+lst2))
    for i in range(1,len(lst3)):
        if lst3[i] - lst3[i - 1] == 1:
            count += 1
    if count == len(lst3) - 1:
        return True
    else:
        return False

print(consecutive_combo([1,3,2], [5,6,4]))  #True
print(consecutive_combo([1,3,2], [5,7,4]))  #False
