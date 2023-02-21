def calculate_scores(txt):
	return [txt.count(x)for x in "ABC"]

print(calculate_scores("AABBBBACCC"))

# def calculate_scores(txt):
# 	return [txt.count("A"),txt.count("B"),txt.count("C")]