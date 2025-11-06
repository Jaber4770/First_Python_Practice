#2. **Find Second Lowest and Second Highest**
#   Given a list of numbers, print 2nd smallest and 2nd largest elements.
def findHighest(lst):
    highest = lst[0]
    lowest = lst[0]
    secondLargest = None
    secondLowest = None
    for x in lst:
        if highest < x:
            highest = x
        if lowest > x:
            lowest = x
    for x in lst:
        if x < highest:
            if secondLargest is None or x > secondLargest:
                secondLargest = x
        if x > lowest:
            if secondLowest is None or x < secondLowest:
                secondLowest = x
    
    print("Second Largest: ", secondLargest)
    print("Second Lowest: ", secondLowest)

lst = [10,20,30,40,50,60,70,88,90,80,110]
findHighest(lst)