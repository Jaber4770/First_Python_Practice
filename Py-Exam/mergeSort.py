#13. **Merge Two Sorted Lists**
#    Merge two sorted lists into one sorted list (without using sort()).

lst1 = [4,3,5,6,7]
lst2 = [1,9,2,8]
finalList = lst1 + lst2

def sortList(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-1):
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1], lst[j]
    return lst

def checkAndSort(lst):
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            print(f'the list is not sorted. sorting now...')
            return sortList(lst)
    print(f"the list is sorted already.")
        
finalSortedList = checkAndSort(finalList)
print("the sorted list: ", finalSortedList)
















"""
list1 = [1,7,9,8,2,3,4,5,6]
list2 = [1,2,3,4,7,9,8,5,6]

def sort_list(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

def checkAndSort(lst, list_name = 'List'):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i+1]:
            print(f"the list {lst} is not sorted. sorting now...")
            return sort_list(lst)
    print(f"{list_name} is already sorted")
    return lst

list1 = checkAndSort(list1, "List 1")
list2 = checkAndSort(list2, "List 2")

print("Final List 1:", list1)
print("Final List 2:", list2)
finalList = list1 + list2
finalSortedList = checkAndSort(finalList)
print(finalSortedList)
"""