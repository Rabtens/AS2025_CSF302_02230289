# Q4: Fibonacci Sequence
def fibonacci(n):
    a, b = 0, 1
    seq = []
    for _ in range(n):
        seq.append(a)
        a, b = b, a+b
    return seq

n = int(input("Enter number of terms for Fibonacci: "))
print("Fibonacci Sequence:", fibonacci(n))
