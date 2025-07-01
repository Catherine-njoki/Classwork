def recursive_bubble_sort(arr, n=None):
    if n is None:
        n = len(arr)

    if n == 1:
        return arr  # Base case: only 1 item, so it's sorted

    # Perform one pass of bubble sort
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

    # Recursive call on the reduced array
    return recursive_bubble_sort(arr, n - 1)
#hh