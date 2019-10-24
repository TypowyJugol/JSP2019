
def klucz(y):
    return y[1]

x=[(2, 8),(5, 5),(9, 3),(1, 0),(3, 2),(6, 4),(1, 9),(10, 3),(2, 3),(1, 7)]


x=sorted(x, key=klucz)

print(x)