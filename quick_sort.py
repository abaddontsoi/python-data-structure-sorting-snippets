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

def reverse_partition(arr, left, right, parti_record: list):
    pivot_value = arr[left]

    i_pointer = left
    print('list current status: ', end='')
    print(arr)

    for j in range(left+1, right+1):
        if arr[j]>pivot_value:
            i_pointer += 1
            arr[i_pointer], arr[j] = arr[j], arr[i_pointer]
    
    arr[i_pointer], arr[left] = arr[left], arr[i_pointer]

    parti_record.append(arr[left:right+1])
    return i_pointer

def quick_sort(arr,left,right, parti_record:list, message="", mode='normal'):
    global depth_counter

    if len(arr)==1:
        print(arr[left: right])
        return arr

    if left<right and mode == 'normal':

        print("\n"+message)
        pivot_index = partition(arr,left,right, parti_record)
        print(f'pivot is in index: {pivot_index}')
        # print(arr[left:right+1])
        print(arr[left:pivot_index], end=' ')
        print(arr[pivot_index], end=' ')
        print(arr[pivot_index + 1:right+1])
        
        # add 1 because it is going to next level
        depth_counter += 1
        quick_sort(arr, left, pivot_index - 1, parti_record, f"left side, in depth {depth_counter}", 'normal')
        
        quick_sort(arr, pivot_index + 1, right, parti_record, f"right side, in depth {depth_counter}", 'normal')
        # quick_sort(arr, left, pivot_index - 1, parti_record)
        # quick_sort(arr, pivot_index + 1, right, parti_record)

        # subtract 1 beacuse is returning to previous level
        depth_counter-=1

    if left<right and mode == 'reverse':
    
        print("\n"+message)
        pivot_index = reverse_partition(arr,left,right, parti_record)
        print(f'pivot is in index: {pivot_index}')
        # print(arr[left:right+1])
        print(arr[left:pivot_index], end=' ')
        print(arr[pivot_index], end=' ')
        print(arr[pivot_index + 1:right+1])
        
        # add 1 because it is going to next level
        depth_counter += 1
        quick_sort(arr, left, pivot_index - 1, parti_record, f"left side, in depth {depth_counter}", 'reverse')
        
        quick_sort(arr, pivot_index + 1, right, parti_record, f"right side, in depth {depth_counter}", 'reverse')
        # quick_sort(arr, left, pivot_index - 1, parti_record)
        # quick_sort(arr, pivot_index + 1, right, parti_record)

        # subtract 1 beacuse is returning to previous level
        depth_counter-=1
