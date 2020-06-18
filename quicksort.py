from random import randint

def quicksort(array):
    if len(array) < 2:
        return array

    low, same, high = [], [], []

    pivot = array[randint(0, len(array) - 1)]

    print('pivot is', str(pivot))

    for item in array:
        if item < pivot:
            low.append(item)
            print('low', low)
        elif item == pivot:
            same.append(item)
            print('same', same)
        elif item > pivot:
            high.append(item)
            print('high', high)
    return quicksort(low) + same + quicksort(high)


print('full sort list' + str(quicksort([5,3,2,6,8,8,20,9,85,63,0])))
