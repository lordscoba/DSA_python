def binary_search(array, target):
    """returns the index position of the target if found, else returns None"""
    if len(array) == 0:
        return False
    else:
        midpoint = len(array) // 2
        if array[midpoint] == target:
            return True
        else:
            if target < array[midpoint]:
                return binary_search(array[:midpoint], target)
            else:
                return binary_search(array[midpoint + 1:], target)
            


def verify(result):
    print("Target found at index: ", result)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = binary_search(numbers, 12)
verify(result)

result = binary_search(numbers, 6)
verify(result)