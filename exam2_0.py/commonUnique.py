#6. **Common and Unique Elements in Two Lists**
#   Given two lists, print:
#
#   * Elements common in both
#   * Elements only in first list
#   * Elements only in second list

List1 = [1, 2, 3, 4, 5]
List2 = [4, 5, 6, 7, 8]

def find_commn_unique(ls1, ls2):
    set1 = set(ls1)
    set2 = set(ls2)
    
    common = set1 & set2
    onlyFirst = set1 - set2
    onlySecond = set2 - set1
    
    print("Common", common)
    print("only first", onlyFirst)
    print("onlySecond", onlySecond)
    
    
find_commn_unique(List1,List2)