import time
# Iteracyjnie

n = int(input("Podaj liczbę: "))

def fib_i(n):
    a = 0
    b = 1
    for i in range(n-1):
        b += a
        a = b - a
    return (b)


# Rekurencyjnie
def fib_rek(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib_rek(n - 1) + fib_rek(n - 2)




start = time.time()
print("Iteracyjnie: " + str(fib_i(n)))
stop = time.time()
print("Czas: " + str(stop-start))
start = time.time()
print("Rekurencyjnie: " + str(fib_rek(n+1)))
stop = time.time()
print("Czas: " + str(stop-start))