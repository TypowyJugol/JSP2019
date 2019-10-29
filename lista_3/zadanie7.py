n=int(input("Wprowadź n-ty wyraz ciągu Fibonacciego:"))
def x(n):
    if n < 1:
        return 0
    if n < 2:
        return 1
    return x(n - 1)+x(n - 2)
print(x(n))