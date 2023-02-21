"""


***************
*             *
*             *
*             *
***************


"""

def box (symbol , width ,height):
    if len(symbol) != 1:
        raise Exception ('"symbol" needs to be a string of length 1.')

    if (width < 2 ) and (height < 2):
        raise Exception('Width and Height should be greater or equal to 2.')
    print(symbol * width)

    for i in range (height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)

    print(symbol * width)

box('*' , 15 , 5)
box('*' , 5,15)
box('*' , 1,1)
