
def quick_sort(arr, start, end):
    if start >= end:
        return arr[end]
    pivot = arr[end]
    p = start
    for i in range(start, end-1):
        if arr[i] <= pivot:
            arr[i], arr[p] = arr[p], arr[i]
            p += 1
    arr[p], arr[end] = arr[end], arr[p]
    quick_sort(arr, start, p-1)
    quick_sort(arr, p+1, end)

if __name__ == '__main__':
    arr = [2, 3, 1, 5, 4]
    quick_sort(arr, 0, len(arr)-1)
    print(arr)