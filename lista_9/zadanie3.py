import matplotlib.pyplot as plt
import numpy

v0 = int(input("Podaj prędkość początkową w m/s: "))
kat = int(input("Podaj kąt rzutu w stopniach: "))
g = float(9.81)

sin_kat = numpy.sin(kat*numpy.pi/180)
cos_kat = numpy.cos(kat*numpy.pi/180)
t_maks_wys = (v0 * sin_kat)/g
maks_wys = v0 * t_maks_wys * sin_kat - (g*t_maks_wys**2)/2
zasieg = v0 * 2*t_maks_wys * cos_kat
vx = []
vy = []
x = []
y = []
t = numpy.arange(0,2*t_maks_wys,0.01)
for i in t:
    vy.append(v0 * sin_kat - g*i)
    vx.append(v0 * cos_kat)
    x.append(v0 * cos_kat * i)
    y.append(v0 * i * sin_kat - (g*i**2)/2)

print("Czas lotu to: " + str(2*t_maks_wys))
print("Maksymalna wysokość w to: " + str(maks_wys) + "[m]")
print("Zasięg rzutu to: " + str(zasieg) + "[m]")
fig, axs = plt.subplots(1, 3)
axs[0].plot(t, vx)
axs[0].set_title("vx(t)")
axs[0].set_xlabel("t[s]")
axs[0].set_ylabel("vx[m/s]")
axs[1].plot(t, vy)
axs[1].set_title("vy(t)")
axs[1].set_xlabel("t[s]")
axs[1].set_ylabel("vy[m/s]")
axs[2].plot(x, y)
axs[2].set_title("y(x)")
axs[2].set_xlabel("x[m]")
axs[2].set_ylabel("y[m]")
plt.show()
