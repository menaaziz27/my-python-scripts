def expensive_orders(d, k):
    # dic1 = dict()
    # for i in d:
    #     if d[i] > 1000:
    #         dic1[i] = d[i]
    # return dic1
    dic1 = {key:value for key , value in d.items() if d[key] > k}
    return dic1

dic = {'a' : 1001,
        'b' : 1500,
        'c' : 130,
        'd' : 5000
        }

print(expensive_orders(dic,1000))