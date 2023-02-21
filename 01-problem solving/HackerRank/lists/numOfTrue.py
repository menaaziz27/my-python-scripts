# def num_OF_True(lst):
#     return sum([1 for x in lst if x == True])


def num_OF_True(lst):
    return sum(lst)

    
print(num_OF_True([True,False,True,True,False]))
print(num_OF_True([False,False,False,False,False]))
print(num_OF_True([True,True,True,True,False]))