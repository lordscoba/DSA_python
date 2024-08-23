# def binary_search(array, target):
#     """returns the index position of the target if found, else returns None"""
#     if len(array) == 0:
#         return None
#     else:
#         midpoint = len(array) // 2
#         if array[midpoint] == target:
#             return midpoint
#         else:
#             if target < array[midpoint]:
#                 return binary_search(array[:midpoint], target)
#             else:
#                 return binary_search(array[midpoint + 1:], target)

# or

def binary_search(list, target):
    """returns the index position of the target if found, else returns None"""
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last) // 2
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None