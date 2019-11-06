n = int(input("Wprowadź wartość n elementów szeregu: "))

x = 0

for i in range (1, n+1):
    x = x + 1/i

print("Suma elementow n=",n," pierwszych szeregu harmonicznego to:",x,sep="")