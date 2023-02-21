# def duplicate(phrase):
#     for word in phrase.split():
#         for letter in word:
#             if word.count(letter) > 1:
#                 return False
#     return True


def duplicate(phrase):
    return all(word.count(letter) == 1 for word in phrase.split() for letter in word)

#all() function returns True if all values in the list are True 
#word.count(letter) == 1 evaluates a boolean value in the list 
#try visualize tool to figure out 

print(duplicate("Fortune favours the bold."))
print(duplicate("Look before you leap."))
    