# ---------------------------------------
def count_digits(start, end):
    result = {}
    for num in range(start, end+1):
        for digit in str(num):
            if digit in result:
                result[digit] += 1
            else:
                result[digit] = 1

    return result


count_digit_result = count_digits(100, 105)
print(count_digit_result)

# ---------------------------------------
# merge dicts


def merge_dicts(d1, d2):
    result = {}
    for x in d1:
        if x in d2:  # time complexity O(n)
            result[x] = d1[x] + d2[x]
    return result


"""     for x in d1:
        for y in d2:
            if x == y: 
                result[x] = d1[x] + d2[y] 
time complexity O(n2)
                """


d1 = {"a": [1], "b": [2], "c": [3, 4]}
d2 = {"a": [3], "b": [4], "d": [3, 4]}

res = merge_dicts(d1, d2)
print("result: ", res)


