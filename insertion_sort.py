"""
 Complexity: O(N^2)
"""

def insertion_sort(array):          #insertion functions starts
    array_length = len(array)       #get the length of array passed
    for i in range(1, array_length):  #for loop starting 1 index
        key = array[i]                #get the key
        j = i - 1
        while j >= 0 and array[j] > key:         #while loop check key and its previous value
            array[j+1], array[j] = array[j], array[j+1]      #swap values
            j = j - 1
        #array[j + 1] = key
    return array                                      #return array

print(insertion_sort([31, 41, 59, 26, 41, 58]))

#insertion in decreasing order
def decreasing_order(array):
    array_length = len(array)
    for i in range(1, array_length):
        key = array[i]
        j = i-1
        while j>=0 and array[j] < key:
            array[j], array[j+1] = array[j+1],array[j]
            j -= 1
    return array

print(decreasing_order([31, 41, 59, 26, 41, 58]))