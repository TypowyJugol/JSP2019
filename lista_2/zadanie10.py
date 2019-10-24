
x=[]

for i in range (33):
    x.append(3*i)

del x[4:33:3]

print(sum(x)/len(x))