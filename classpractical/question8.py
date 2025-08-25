import random

# Q8: Array with Duplicates
arr = [random.randint(1, 10) for _ in range(20)]  # Random numbers with duplicates
print("Array:", arr)

# A) Total number of duplicate elements
duplicates = len(arr) - len(set(arr))
print("Total number of duplicate elements:", duplicates)

# B) Most repeating element
freq = {}
for num in arr:
    freq[num] = freq.get(num, 0) + 1

most_repeating = max(freq, key=freq.get)
print("Most Repeating Element:", most_repeating, "appears", freq[most_repeating], "times")
