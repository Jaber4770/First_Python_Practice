#1. **List Rotation**
#   Rotate a list to the right by *k* positions.
#   Example: `[1,2,3,4,5], k=2 → [4,5,1,2,3]`

def rotate_right(lst, k):
    k = k % len(lst)
    return lst[-k:] + lst[:-k]

print(rotate_right([1,2,3,4,5,6], 3))
