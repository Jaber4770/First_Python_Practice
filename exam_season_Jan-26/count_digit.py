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
