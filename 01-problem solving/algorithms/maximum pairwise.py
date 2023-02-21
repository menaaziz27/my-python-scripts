def maximum_pairwise(arr):
    res = 0
    for i in arr:
        for j in arr[arr.index(i)+1:]:
            if i * j > res:
                res = i * j
    return res

inp = int(input())
lis = []
lis = input().split()
lis2 = [int(i)for i in lis]
result = maximum_pairwise(lis2)
print(result)

'''
input: 3
1 2 3
output: 6
'''