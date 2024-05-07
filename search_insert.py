"""    
    For example:
    [1,3,5,6], 5 -> 2
    [1,3,5,6], 2 -> 1
    [1,3,5,6], 7 -> 4
    [1,3,5,6], 0 -> 0
    
"""    

def search_insert(array:list, val:int) -> int:
    low = 0
    high = len(array) - 1
    mid = high // 2
    
    
    while low <= high:
        if val > array[mid]:
            mid += 1
            low = mid 
            
        else:
            mid -= 1
            high = mid
            
    return mid 


print( search_insert([1,3,5,6], 7))     
                   