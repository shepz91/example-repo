def largest_number(list_integers):
    
    if len(list_integers) == 1:
        return list_integers[0]
    
    remainder = largest_number(list_integers[1:])
    
    if list_integers[0] > remainder:
        return list_integers[0]
    else:
        return remainder
        
print(largest_number([3, 1, 6, 8, 2, 4, 5]))
