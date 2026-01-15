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
