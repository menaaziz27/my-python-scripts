#DNA
import textwrap
inp = int(input("What's the list size?\n"))
print("Enter you sequences" , inp , "times")
DNA_list = list()
for i in range(inp):
    DNA_list.append(input())
three_seq = list()
with open("sequences.txt" , "w+") as wf:
    for j in DNA_list:
        wrapper = textwrap.TextWrapper(width=3) 
        word_list = wrapper.wrap(text=j)
        for seq in word_list:
            wf.write(seq + "\n")

full_seq = "".join(DNA_list)
capitalize = full_seq.upper()
print("C =", capitalize.count("c".upper()))
print("G =", capitalize.count("g".upper()))
print("T =", capitalize.count("t".upper()))
print("A =", capitalize.count("a".upper()))