# def twoD(array):
#     lst = list()
#     sum = 0
#     for i in range(len(array)): #5 times
#         sum = 0
#         for j in array: #looping throw rows
#             sum += j[i]
#         lst.append(sum)
#     return max(lst)
   
def twoD(array):
    return max(sum(i) for i in zip(*array))

arr = [
    [0, 0, 0, 0, 0, 0], #[0]
    [0, 0, 0, 0, 1, 0], #[1]
    [0, 0, 1, 0, 1, 0], #[2]
    [0, 1, 1, 1, 1, 0], #[3]
    [1, 1, 1, 1, 1, 1]  #[4]
        ]                   
   #[0][1][2][3][4][5] 
print(twoD(arr))