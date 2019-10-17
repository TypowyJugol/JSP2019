import cmath

z = 2j
print(cmath.sin(z))
print("Część rzeczywista sin(z): ", cmath.sin(z.real))
print("Część urojona sin(z): ", cmath.sin(z.imag))
print("Część rzeczywista cos(z)", cmath.cos(z.real))
print("Część urojona cos(z)", cmath.cos(z.imag))
x=(cmath.cos(z)**2 + cmath.sin(z)**2)
if x==1:
    print("zależność spełniona")
else:
    print("zależność niespełniona")