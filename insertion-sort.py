def insertionSort(arr):
    print('original list: ', end='')
    print(arr)

    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j] :
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

        print(f'{i}th pass: ', end='')
        print(arr)

arr = [1,2,3,4,4,1,12,2]

insertionSort(arr)

print(arr)