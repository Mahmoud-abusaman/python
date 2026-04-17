def biggie_size(lst):

    for i in range(len(lst)):
        if lst[i] > 0:
            lst[i] = "big"
    return lst
print(biggie_size([-1, 3, 5, -5]))

def count_positives(lst):
    count = 0
    for num in lst:
        if num > 0:
            count += 1
    
    if len(lst) > 0:
        lst[-1] = count
    return lst
print(count_positives([-1, 1, 1, 1]))

def sum_total(lst):
    total = 0
    for num in lst:
        total += num
    return total
print(sum_total([2,3,4]))

def average(lst):

    if len(lst) == 0:
        return 0
    
    total = sum_total(lst)
    return total / len(lst)
print(average([2,3,4]))


def length(lst):
    return len(lst)
print(length([2,3,4]))


def minimum(lst):
    if len(lst) == 0:
        return False
    min_val = lst[0]
    for num in lst:
        if num < min_val:
            min_val = num
    return min_val
print(minimum([37, 2, 1, -9]))


def maximum(lst):
    if len(lst) == 0:
        return False
    
    max_val = lst[0]
    for num in lst:
        if num > max_val:
            max_val = num
    return max_val
print(maximum([37, 2, 1, -9]))


def ultimate_analysis(lst):

    analysis = {
        'sum': sum_total(lst),
        'average': average(lst),
        'min': minimum(lst),
        'max': maximum(lst),
        'length': length(lst)
    }
    return analysis
print(ultimate_analysis([2,3,4]))


def reverse_list(lst):
    lst=[]
    for i in range(len(lst) - 1, -1, -1):
        lst.append(lst[i])
    return lst
print(reverse_list([37, 2, 1, -9]))

