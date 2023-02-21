def to_camel_case(text):
    text = text.replace('-',' ')
    text2 = text.replace('_',' ' )
    spl = text2.split()
    lst = [word if word == spl[0] else word.title() for word in spl ]
    return " ".join(lst)

print(to_camel_case("the-stealth-warrior"))
print(to_camel_case("The_Stealth_Warrior"))