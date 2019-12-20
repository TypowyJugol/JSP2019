import matplotlib.pyplot as plt
import numpy
jezyk = ['Java', 'C', 'Python', 'C++', 'C#', 'Visual Basic .NET', 'JavaScript', 'PHP',
         'SQL', 'Swift']
popularnosc = [17.253, 16.086, 10.308, 6.196, 4.801, 4.743, 2.090, 2.048, 1.843, 1.490]
kolor = ["red" , "blue", "green", "purple", "brown", "pink", "black", "yellow", "gray", "orange"]
plt.bar(jezyk, popularnosc, color=kolor)
plt.title("Popularność języków programowania wg. Tiobe")
plt.ylabel("Popularność [%]")
x=[1,2,3,4,5,6,7,8,9,10]
for i in range(len(jezyk)):
    plt.annotate(str(popularnosc[i]), xy=(jezyk[i],popularnosc[i]))

plt.show()
