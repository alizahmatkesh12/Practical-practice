def binary_search(array, element):
    low = 0
    high = len(array) - 1
    
    while low <= high:
        mid = (high + low) // 2
        val = array[mid]
        
        if val == element:
            return mid
        elif val < element:
            low = mid + 1
        else:
            high = mid - 1 
   
    return None
    
    
                    
print(binary_search([1, 3, 5, 7, 8, 10], 7))           
                        