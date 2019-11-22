x=int(input("podaj x:"))
a=[0,1,2,3,4,5,6]
x2=[]
elementy=[]
def w(x,a):
    for i in range(len(a)-1):
        x2.append(x**(i+1))
    for i in range(len(a)-1):
        elementy.append(a[i+1]*x2[i])
    print(sum(elementy)+a[0])

w(x,a)