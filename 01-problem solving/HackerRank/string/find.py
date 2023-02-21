'''In this challenge, the user enters a string and a substring.
You have to print the number of times that the substring occurs in the given string'''
def count_substring(string, sub_string):
    strlen = len(string)
    substrlen = len(sub_string)
    occ = 0
    for i in range(strlen):
        if string[i:i+substrlen] == sub_string:
            occ += 1
    return occ

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)  	

#w momkn n3mlha 3la tol b count function
# w momkn nst3ml find() function
