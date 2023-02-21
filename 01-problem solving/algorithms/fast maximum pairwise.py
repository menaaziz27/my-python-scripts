def maximum_pairwise(arr):
    max_index1 = -1
    for i in range(len(arr)):
        if arr[i] > max_index1:
            max_index1 = arr[i]
    max_index2 = -1
    for j in range(len(arr)):
        if arr[j] > max_index2 and arr[j] != max_index1:
            max_index2 = arr[j]
    return max_index1 * max_index2

inp = int(input())
lis = [int(i)for i in input().split()]
result = maximum_pairwise(lis)
print(result)

'''
input: 3
1 2 3
output: 6
'''