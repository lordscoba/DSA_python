def linear_search(array, target):
    """returns the index position of the target if found, else returns None"""
    for i in range(len(array)):
        if array[i] == target:
            return i
    return None    


def verify(result):
    if result is not None:
        print("Target found at index: ", result)
    else:
        print("Target not found in array")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = linear_search(numbers, 12)
verify(result)

result = linear_search(numbers, 6)
verify(result)