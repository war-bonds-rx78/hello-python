import matplotlib.pyplot as plt
import math

x = range(0, 360)
y = [math.sin(math.radians(d)) for d in x ]
c = [math.cos(math.radians(d)) for d in x ]
plt.plot(x, y)
plt.plot(x, c)
plt.show()