def last_occurrence(array, element):
    
    low, high = 0, len(array) - 1
    while low <= high:
        mid = (high + low) // 2
        if (array[mid] == element and array[mid] == len(array) -1) or \
            (array[mid] == element and (array[mid+1] > element)):
                return mid
            
        elif array[mid] <= element:
            low = mid + 1
            
        else:
            high = mid - 1
            
print(last_occurrence([2, 2, 2, 3, 3, 4, 4, 5, 5, 5], 4))                           