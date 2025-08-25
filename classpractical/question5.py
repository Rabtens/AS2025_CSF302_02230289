# Q5: Frequency Count
arr = [1, 2, 3, 2, 4, 1, 2, 5, 3]
freq = {}

for num in arr:
    freq[num] = freq.get(num, 0) + 1

print("Array:", arr)
print("Frequency Count:", freq)
