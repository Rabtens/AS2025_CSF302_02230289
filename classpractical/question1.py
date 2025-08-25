import random

# Q1: Store random numbers and find smallest and largest
n = int(input("Enter number of elements: "))
arr = [random.randint(1, 100) for _ in range(n)]  # Generate n random numbers between 1 and 100

print("Array:", arr)
print("Smallest Number:", min(arr))
print("Largest Number:", max(arr))
