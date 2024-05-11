# Using a bidirectional linear search.

def two_sum(numbers, target):
    
    left = 0
    right = len(numbers) - 1

    
    while left < right:
        s = numbers[left] + numbers[right]
        if s == target:
            return [left, right]
        elif s > target:
            right = right -1 
        else:
            left = left + 1
            
print(two_sum([2, 7, 11, 15], target=9))                  

