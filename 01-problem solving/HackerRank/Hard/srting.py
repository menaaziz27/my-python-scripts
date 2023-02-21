def censor_words(txt, lst, char):
    splitting = txt.split()
    for word in range(len(lst)):
        if lst[word] in splitting:
            pos = splitting.index(lst[word])
            splitting[pos] = char*len(lst[word])
    return " ".join(splitting)

# def censor_words(txt, lst, char):
#     for word in lst:
#         txt = txt.replace(word, char*len(word))
#     return txt
   
print(censor_words("Today is a Wednesday!", ["Today", "a"], "-"))

print(censor_words("The cow jumped over the moon.", ["cow", "over"], "*"))
