# bubble sort: Complexity O(N^2)

def bubblesort(array):
    n = len(array)

    # Tranverse through all array element
    for i in range(n):

        # Last i elements are already place
        for j in range(0, n - i - 1):

            # tranverse the array from 0 to n-i-1
            # swap if elements found is greater than next elements
            if (array[j] > array[j + 1]):
                array[j], array[j + 1] = array[j + 1], array[j]


array = [64, 34, 25, 12, 22, 11, 90]
bubblesort(array)
print(array)
