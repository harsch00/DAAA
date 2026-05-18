def fib(n):
    if list[n] != -1:
        return list[n]

    list[n] = fib(n - 1) + fib(n - 2)
    return list[n]

while True:
    try:
        n = int(input("Enter n: "))
        break
    except ValueError:
        print("Invalid input! Enter integer only.")

list = [-1]*(n+1)
list[0] = 0
list[1] = 1

print(f"Fibonacci({n}) = {fib(n)}")
