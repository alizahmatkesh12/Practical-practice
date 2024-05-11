"""   
    For example:
    Input: nums = [5,7,7,8,8,8,10], target = 8
    Output: [3,5]
    Input: nums = [5,7,7,8,8,8,10], target = 11
    Output: [-1,-1]
        
"""

def search_insert(nums:list, target:int):
    low = 0
    high = len(nums) - 1
    
    while low <= high:
        mid = low + (high - low) // 2
        if target < nums[mid]:
            high = mid - 1
        elif target > nums[mid]:
            low = mid + 1
        else:
            break               
        
    for j in range(len(nums)-1, -1, -1):
        if nums[j] == target:
            return [mid, j]
        
    return [None, None]        
            

print(search_insert([5,7,7,8,8,8,10], 8))