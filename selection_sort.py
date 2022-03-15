def selection_sort(arr):
    print('original list: ', end='')
    print(arr)


    for i in range(len(arr)):
        min_index = i
        sub_counter = 0
        for j in range(i+1, len(arr)):
            if arr[j]<arr[min_index]:
                min_index = j
            print(f'{sub_counter + 1}th sub-pass: ', end='')
            print(min_index)
            sub_counter += 1

        arr[i],arr[min_index] = arr[min_index],arr[i]
        print(f'\n{i + 1}th pass: ', end='')
        print(arr)

    print("Sorted, ascending: ", end='')
    print(arr)

# descendingly sort the list
def reverse_selectionSort(arr):
    pass