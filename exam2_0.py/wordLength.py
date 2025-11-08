#15. **Count Word Lengths in a Sentence**
#    Input: `"Python is easy"`
#    Output: `{ "Python":6, "is":2, "easy":4 }`

def wordLength(text):
    words = text.split()
    wordsLength = {}
    for word in words:
        wordsLength[word] = len(word)
    print(wordsLength)
    
text = 'the quick brown fox jumps over the laxy dog'
#text = 'python is easy'
wordLength(text)