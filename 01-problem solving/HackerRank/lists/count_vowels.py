# def count_vowels(txt):
# 	count = 0 
# 	vowel = ['a','e','i','o','u']
# 	for character in txt:
# 		if character in vowel:
# 			count += 1
# 	return count

# def count_vowels(txt):
#     return sum([ 1 for x in txt if x.lower() in "aeiuo"])

def count_vowels(txt):
    return len([ x for x in txt if x.lower() in "aeiuo"])


print(count_vowels("aopertyu"))