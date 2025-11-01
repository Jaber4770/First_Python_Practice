#7. **Palindrome Checker (Word)**
#   Check if an input string is a palindrome (same forward and backward).
def palindrome():
    text = input("enter the text to check palindrome: ")
    reversedText = ''
    textRange = range(len(text))
    # print(textRange)
    for x in textRange:
        index = len(text) -1 -x
        reversedText += text[index]
    if text == reversedText:
        print(f"{text} is a palindrome.")
    else:
        print(f"{text} is not plaindrome.")
palindrome()
