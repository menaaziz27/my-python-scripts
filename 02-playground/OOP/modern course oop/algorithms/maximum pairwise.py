def maximum_pairwise(arr):
    res = 0
    for i in arr:
        for j in arr[arr.index(i)+1:]:
            if i * j > res:
                res = i * j
    return res

inp = int(input("Enter array length :"))
lis = []
for i in range(inp):
    lis.append(int(input("enter number")))

result = maximum_pairwise(lis)
print(result)