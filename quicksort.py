from random import randrange, shuffle

def quicksort(list, start, end):
    if start >= end:
        return
    
    pivot_idx = randrange(start, end + 1)
    pivot_element = list[pivot_idx]
    list[end], list[pivot_idx] = list[pivot_idx], list[end]
    less_than_pointer = start

    for i in range(start, end):
        if list[i] < pivot_element:
            list[i], list[less_than_pointer] = list[less_than_pointer], list[i]
            less_than_pointer += 1

    list[end], list[less_than_pointer] = list[less_than_pointer], list[end]

    quicksort(list, start, less_than_pointer - 1)
    quicksort(list, less_than_pointer + 1, end)

    return list