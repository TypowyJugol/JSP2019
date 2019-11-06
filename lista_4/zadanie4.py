n = int(input("Wprowadź n:"))
a = int(input("Wprowadź pierwszy wyraz:"))
q = int(input("Wprowadź q:"))

def ciąg(q, n, a):
    return a * q**(n-1)

print("Wyraz na n-tym miejscu to: ", ciag(q, n, a))