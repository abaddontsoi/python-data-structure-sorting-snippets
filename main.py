import argparse

import bubble_sort, merge_sort, quick_sort, selection_sort, insertion_sort

parser = argparse.ArgumentParser()

parser.add_argument('-b', '--bubble-sort', help='This is bubble sort', nargs='*')
parser.add_argument('-m', '--merge-sort', help='This is merge sort', nargs='*')
parser.add_argument('-q', '--quick-sort', help='This is quick sort', nargs='*')
parser.add_argument('-s', '--selection-sort', help='This is selection sort', nargs='*')
parser.add_argument('-i', '--insertion-sort', help='This is insertion sort', nargs='*')

args = parser.parse_args()

if args.bubble_sort:
    print('\nBubble sort')
    unsorted_list = [int(i) for i in args.bubble_sort]
    bubble_sort.bubble_sort(args.bubble_sort)

if args.merge_sort:
    print("\nMerge_sort")
    unsorted_list = [int(i) for i in args.merge_sort]
    merge_sort.merge_sort(args.merge_sort, 0, len(args.merge_sort))

if args.quick_sort:
    print("\nQuick sort")
    parti_record = []
    unsorted_list = [int(i) for i in args.quick_sort]
    quick_sort.quick_sort(unsorted_list, 0, len(unsorted_list)-1, 
        parti_record, f"original list {unsorted_list}")

if args.selection_sort:
    print('\nSelection sort')
    unsorted_list = [int(i) for i in args.selection_sort]
    selection_sort.selection_sort(args.selection_sort)

if args.insertion_sort:
    print('\nInsertion sort')
    unsorted_list = [int(i) for i in args.insertion_sort]
    insertion_sort.insertionSort(args.insertion_sort)