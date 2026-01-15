# --------------------------------------------
def group_words(words):
    groupWords = {}

    for word in words:
        firstLetter = word[0]

        if firstLetter not in groupWords:
            groupWords[firstLetter] = []
        groupWords[firstLetter].append(word)

    return groupWords


text = "the quick brown fox jumps over the lazy dog"
resullt = group_words(text.split())
print(resullt)


# -----------------------------------------------------
#question: write the Python function stringlist() that asks the user to input some strings and returns the list containing all the strings. the string 'stop' is used to exit theinput phase and it must be excluded from the list returned.

def stringlist():
    text = input("enter text & 'stop' to exit: ")
    result = []

    for x in text.split():
        if x == 'stop':
            break
        result.append(x)
    return result

stringResult = stringlist()
print(stringResult)

#--------------------------------
#oddList:
def onlyodd(xlist):
    result = []
    for x in xlist:
        if x % 2 != 0:
            result.append(x)
    return result

xlist = [1,2,3,4,26,7,8,9,19,20]
resss = onlyodd(xlist)
print(resss)

#----------------------------------------
def alternate_case(s):
    capitalize = True
    result = ''
    for x in s:
        if capitalize:
            result += x.upper()
        else:
            result += x.lower()
        capitalize = not capitalize
    return result
        

s = 'a quick brown fox jumps over the lazy dog'
print(alternate_case(s))