"""
    array = [False, 2, 4, 'ali', 5, 2]
        return [False, 2, 4, 'ali', 5, 0, 0]
    
"""


def move_zeros(array):
    result = []
    zeros = 0

    for i in array:
        if i == 0 and type(i) != bool:
            zeros += 1
        else:
            result.append(i)
    
    result.extend([0] * zeros)
    return result


print(move_zeros([False, 2, 4, 'ali', 5, 0, 0]))