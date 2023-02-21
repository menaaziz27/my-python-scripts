def string_filter(l):
    return [ i for i in l if type(i) == int]

lis = [1,2,3,'a','b',5,'mena']
print(string_filter(lis))