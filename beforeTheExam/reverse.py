txt = input("write the message to revese: ")
reversedTxt = ''
reversList = []
for i in range(len(txt)-1, -1, -1):
    reversList.append(txt[i])
    
reversedTxt = ''.join(reversList)
print("ei nen revese: ",reversedTxt)
print("kam shesh ostad!")