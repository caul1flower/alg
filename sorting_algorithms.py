def selection_sort(arr):
    comparisons = 1
    for i in range(len(arr)):
        comparisons += 1
        min_idx = i
        comparisons += 1
        for j in range(i + 1, len(arr)):
            comparisons += 2
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return comparisons


def insertion_sort(arr):
    comparisons = 1
    for i in range(1, len(arr)):
        comparisons += 1
        key = arr[i]
        j = i - 1
        comparisons += 1
        while j >= 0 and key < arr[j]:
            comparisons += 2
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return comparisons


def merge_sort(lst):
    comparisons = 0
    if len(lst) > 1:
        middle = len(lst) // 2
        left = lst[:middle]
        right = lst[middle:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1
            comparisons += 1
        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1
    return comparisons


def shell_sort(lst):
    length = len(lst)
    h = 1
    comparisons = 0
    while (h < (length//3)):
        h = 3*h + 1
    while (h >= 1):
        for i in range(h, length):
            for j in range(i, h-1, -h):
                comparisons += 1
                if (lst[j] < lst[j-h]):
                    lst[j], lst[j-h] = lst[j-h], lst[j]
                else:
                    break

        h = h//3
    return comparisons
