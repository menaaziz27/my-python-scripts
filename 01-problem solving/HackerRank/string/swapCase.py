def swap_case(txt):
    return "".join(x.lower() if x.isupper() else x.upper() for x in txt)

print(swap_case("hElLo wOrlD"))

# return txt.swapcase()