def binary_search(arr, target):  # Works on sorted lists
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Don’t forget this return in case not found!

arr = [2, 3, 5, 7, 8, 10]
target = 8
result = binary_search(arr, target)
#hh
if result != -1:
    print(f"Binary Search result: Found at index {result}")
else:
    print("Binary Search result: Not found")
#gg