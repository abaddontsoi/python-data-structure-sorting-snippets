def selection_sort(arr):
    print('original list: ', end='')
    print(arr)


    for i in range(len(arr)):
        min_index = i
        sub_counter = 0
        for j in range(i+1, len(arr)):
            print(f'{sub_counter}th sub-pass: \nCurrent min_index {min_index}', end='\t')
            print(f"comparing: {arr[min_index]}, {arr[j]}")
            if arr[j]<arr[min_index]:
                print(f"{arr[j]} < {arr[min_index]}", end='\t')
                min_index = j
                print(f"Updated min_index to {min_index}")
            sub_counter += 1

        print(arr)
        print(f"Swap index {i} and {min_index}")
        arr[i],arr[min_index] = arr[min_index],arr[i]
        print(f'\n{i + 1}th pass: ', end='')
        print(arr)

    print("Sorted, ascending: ", end='')
    print(arr)

# descendingly sort the list
def reverse_selectionSort(arr):
    print('original list: ', end='')
    print(arr)


    for i in range(len(arr)):
        max_index = i
        sub_counter = 0
        for j in range(i+1, len(arr)):
            print(f'{sub_counter }th sub-pass: \nMax index is {max_index}', end='\t')
            print(f"comparing: {arr[max_index]}, {arr[j]}")
            if arr[j]>arr[max_index]:
                print(f"{arr[j]} > {arr[max_index]}", end='\t')
                max_index = j
                print(f"Updated max_index to {max_index}")
            sub_counter += 1

        print(arr)
        print(f"Swap index {i} and {max_index}")
        arr[i],arr[max_index] = arr[max_index],arr[i]
        print(f'\n{i + 1}th pass: ', end='')
        print(arr)

    print("Sorted, descending: ", end='')
    print(arr)