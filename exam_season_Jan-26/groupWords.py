# --------------------------------------------
def group_words(words):
    groupWords = {}

    for word in words:
        firstLetter = word[0]

        if firstLetter not in groupWords:
            groupWords[firstLetter] = []
        groupWords[firstLetter].append(word)

    return groupWords


text = "the quick brown fox jumps over the laxy dog"
resullt = group_words(text.split())
print(resullt)
