
import math


#zadanie1

a=int(input("wprowadz piersza liczbe"))
b=int(input("wprowadz druga liczbe"))
c=a%b
print(c)

#zadanie2
x=float(input("wprowadz pierwszy bok"))
y=float(input("wprowadz drugi bok"))
z=float(input("wprowadz trzeci bok"))

h=(x*x-y*y-z*z)/(-2*y*z)
cosin=(math.acos(h))

cosinstopnie=cosin*(180/math.pi)
print(cosinstopnie)