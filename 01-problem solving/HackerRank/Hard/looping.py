def looping(n):
    if n == 1:
        print(n)
    else:
        for rows in range(n):
            print("#" * n)
            for newlines in range(n-1):
                print("\n")
            print("#" * n)
            
looping(4)