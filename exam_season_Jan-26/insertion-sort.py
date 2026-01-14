def insertion_sort(arr):
    n = len(arr)
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            
        arr[j + 1] = key
    return arr

lst = [3,5,4,5,6,4,3,2,57,8,5,9,5,4,6,]
print(insertion_sort(lst))
