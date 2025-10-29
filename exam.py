# basic problem
print("hello exam!")
# sum of the list
sumList = [1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10]
sum = 0
for x in sumList:
    sum += x
print("sum of the list is: ", sum)

# find Min and Max:
min_ = sumList[0]
max_ = sumList[0]

for x in sumList:
    if min_ > x:
        min_ = x
    if max_ < x:
        max_ = x

print('min: ', min_, 'and the max is: ', max_)
print('min: ', min(sumList))
print('max: ', max(sumList))


# Even & Odd Split
# একটি list থেকে সব জোড় সংখ্যা এবং বিজোড় সংখ্যা আলাদা দুইটা list এ রাখো।
eventOddList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
evenNumber = []
oddNumber = []
for x in eventOddList:
    if x % 2 == 0:
        evenNumber.append(x)
    else:
        oddNumber.append(x)
print("evenNumber: ", evenNumber)
print("oddNumber: ", oddNumber)

# Count Occurrence
# একটি list এ একটি নির্দিষ্ট সংখ্যাটি কতবার এসেছে তা গণনা করো।
countList = [1, 2, 3, 1, 3, 4, 3, 5, 3, 6, 7, 3, 8, 9, 3, 3, 10, 3]
count = 0
for x in countList:
    if x == 3:
        count += 1
print("the number 3 is available on the list: ", count, 'times')

# Remove Duplicates
# একটি list থেকে ডুপ্লিকেট এলিমেন্ট বাদ দিয়ে নতুন list তৈরি করো।
duplicateList = ['abul', 'dabul', 'kabul', 'chabul', 'dabul',
                 'babul', 'tabul', 'dabul', 'dabul', 'mabul', 'dabul']
removedDuplicate = []
for x in duplicateList:
    if x not in removedDuplicate:
        removedDuplicate.append(x)
print("duplicate removed: ", removedDuplicate)

# Reverse List Without reverse()
# লুপ ব্যবহার করে একটি list উল্টে দাও (reverse করো)।
rightList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
             11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
reversedList = []
for x in range(len(rightList)-1, -1, -1):
    reversedList.append(rightList[x])
print(reversedList)

# Square of Numbers
# একটি list এর প্রতিটি সংখ্যার বর্গ করে নতুন list তৈরি করো।
regularList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
               11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
squreList = []
for x in regularList:
    squreList.append(x*x)
print(squreList)


# Moderate Level (8–14)

# List to Dictionary (Index as Key)
# একটি list কে dictionary তে রূপান্তর করো যেখানে key হবে index, আর value হবে list এর element।
theList = ['abul', 'dabul', 'kabul', 'chabul', 'dabul',
           'babul', 'tabul', 'dabul', 'dabul', 'mabul', 'dabul']
theDict = {}
for x in range(len(theList)):
    theDict[x] = theList[x]
print("the dictionary by the list: ", theDict)

# Dictionary from Two Lists
# দুটি list দেওয়া আছে — একটি keys আর একটি values।
# এগুলো দিয়ে একটি dictionary বানাও।
list1 = ['abul', 'dabul', 'kabul', 'chabul', 'dabul',
         'babul', 'tabul', 'dabul', 'dabul', 'mabul', 'dabul']
list2 = ['abul', 'dabul', 'kabul', 'chabul', 'dabul',
         'babul', 'tabul', 'dabul', 'dabul', 'mabul', 'dabul']
createdDict = {}
for index, value in enumerate(list1):
    createdDict[value] = list2[index]
print(createdDict)

# Filter Dictionary by Value
# একটি dictionary থেকে যেসব value ৫০ এর বেশি সেগুলো রেখে বাকিগুলো বাদ দাও।
original_dict = {'a': 45, 'b': 67, 'c': 23, 'd': 89, 'e': 52, 'f': 38, 'g': 71}
filtered_Dict = {}
for key, value in original_dict.items():
    if value > 50:
        filtered_Dict[key] = value
print('filtered dict: ', filtered_Dict)

lowerFiltered = {}
for key, value in original_dict.items():
    if value < 50:
        lowerFiltered[key] = value
print('lower filtered: ', lowerFiltered)


# Count Word Frequency
# একটি বাক্য দেওয়া আছে — প্রতিটি শব্দ কয়বার এসেছে তা dictionary তে সংরক্ষণ করো।
theSentence = "the quick brown fox jumps over the lazy dog the fox is qucik and the dog is lazy"
splitedSentence = theSentence.split(' ')
countedDict = {}
for word in splitedSentence:
    if word not in countedDict:
        countedDict[word] = 1
    else:
        countedDict[word] = countedDict[word] + 1

print(countedDict)

# Find Common Elements
# দুটি list দেওয়া আছে — কোন কোন element দুটোতেই common আছে তা বের করো।
list11 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list22 = [5, 6, 7, 8, 9, 10, 11, 12, 13]
list33 = []

for x in list11:
    if x in list22:
        list33.append(x)
print(list33)

# Merge Dictionaries
# দুটি dictionary merge করো (যদি একই key থাকে, দ্বিতীয়টার value ব্যবহার করো)।
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'c': 30, 'd': 4, 'e': 5}
margedDict = dict1.copy()
margedDict.update(dict2)


# List of Dictionaries Sorting
# নিচের মতো list দেওয়া আছে:
# students = [
#    {"name": "A", "score": 85},
#    {"name": "B", "score": 92},
#    {"name": "C", "score": 78}
# ]
# এটাকে score অনুযায়ী descending অর্ডারে sort করো।
students = [
    {"name": "A", "score": 85},
    {"name": "B", "score": 92},
    {"name": "C", "score": 78}
]
sortedStu = sorted(students, key=lambda x: x['score'], reverse=True)
print(sortedStu)

sorted_student = sorted(students, key=lambda x: x["score"], reverse=True)
print(sorted_student)


# Advanced Level (15–20)
#
# Nested Dictionary Access
# নিচের dictionary থেকে “Python” এর score বের করো:
#
data = {
    "student": {
        "name": "Jaber",
        "scores": {"Math": 90, "Python": 95, "English": 88}
    }
}
print(data["student"]["scores"]["Python"])


# Unique Values from List of Dicts
# নিচের list থেকে সব unique city বের করো:
#
people = [
    {"name": "A", "city": "Dhaka"},
    {"name": "B", "city": "Chittagong"},
    {"name": "C", "city": "Dhaka"}
]
uniqueCity = []
for person in people:
    if person['city'] not in uniqueCity:
        uniqueCity.append(person['city'])
print(uniqueCity)

for person in people:
    if person['city'] not in uniqueCity:
        uniqueCity.append[person['city']]
print(uniqueCity)

# Group People by City
# উপরের list থেকে city অনুযায়ী group করো।
# Output এর মতো হওয়া উচিত:
#
# {
#    "Dhaka": ["A", "C"],
#    "Chittagong": ["B"]
# }


# List Flattening
# Nested list [ [1,2], [3,4,5], [6] ] কে একটিমাত্র flat list বানাও: [1,2,3,4,5,6]
#
# Top 3 Highest Scores
# একটি dictionary দেওয়া আছে:
#
# marks = {"A": 85, "B": 92, "C": 78, "D": 88, "E": 95}
#
#
# সর্বোচ্চ তিনজন ছাত্রের নাম ও নম্বর বের করো।
#
# Inventory Management
# নিচের মতো একটি dictionary দেওয়া আছে:
#
# inventory = {
#    "apple": {"price": 30, "quantity": 50},
#    "banana": {"price": 10, "quantity": 100},
#    "orange": {"price": 20, "quantity": 80}
# }
#
#
# একটি প্রোগ্রাম লেখো যা total value (price × quantity) হিসাব করবে প্রতিটি item এর এবং শেষে মোট value প্রিন্ট করবে।
#
