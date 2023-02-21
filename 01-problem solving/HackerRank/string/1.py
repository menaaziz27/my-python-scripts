def mutate_string(string, position, character):
	newstr = string[:position] + character + string[position + 1 :]
	return newstr

if __name__ == '__main__':
    s = input()
    i, c = input().split() # law 7oshna .split hytalla3 nfs el ntega !
    # print(i ,c)
    s_new = mutate_string(s, int(i), c)
    print(s_new)