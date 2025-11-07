#4. **Replace All Occurrences**
#   Replace all occurrences of a given number in a list with another number.

lst = [1, 2, 3, 2, 4, 2, 5]
print('old list: ', lst)
for x in lst:
    if x == 2:
        index = lst.index(2)
        lst[index]=9
print('new list: ', lst)
#------------------------------------------------------------------------------
text = 'The quick brown fox jumps over the laxy dog'
print(text)
splited = list(text)
for x in splited:
    if x == 'o':
        index = splited.index('o')
        splited[index] = "OO"
result = ''.join(splited)
print(result)
#-------------------------------------------------------------------------------
txt = 'the quick brown fox jumps over the laxy dog'
print(txt.title())

#words = txt.split()
#for word in words:
#    firstLetter = word[0].capitalize()
#    print(firstLetter)
#    
#print(words)
# 
# #-------------possible ans:
#txt = 'the quick brown fox jumps over the laxy dog'
# words = txt.split()
# result_words = []
# 
# for w in words:
#     result_words.append(w[0].upper() + w[1:])
# 
# result = " ".join(result_words)
# print(result)
# #
#-------------------------------------------------------------------------------