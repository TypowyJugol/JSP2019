parzyste=[]
for a in range(100, 401):
    x=True
    for b in str(a):
        if int(b)%2==1:
            x=False
    if (x):
        parzyste.append(a)

print(parzyste)