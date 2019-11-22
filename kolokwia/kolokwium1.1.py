list=[2,(17,-8),6,"Ala","Python",-4.0,"Ela"]
ints=[]
strings=[]
tuples=[]
floats=[]
list2=[]
intsf=[]
strings2=[]
for i in range(len(list)):
    if type(list[i])==int:
        list2.append(list[i])
    elif type(list[i])==str:
        list2.append(list[i])
    elif type(list[i])==tuple:
        x=list[i]
    else:
        list2.append(list[i])

for i in range(len(x)):
    tuples.append(x[i])

for i in range(len(tuples)):
    list2.append(tuples[i])


for i in range(len(list2)):
    if type(list2[i])==int:
        intsf.append(float(list2[i]))
    if type(list2[i])==float:
        intsf.append(list2[i])
    if type(list2[i])==str:
        strings2.append(list2[i])

print(min(intsf))
print(max(strings2, key=len))

