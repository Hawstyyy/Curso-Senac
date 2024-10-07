import matplotlib.pyplot as plt


# plt.plot((1,2,3,4,5,6),(1,2,3,4,5,6), 'mo')
# plt.xlabel('eixo x')
# plt.ylabel('eixo y')
# plt.title('Título massa')
# plt.grid(True)

# a = (altura)
# b = (peso)

# plt.scatter(b,a)

# a = (1,2,3,4,5,6)
# b = (2,4,6,8,10,12)

# plt.bar(a,b)

a = (10,20,30)
explode = (0.1,0,0)
labels = ["HB20", "Gol", "Fusca"]
plt.pie(a, explode=explode, labels=labels, autopct='%.2f%%', shadow=True)

plt.show()