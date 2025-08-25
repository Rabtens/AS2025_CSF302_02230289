# Q7: Linear Search Algorithm
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

arr = [10, 25, 30, 45, 50]
key = int(input("Enter number to search: "))
result = linear_search(arr, key)
if result != -1:
    print(f"Element {key} found at index {result}")
else:
    print(f"Element {key} not found")
