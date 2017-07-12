# BINARY SEARCH: Complexity: O(log n)

def binary(array, v):
    array.sort()
    low = 1
    high = len(array)
    while low <= high:
        mid = (low+high)//2
        if(array[mid] == v):
            return mid
        if(array[mid] < v):
            low = mid+1
        else:
            high = mid-1
    return


print(binary([4, 7, 2, 8, 3, 9, 1, 0], 7))