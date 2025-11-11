""" 
Write the Python function onlyodd(xlist), xlist being a list of 10 integers in the range (1,20), that returns a list containing only the odd numbers contained in the list xlist.

Answer:(penalty regime: 0 %)
Ace editor not ready. Perhaps reload page?
Falling back to raw text area.
"""


def onlyodd(xlist):
    onlyOddNum = []
    for x in xlist:
        if x % 2 != 0:
            onlyOddNum.append(x)
            
    return onlyOddNum

xlist = [1,2,3,4,5,6,7,8,9,10]
result = onlyodd(xlist)
print(result)