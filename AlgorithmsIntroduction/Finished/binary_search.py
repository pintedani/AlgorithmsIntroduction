def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  # Target found at index mid
        elif arr[mid] < target:
            low = mid + 1  # Search in the right half
        else:
            high = mid - 1  # Search in the left half
    return -1  # Target not found

# Example usage
sorted_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 11
result = binary_search(sorted_list, target)
if result != -1:
    print(f"Target {target} found at index {result}.")
else:
    print(f"Target {target} not found in the list.")
    
# Target 11 found at index 5.