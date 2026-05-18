def count_digits(n):
    if n == 0:
        return 1

    count = 0
    while n != 0:
        count += 1
        n //= 10
    return count

def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y

    n = count_digits(x)
    n_y = count_digits(y)
    if n_y > n:
        n = n_y

    half = n//2
    base = 10**half

    a = x//base
    b = x%base
    c = y//base
    d = y%base

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_bc = karatsuba(a + b, c + d) - ac - bd

    return ac*(10**n) + ad_bc*base + bd

while True:
    try:
        x, y = input("Enter the two numbers: ").split()
        x = int(x)
        y = int(y)

        if x < 0 or y < 0:
            print("Pls enter only non-negative numbers!")
            continue
        else:
            break

    except ValueError:
        print("Pls enter exactly two integers!")

print(karatsuba(x, y))
