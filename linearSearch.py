def linear_Search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


arr = [10, 3, 7, 8, 2, 5]
target = 8
result = linear_Search(arr, target)

if result != -1:
    print(f"Linear Search Result: Found at index {result}")
else:
    print("Linear Search Result: Not found")
