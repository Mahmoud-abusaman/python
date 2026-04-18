# 1. Countdown
def countdown(num):
    result = []
    for i in range(num, -1, -1):
        result.append(i)
    return result


# 2. Print and Return
def print_and_return(lst):
    print(lst[0])
    return lst[1]


# 3. First Plus Length (returns the sum of the first element + length of the list)
def first_plus_length(lst):
    return lst[0] + len(lst)


# 4. return a function that values is greater than the second value in the list inputed.
def values_greater_than_second(lst):
    if len(lst) < 2:
        return False
    
    result = []
    second_value = lst[1]
    
    for val in lst:
        if val > second_value:
            result.append(val)
    
    print(len(result))
    return result


# 5. This Length, That Value (return a list that contains size number elements, with value of value)
def length_and_value(size, value):
    return [value] * size