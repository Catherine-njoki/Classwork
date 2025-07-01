def binary_search(arr, key_value) -> int:
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        mid_val = arr[mid]
        if mid_val == key_value:
            return mid
        elif key_value < mid_val:
            end = mid - 1
        else:  # key_value > mid_val
            start = mid + 1
    return -1

#that was iterative

#for recursive is below
def recursive_binary_search(arr, target, start_index, end_index):
    if start_index > end_index:
        return -1
    mid = (start_index + end_index) // 2
    mid_val = arr[mid]
    if mid_val == target:
        return mid
    elif mid_val < target:
        return recursive_binary_search(arr, target, mid + 1, end_index)
    else:
        return recursive_binary_search(arr, target, start_index, mid - 1)



#testing testing
sorted_numbers = [11, 22, 33, 44, 55, 66, 77, 88, 99]
key = 88

# Iterative
index_found = binary_search(sorted_numbers, key)

if index_found != -1:
    print(f"Iterative Binary Search: Target {key} found at index {index_found}")
else:
    print("Iterative Binary Search: Target Not Found")

# Recursive
recursive_index = recursive_binary_search(sorted_numbers, key, 0, len(sorted_numbers) - 1)

if recursive_index != -1:
    print(f"Recursive Binary Search: Target {key} found at index {recursive_index}")
else:
    print("Recursive Binary Search: Target Not Found")

