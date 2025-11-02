#14. **Unique Words in a Sentence**
#    Input a sentence and print all unique words (no duplicates).
def findUnique():
    text = input("enter the sentence: ")
    theList = []
    words = text.split()
    for word in words:
        if word not in theList:
            theList.append(word)
    print(theList)
    
findUnique()
