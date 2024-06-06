def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

# Example usage
arr1 = [1, 2, 3, 4, 5]
arr2 = [5, 4, 3, 2, 1]

print("Is arr1 sorted?", is_sorted(arr1))  # Output: True
print("Is arr2 sorted?", is_sorted(arr2))  # Output: False