#5. **Positive, Negative, or Zero**
#   Input a number and determine whether it’s positive, negative, or zero.
def numChecker():
    number = int(input("enter e naumber: "))
    if number == 0:
        print('its zero')
    elif number < 0:
        print('its negative')
    elif number > 0:
        print("its positive")
numChecker()
