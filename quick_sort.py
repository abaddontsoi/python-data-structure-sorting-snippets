depth_counter = 0

def partition(arr, left, right, parti_record: list):
    pivot_value = arr[left]

    i_pointer = left
    print('list current status: ', end='')
    print(arr)

    for j in range(left+1, right+1):
        if arr[j]<pivot_value:
            i_pointer += 1
            arr[i_pointer], arr[j] = arr[j], arr[i_pointer]
    
    arr[i_pointer], arr[left] = arr[left], arr[i_pointer]

    parti_record.append(arr[left:right+1])
    return i_pointer

def quick_sort(arr,left,right, parti_record:list, message=""):
    global depth_counter

    if len(arr)==1:
        print(arr[left: right])
        return arr

    if left<right:

        print("\n"+message)
        pivot_index = partition(arr,left,right, parti_record)
        print(f'pivot is in index: {pivot_index}')
        # print(arr[left:right+1])
        print(arr[left:pivot_index], end=' ')
        print(arr[pivot_index], end=' ')
        print(arr[pivot_index + 1:right+1])
        
        depth_counter += 1
        quick_sort(arr, left, pivot_index - 1, parti_record, f"left side, in depth {depth_counter}")
        
        quick_sort(arr, pivot_index + 1, right, parti_record, f"right side, in depth {depth_counter}")
        # quick_sort(arr, left, pivot_index - 1, parti_record)
        # quick_sort(arr, pivot_index + 1, right, parti_record)
        depth_counter-=1
