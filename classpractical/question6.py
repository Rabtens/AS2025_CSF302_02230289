# Q6: Second Largest Element
arr = [10, 20, 4, 45, 99, 99]
unique_arr = list(set(arr))  # Remove duplicates
unique_arr.sort()
print("Array:", arr)
print("Second Largest:", unique_arr[-2])
