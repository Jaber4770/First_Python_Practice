### 🎓 **Python Problem Set (University 1st Year Level)**
#### 🧩 **Part 1 — Basics (1–10)**
#
#1. **Temperature Converter**
#   Convert temperature from Celsius to Fahrenheit and vice versa using user input.

#2. **Simple Interest Calculator**
#   Input `principal`, `rate`, and `time`, then calculate the simple interest.
#
#3. **Leap Year Checker**
#   Check whether a given year is a leap year or not.
#
#4. **Grade Calculator**
#   Take marks for 5 subjects and print total, average, and letter grade.
#
#5. **Positive, Negative, or Zero**
#   Input a number and determine whether it’s positive, negative, or zero.
#
#6. **Odd or Even Counter**
#   Count how many odd and even numbers are in a given list.
#
#7. **Palindrome Checker (Word)**
#   Check if an input string is a palindrome (same forward and backward).
#
#8. **Factorial Using Loop**
#   Find the factorial of a number without using recursion.
#
#9. **Sum of Digits**
#   Input a number like `1234`, output should be `1+2+3+4 = 10`.
#
#10. **Find Largest Among Three Numbers**
#    Input 3 numbers and print the largest.
#
#---
#
#### 🧮 **Part 2 — Lists & Dictionaries (11–20)**
#
#11. **Second Largest Element in a List**
#    Find the 2nd largest number without using sort().
#
#12. **Count Frequency of Elements**
#    Given a list, create a dictionary showing how many times each element occurs.
#
#13. **Merge Two Sorted Lists**
#    Merge two sorted lists into one sorted list (without using sort()).
#
#14. **Unique Words in a Sentence**
#    Input a sentence and print all unique words (no duplicates).
#
#15. **Dictionary Search**
#    Create a dictionary of countries and capitals.
#    Input a country name → show its capital.
#
#16. **Reverse Dictionary**
#    Swap keys and values of a dictionary.
#
#17. **Remove Duplicate Words**
#    Input: `"python is great and python is fun"`
#    Output: `"python is great and fun"`
#
#18. **Sort Dictionary by Value**
#    Sort a dictionary in descending order of its values.
#
#19. **Matrix Addition (2D List)**
#    Take two 2×2 matrices and perform matrix addition.
#
#20. **Student Gradebook**
#    Create a dictionary of students → marks.
#    Print student names who scored above average.
#
#---
#
#### ⚙️ **Part 3 — Functions & Loops (21–25)**
#
#21. **Prime Number Checker (Function)**
#    Write a function `is_prime(n)` that returns True/False.
#
#22. **Fibonacci Series (Function)**
#    Print the first `n` Fibonacci numbers using a function.
#
#23. **Count Vowels & Consonants**
#    Write a function that counts vowels and consonants in a string.
#
#24. **Number Pattern Printing**
#    Print patterns like:
#
#    ```
#    1
#    1 2
#    1 2 3
#    1 2 3 4
#    ```
#
#25. **Perfect Number Checker**
#    A number is perfect if the sum of its divisors equals the number itself.
#    Write a program to check this.
#
#---
#
#### 💡 **Part 4 — Logic & File Handling (26–30)**
#
#26. **Simple Login System**
#    Store usernames & passwords in a dictionary.
#    Input from user → check if login successful.
#
#27. **Count Lines, Words, Characters from File**
#    Read a text file and count number of lines, words, and characters.
#
#28. **Student Result Manager (File Based)**
#    Write student names and marks into a file.
#    Read and print all students with marks ≥ 50.
#
#29. **Word Frequency from File**
#    Read a file and count how many times each word appears.
#
#30. **Mini Project: Contact Book**
#    Create a small contact book using a dictionary:
#
#    * Add contact (name, phone, email)
#    * Search by name
#    * Delete contact
#    * Display all contacts
#
#---
#
#Would you like me to make **solutions** for these 30 (with comments & explanations) — maybe grouped as 3 separate Python files like:
#
#* `part1_basics.py`
#* `part2_collections.py`
#* `part3_functions_and_files.py`
#  ?
#  That would be great for structured learning and practicing.


#------------------------------------------------------------------------------------------------------
#
### 📘 **25 More University-Level Python Problems (List, Dict, Set, Tuple Focused)**
#
#### ✅ **List-Based Problems**
#
#1. **List Rotation**
#   Rotate a list to the right by *k* positions.
#   Example: `[1,2,3,4,5], k=2 → [4,5,1,2,3]`
#
#2. **Find Second Lowest and Second Highest**
#   Given a list of numbers, print 2nd smallest and 2nd largest elements.
#
#3. **Split List into Even and Odd Index Lists**
#   For a given list, create two new lists:
#
#   * One containing elements at even indexes
#   * One containing elements at odd indexes
#
#4. **Replace All Occurrences**
#   Replace all occurrences of a given number in a list with another number.
#
#5. **List of Squares Without Loop (Using List Comprehension)**
#   Input `n` → create list of squares from 1 to n.
#
#6. **Common and Unique Elements in Two Lists**
#   Given two lists, print:
#
#   * Elements common in both
#   * Elements only in first list
#   * Elements only in second list
#
#7. **Sort List of Tuples by Second Value**
#   Example:
#
#   ```
#   data = [(1, 5), (3, 2), (6, 8)]
#   Output: sorted ascending by 2nd value → [(3,2), (1,5), (6,8)]
#   ```
#
#8. **Remove Elements Greater Than a Given Value**
#   Given a list and a number x, remove all elements greater than x.
#
#9. **Find Duplicate Elements in a List**
#   Input: `[1,2,3,2,4,3,5]` → Output: `[2,3]`
#
#10. **Flatten a Nested List (One Level)**
#    Example:
#
#    ```
#    Input: [[1,2], [3,4,5], [6]]
#    Output: [1,2,3,4,5,6]
#    ```
#
#---
#
#### 🟩 **Dictionary-Based Problems**
#
#11. **Frequency of Characters in a String (Using Dict)**
#    Input: `"BANANA"` → Output: `{'B':1,'A':3,'N':2}`
#
#12. **Swap Keys and Values in a Dictionary**
#    Example:
#    `{"a":1, "b":2, "c":3}` → `{1:"a", 2:"b", 3:"c"}`
#
#13. **Delete a Key from Dictionary if Exists**
#    Ask user for a key → if found, delete it, else show "Key not found".
#
#14. **Students Marks Analysis**
#    Given a dict of students and their marks:
#
#    * Find highest mark
#    * Print names of students who passed (≥ 40)
#
#15. **Count Word Lengths in a Sentence**
#    Input: `"Python is easy"`
#    Output: `{ "Python":6, "is":2, "easy":4 }`
#
#16. **Merge Two Dictionaries (Without Built-in .update())**
#    If both have same key, sum their values.
#    Example:
#
#    ```
#    A={"a":3,"b":2}, B={"b":4,"c":5}
#    Output: {"a":3,"b":6,"c":5}
#    ```
#
#17. **Dictionary Sorting by Key and Value**
#    Given a dict:
#
#    * Print dict sorted by keys
#    * Print dict sorted by values
#
#18. **Group Words by First Letter**
#    Input: `["cat","car","dog","apple","door"]`
#    Output:
#
#    ```
#    {
#       'c': ['cat','car'],
#       'd': ['dog','door'],
#       'a': ['apple']
#    }
#    ```
#
#19. **Create a Frequency Dictionary from List of Tuples**
#    Example input: `[("A",10),("B",20),("A",5)]`
#    Output: `{"A":15,"B":20}`
#
#20. **Invert Nested Dictionary Mapping**
#
#    ```
#    data = {"Dhaka": ["A","B"], "Chittagong": ["C"]}
#    Output: {"A":"Dhaka","B":"Dhaka","C":"Chittagong"}
#    ```
#
#---
#
#### 🟧 **Set-Based Problems**
#
#21. **Set Operations**
#    Given two sets, perform: union, intersection, difference, symmetric difference.
#
#22. **Find Unique Words in a Sentence Using Set**
#    Input: `"python is fun and python is powerful"`
#    Output: unique words as a set.
#
#23. **Remove Duplicate Characters from a Word**
#    Input: `"balloon"` → Output: `"balon"` (order not important)
#
#24. **Check if Two Words are Anagrams Using Set**
#    Example: `"listen"` and `"silent"` → True
#
#25. **Set from List of Tuples**
#    Convert a list of tuples into a set of unique tuples.
#    Input: `[(1,2),(2,3),(1,2)]` → `{(1,2),(2,3)}`
#
#---
#
#### 🟪 **Tuple-Based (Short Exam-Style) Problems — Optional If Needed**
#
#*(Say "send more tuple problems" if you want 10 more specifically on tuple)*
#
#---
#
#If you want, I can now:
#✅ Turn this into a **PDF exam sheet**
#✅ Provide **solutions** separately or with hints
#✅ Create a **practice workbook (.py)** with placeholders
#
#Would you like next:
#A) **Solutions for all 25**
#B) More Problems (another 25)?
#C) Convert to Exam Question Paper format (with marks)?
#
##