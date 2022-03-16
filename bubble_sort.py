def bubble_sort(our_list):
    print('original list: ', end='')
    print(our_list)
    print('')


    # We go through the list as many times as there are elements
    for i in range(len(our_list)):
        # We want the last pair of adjacent elements to be (n-2, n-1)
        for j in range(len(our_list) - 1):
            
            # print(our_list[0:j], end=' ')
            # print(our_list[j:j+2], end=' ')
            # print(our_list[j+2:])

            print(f"current bubble: ",end='')
            if our_list[j] > our_list[j+1]:
                # Swap
                print(f'at index {j} and {j+1} \nvalue {our_list[j]}, { our_list[j+1] } swapped')
                our_list[j], our_list[j+1] = our_list[j+1], our_list[j]
            else:
                print(f'at index {j} and {j+1} \nvalue {our_list[j]}, { our_list[j+1] } not swapped')
            
            print(our_list[0:j], end=' ')
            print(our_list[j:j+2], end=' ')
            print(our_list[j+2:])
            # print('')

        print(f"{i+1}th pass result: ", end='')
        print(our_list)
        print('')

def reverse_bubbleSort(our_list):

    print('original list: ', end='')
    print(our_list)
    print('')


    # We go through the list as many times as there are elements
    for i in range(len(our_list)):
        # We want the last pair of adjacent elements to be (n-2, n-1)
        for j in range(len(our_list) - 1):
            
            # print(our_list[0:j], end=' ')
            # print(our_list[j:j+2], end=' ')
            # print(our_list[j+2:])

            print(f"current bubble: ",end='')
            if our_list[j] < our_list[j+1]:
                # Swap
                print(f'at index {j} and {j+1} \nvalue {our_list[j]}, { our_list[j+1] } swapped')
                our_list[j], our_list[j+1] = our_list[j+1], our_list[j]
            else:
                print(f'at index {j} and {j+1} \nvalue {our_list[j]}, { our_list[j+1] } not swapped')
            
            print(our_list[0:j], end=' ')
            print(our_list[j:j+2], end=' ')
            print(our_list[j+2:])
            # print('')

        print(f"{i+1}th pass result: ", end='')
        print(our_list)
        print('')
