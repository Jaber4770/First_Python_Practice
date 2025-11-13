#Count Even and Odd Numbers
#Given a list of integers, count how many are even and how many are odd.
def oddEvenCounter(list):
        totalOddNumber = 0
        totalEvenNumber = 0
        for x in list:
            if x % 2 == 0:
                totalEvenNumber += 1
            else:
                totalOddNumber += 1
        print(f"total odd number is {totalOddNumber} and total even number is {totalEvenNumber}")

theList = [1,2,3,4,5,6,7,8,9,10,11,12,12,14,15,16,17]
oddEvenCounter(theList)
