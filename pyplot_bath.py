import matplotlib.pyplot as plt
labels = ["A", "B", "C", "D", "E"]
y_pos = range(0, 5)
v = [91, 45, 17, 88, 47]
plt.barh(y_pos, v, tick_label = labels)
plt.show()