# def counting(txt):
#     words = txt.split(" ")
#     newlist = list()
#     for word in words:
#         if word[0] == word[-1] and len(word) > 1: 
#             newlist.append(word)
#     return len(newlist)

def counting(txt):
    words = txt.split(" ")
    # print(words[-1])
    if not words[-1].isalpha():
        words[-1] = words[-1][:-1]
    # print(words)
    return len([word for word in words if word[0] == word[-1] and len(word) > 1])


print(counting("here halah william is a pop and elegente."))