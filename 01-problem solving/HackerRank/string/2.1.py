inp = input()
print(any(x.isalnum() for x in inp))
print(any(x.isalpha() for x in inp))
print(any(x.isdigit() for x in inp))
print(any(x.islower() for x in inp))
print(any(x.isupper() for x in inp))
