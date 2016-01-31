def rev(lst):
    '''(list)->(list)
    This function is made to make the reversed value of the input ilst presentation of the number in base (-2). 
    >>> rev([1,1,0,1])
    [1, 0, 0, 1, 1, 1, 1]
    >>> rev([1,3,1,0,1]
    'Not a binary' '''
    val = 0
    r_lst = []
    for i in range(len(lst)):
        if lst[i] not in [0,1]: return "Not a binary" # If not in base 2 - exit
        val += lst[i] * (-2)**i # Else is not a must here. Take the value and turn it into decimal
    # Show the value and its reversed value. No need to reverse it val=-val, as test showed
    # print (val, -val) 
    while val: # while True
        r_lst.append(abs(val % (-2))) # Check the modulo of base (-2) and append it to the empty list list
        val //= -2 # Integer division
    return r_lst # return the list. Also we may type return "".join(str(item) for item in r_lst) to return as a string like '10011'

print(rev([1,1,1,0,0,1,1])) # returns [1, 0, 1, 1, 0, 1]
print(rev([1,0,0,1])) # returns [1, 1, 0, 1, 1]
print(rev([1,1,0,1])) # returns [1, 0, 0, 1, 1]
print(rev([1,1,0,2,1])) # returns "Not a binary" exception
