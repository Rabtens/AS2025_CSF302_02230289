import random

# Q2: Binary Search Algorithm
def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid   # Element found
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1   # Element not found

arr = sorted([random.randint(1, 100) for _ in range(10)])
print("Sorted Array:", arr)
key = int(input("Enter number to search: "))
result = binary_search(arr, key)
if result != -1:
    print(f"Element {key} found at index {result}")
else:
    print(f"Element {key} not found")
