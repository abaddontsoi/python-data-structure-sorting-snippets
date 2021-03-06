def insertionSort(arr):
    print('original list: ', end='')
    print(arr)
    print('')

    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        print(f"Cuttent list: {arr}")
        print(f"key value: {key}")
        print(f"index: {i}")
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j] :
            print(f'{key} < {arr[j]}')
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

        print(f'{i}th pass result: {arr}')

    return arr


def reverse_insertionSort(arr):
    print('original list: ', end='')
    print(arr)
    print('')

    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        print(f"Cuttent list: {arr}")
        print(f"key value: {key}")
        print(f"index: {i}")
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key > arr[j] :
            print(f'{key} > {arr[j]}, list status: {arr}')
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

        print(f'{i}th pass result: {arr}')
        print('')

    return arr
