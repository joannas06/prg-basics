import matplotlib.pyplot as plt

x = []
y = []

# create x values
for n in range(-100,101):
   x = x + [n]

# create y values
for n in x:
   val = (n**2)-3
   y.append(val)

# print chart
plt.plot(x,y)
plt.show()
