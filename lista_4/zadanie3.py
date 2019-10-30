import math
rs=int(input("Chcesz otrzymać radiany(0) czy stopnie(1)?:"))
if rs==0:
    stopnie=float(input("Podaj kąt w stopniach:"))
    print(stopnie*math.pi/180)
else:
    radiany=float(input("Podaj kąt w radianach:"))
    print(radiany*180/math.pi)