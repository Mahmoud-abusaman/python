def greater_than_second(lst):

    if len(lst) < 2:
        return False
    
    second_value = lst[1]
    count = 0
    for num in lst:
        if num > second_value:
            count += 1
    return count


def this_length_that_value(size, value):
    """
    Creates a list of given size where all elements are the given value.
    
    Args:
        size: Length of the list to create
        value: Value to fill the list with
        
    Returns:
        List of given size filled with the specified value
    """
    result = []
    for i in range(size):
        result.append(value)
    return result


def fit_the_first_value(lst):
    """
    If the first value in the list is greater than the list length,
    print "Too big!". If it's smaller, print "Too small!". Otherwise print "Just right!".
    
    Args:
        lst: List of numbers
        
    Returns:
        None (prints a message)
    """
    if len(lst) == 0:
        return
    
    first_value = lst[0]
    list_length = len(lst)
    
    if first_value > list_length:
        print("Too big!")
    elif first_value < list_length:
        print("Too small!")
    else:
        print("Just right!")


def fahrenheit_to_celsius(f_temps):
    """
    Converts a list of Fahrenheit temperatures to Celsius.
    
    Args:
        f_temps: List of Fahrenheit temperatures
        
    Returns:
        List of Celsius temperatures
    """
    c_temps = []
    for f in f_temps:
        c = (f - 32) * 5 / 9
        c_temps.append(c)
    return c_temps


def check_even(num):
    """
    Checks if a number is even and returns a boolean.
    
    Args:
        num: Number to check
        
    Returns:
        True if number is even, False if odd
    """
    return num % 2 == 0


# Test cases to verify the functions
if __name__ == "__main__":
    # Test greater_than_second
    print("greater_than_second([5, 2, 3, 2, 1, 4]):", greater_than_second([5, 2, 3, 2, 1, 4]))  # Expected: 3
    print("greater_than_second([3, 2, 1]):", greater_than_second([3, 2, 1]))  # Expected: 1
    print("greater_than_second([2]):", greater_than_second([2]))  # Expected: False
    
    # Test this_length_that_value
    print("this_length_that_value(3, 7):", this_length_that_value(3, 7))  # Expected: [7, 7, 7]
    print("this_length_that_value(4, 2):", this_length_that_value(4, 2))  # Expected: [2, 2, 2, 2]
    
    # Test fit_the_first_value
    print("fit_the_first_value([5, 2, 3]):", end=" ")
    fit_the_first_value([5, 2, 3])  # Expected: "Too big!"
    
    print("fit_the_first_value([3, 2, 3]):", end=" ")
    fit_the_first_value([3, 2, 3])  # Expected: "Too small!"
    
    print("fit_the_first_value([3, 2, 2]):", end=" ")
    fit_the_first_value([3, 2, 2])  # Expected: "Just right!"
    
    # Test fahrenheit_to_celsius
    print("fahrenheit_to_celsius([32, 212, 0, 100]):", fahrenheit_to_celsius([32, 212, 0, 100]))
    # Expected: [0.0, 100.0, -17.77777777777778, 37.77777777777778]
    
    # Test check_even
    print("check_even(4):", check_even(4))  # Expected: True
    print("check_even(7):", check_even(7))  # Expected: False
    print("check_even(0):", check_even(0))  # Expected: True