def first_occurrence(array, element):
    low, high = 0, len(array) - 1
    
    while low <= high:
        mid = (high + low) // 2
        
        
        if low == high:
            break
        elif array[mid] < element:
            low = mid + 1
        else:
            high = mid    
            
            
    if array[low] == element:
        return low                     
    
    
    
print(first_occurrence([2,3,5,6,7,8,9,10], 7))    