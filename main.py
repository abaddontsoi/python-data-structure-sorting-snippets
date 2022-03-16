import argparse

import bubble_sort, merge_sort, quick_sort, selection_sort, insertion_sort

parser = argparse.ArgumentParser()

parser.add_argument('-b', '--bubble-sort', help='This is bubble sort', nargs='*')
parser.add_argument('-m', '--merge-sort', help='This is merge sort', nargs='*')
parser.add_argument('-q', '--quick-sort', help='This is quick sort', nargs='*')
parser.add_argument('-s', '--selection-sort', help='This is selection sort', nargs='*')
parser.add_argument('-i', '--insertion-sort', help='This is insertion sort', nargs='*')

parser.add_argument('-r', '--reverse', help='Reverse sorting(descending)', action='store_true')

args = parser.parse_args()

if args.bubble_sort:
    if args.reverse:
        print('\nReverse bubble sort')
        unsorted_list = [int(i) for i in args.bubble_sort]
        sorted_list = bubble_sort.reverse_bubbleSort(unsorted_list)
        pass
    else:
        print('\nBubble sort')
        unsorted_list = [int(i) for i in args.bubble_sort]
        sorted_list = bubble_sort.bubble_sort(unsorted_list)
        pass

if args.merge_sort:
    if args.reverse:
        print("\nReverse merge_sort")
        unsorted_list = [int(i) for i in args.merge_sort]
        sorted_list = merge_sort.mergeSort(unsorted_list, 0, len(unsorted_list)-1, f"original list {unsorted_list}", "reverse")
        pass
    else:    
        print("\nMerge_sort")
        unsorted_list = [int(i) for i in args.merge_sort]
        sorted_list = merge_sort.mergeSort(unsorted_list, 0, len(unsorted_list)-1, f"original list {unsorted_list}",)
        pass

if args.quick_sort:
    if args.reverse:
        print("\nQuick sort")
        parti_record = []
        unsorted_list = [int(i) for i in args.quick_sort]
        sorted_list = quick_sort.quick_sort(unsorted_list, 0, len(unsorted_list)-1, 
            parti_record, f"original list {unsorted_list}", 'reverse')
        pass
    else:
        print("\nQuick sort")
        parti_record = []
        unsorted_list = [int(i) for i in args.quick_sort]
        sorted_list = quick_sort.quick_sort(unsorted_list, 0, len(unsorted_list)-1, 
            parti_record, f"original list {unsorted_list}")
        pass

if args.selection_sort:
    if args.reverse:
        print('\nReverse selection sort')
        unsorted_list = [int(i) for i in args.selection_sort]
        sorted_list = selection_sort.reverse_selectionSort(unsorted_list)
        pass
    else: 
        print('\nSelection sort')
        unsorted_list = [int(i) for i in args.selection_sort]
        sorted_list = selection_sort.selection_sort(unsorted_list)
        pass

if args.insertion_sort:
    if args.reverse:
        print('\nInsertion sort')
        unsorted_list = [int(i) for i in args.insertion_sort]
        sorted_list = insertion_sort.reverse_insertionSort(unsorted_list)
        pass
    else:
        print('\nInsertion sort')
        unsorted_list = [int(i) for i in args.insertion_sort]
        sorted_list = insertion_sort.insertionSort(unsorted_list)


print(f"\nFinal sorted list: {sorted_list}")
