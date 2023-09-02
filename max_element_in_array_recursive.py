def find_max(array):

    # base case
    if len(array) == 1:
        return array[0]
    
    # recursive case
    array[-2] = (array[-1] if array[-1]>array[-2] else array[-2])
    del array[-1]
    return find_max(array)
    # [3,5]

print(find_max([10,3,45,1,6,32]))
# [10,3,45,1,6,32]