print("hello exam!")
#sum of the list
sumList = [1,2,3,4,5,6,6,7,8,9,10]
sum = 0
for x in sumList:
    sum += x
print("sum of the list is: ", sum)

# find Min and Max:
min_ = sumList[0]
max_ = sumList[0]

for x in sumList:
    if min_ > x:
        min_ =x
    if max_ < x:
        max_ = x
        
print('min: ', min_ ,'and the max is: ', max_)
print('min: ', min(sumList))
print('max: ', max(sumList))


#Even & Odd Split
#একটি list থেকে সব জোড় সংখ্যা এবং বিজোড় সংখ্যা আলাদা দুইটা list এ রাখো।
eventOddList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
evenNumber = []
oddNumber = []
for x in eventOddList:
    if x % 2 == 0:
        evenNumber.append(x)
    else:
        oddNumber.append(x)
print("evenNumber: ", evenNumber)
print("oddNumber: ", oddNumber)

#Count Occurrence
#একটি list এ একটি নির্দিষ্ট সংখ্যাটি কতবার এসেছে তা গণনা করো।
countList = [1,2,3,1,3,4,3,5,3,6,7,3,8,9,3,3,10,3]
count = 0
for x in countList:
    if x == 3:
        count += 1
print("the number 3 is available on the list: ", count, 'times')

#Remove Duplicates
#একটি list থেকে ডুপ্লিকেট এলিমেন্ট বাদ দিয়ে নতুন list তৈরি করো।
duplicateList = ['abul','dabul', 'kabul', 'chabul','dabul', 'babul', 'tabul','dabul','dabul','mabul','dabul']
removedDuplicate = []
for x in duplicateList:
    if x not in removedDuplicate:
        removedDuplicate.append(x)
print("duplicate removed: ",removedDuplicate)

#Reverse List Without reverse()
#লুপ ব্যবহার করে একটি list উল্টে দাও (reverse করো)।
rightList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
reversedList = []
for x in range(len(rightList)-1,-1,-1):
    reversedList.append(rightList[x])
print(reversedList)

#Square of Numbers
#একটি list এর প্রতিটি সংখ্যার বর্গ করে নতুন list তৈরি করো।
regularList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
squreList = []
for x in regularList:
    squreList.append(x*x)
print(squreList)
