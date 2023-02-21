def mutate_string(string, position, character):
	lis = string.split()
	lis.insert(position , character)
	newstr = ''.join(lis)
	return newstr

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)