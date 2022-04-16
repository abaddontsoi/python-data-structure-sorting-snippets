depth_counter = 0

def merge(arr, left, middle, right):
    print(f"Current list status: {arr}")

    n1 = middle - left + 1
    n2 = right - middle

    L = arr[left:middle+1] # have first m elements
    R = arr[middle+1:right+1] # starts from no. m element

    # print(f"Ltest: {Ltest} VS L: {L}")
    # print(f"Rtest: {Rtest} VS R: {R}")

    # Merge the temp arrays back into arr[l..r]
    i_pointer = 0     # Initial index of first subarray
    j_pointer = 0     # Initial index of second subarray
    k = left     # Initial index of merged subarray

    while i_pointer < n1 and j_pointer < n2:
        if L[i_pointer] < R[j_pointer]:
            print(f"{L[i_pointer]} < {R[j_pointer]}")
            print(f"{L[i_pointer]} inserted into index {k} of {arr}")
            # print(f"")
            arr[k] = L[i_pointer]
            i_pointer += 1
        else:
            print(f"{L[i_pointer]} > {R[j_pointer]}")
            print(f"{R[j_pointer]} inserted into index {k} of {arr}")
            arr[k] = R[j_pointer]
            j_pointer += 1
        k += 1
 
    # Copy the remaining elements of L[], if there
    # are any
    while i_pointer < n1:
        print(f"{L[i_pointer]} inserted into index {k} of {arr}")
        arr[k] = L[i_pointer]
        i_pointer += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j_pointer < n2:
        print(f"{R[j_pointer]} inserted into index {k} of {arr}")
        arr[k] = R[j_pointer]
        j_pointer += 1
        k += 1


def reverseMerge(arr, left, middle, right):
    print(f"Current list status: {arr}")

    n1 = middle - left + 1
    n2 = right - middle

    L = arr[left:middle+1] # have first m elements
    R = arr[middle+1:right+1] # starts from no. m element

    # print(f"Ltest: {Ltest} VS L: {L}")
    # print(f"Rtest: {Rtest} VS R: {R}")

    # Merge the temp arrays back into arr[l..r]
    i_pointer = 0     # Initial index of first subarray
    j_pointer = 0     # Initial index of second subarray
    k = left     # Initial index of merged subarray

    while i_pointer < n1 and j_pointer < n2:
        if L[i_pointer] > R[j_pointer]:
            print(f"{L[i_pointer]} > {R[j_pointer]}")
            print(f"{L[i_pointer]} inserted into index {k} of {arr}")
            arr[k] = L[i_pointer]
            i_pointer += 1
        else:
            print(f"{L[i_pointer]} < {R[j_pointer]}")
            print(f"{R[j_pointer]} inserted into index {k} of {arr}")
            arr[k] = R[j_pointer]
            j_pointer += 1
        k += 1
 
    # Copy the remaining elements of L[], if there
    # are any
    while i_pointer < n1:
        print(f"{L[i_pointer]} inserted into index {k} of {arr}")
        arr[k] = L[i_pointer]
        i_pointer += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j_pointer < n2:
        print(f"{R[i_pointer]} inserted into index {k} of {arr}")
        arr[k] = R[j_pointer]
        j_pointer += 1
        k += 1
    

def mergeSort(arr, left, right, message="", mode="normal"):
    global depth_counter

    if left < right:
        print("\n"+message)
        if mode=="normal":
            
            # Same as (l+r)//2, but avoids overflow for
            # large l and h
            middle = left+(right-left)//2
            print(arr[left:middle+1], end=' ')
            print(arr[middle + 1:right+1])

            # going to next level
            depth_counter += 1
            # Sort first and second halves
            mergeSort(arr, left, middle, f"left side, in depth {depth_counter}", )
            mergeSort(arr, middle+1, right, f"right side, in depth {depth_counter}", )
            merge(arr, left, middle, right)

            # return to previous level
            depth_counter -= 1

            print(f"Array is: {arr}")

        if mode=="reverse":
            # Same as (l+r)//2, but avoids overflow for
            # large l and h
            middle = left+(right-left)//2
            print(arr[left:middle+1], end=' ')
            print(arr[middle + 1:right+1])

            # going to next level
            depth_counter += 1

            # Sort first and second halves
            mergeSort(arr, left, middle, f"left side, in depth {depth_counter}", "reverse")
            mergeSort(arr, middle+1, right, f"right side, in depth {depth_counter}", "reverse")

            reverseMerge(arr, left, middle, right)

            # return to previous level
            depth_counter -= 1

            print(f"Array is: {arr}")

    return arr
