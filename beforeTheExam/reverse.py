txt = input("write the message to reverse: ")
reversedTxt = ''
reversList = []
for i in range(len(txt)-1, -1, -1):
    reversList.append(txt[i])
    
reversedTxt = ''.join(reversList)
print("ei nen reverse: ",reversedTxt)
print("kam shesh ostad!")