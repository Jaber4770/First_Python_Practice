#23. **Count Vowels & Consonants**
#    Write a function that counts vowels and consonants in a string.
def VowelConsonantsFinder(text):
    totalVowel = 0
    totalConsonant = 0
    txt = text.lower()
    for x in txt:
        if x in 'aeiou':
            totalVowel += 1  
        elif x.isalpha():
            totalConsonant += 1
    print("total vowel: ",totalVowel)
    print("total consonant: ",totalConsonant)

theText = 'the quick brown fox jumps over the lazy dog'
VowelConsonantsFinder(theText)