import matplotlib.pyplot as plt
steps = [6000, 7000, 8000, 9000, 10000, 12000, 13000]
labels = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
num_bars = len(steps)
positions = range(1, num_bars+1)
plt.bar(positions, steps, align='center')
plt.xticks(positions, labels)
plt.xlabel('Steps')
plt.ylabel('Day')
plt.title('Number of steps walked')
plt.grid()
plt.show()
