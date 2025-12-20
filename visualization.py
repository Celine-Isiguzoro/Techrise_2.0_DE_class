import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 4, 6, 7]) # x axis
ypoints = np.array([3, 8, 1, 10]) # y axis


# plt.plot(xpoints, marker = "d", ls = ":", color = "#34159a", ms = 5, mec = "k",mfc = "b", lw = 1,)
# plt.plot(ypoints, marker = "o", ls= ":", color = "#065C53", ms = 5, mec = "k", mfc = "hotpink", lw = 1) # use of markers and linestyle(format is marker, line, color)
# plt.show() # To show the graph

x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

# plt.plot(x1, y1, x2, y2)
font1 = {'family': 'Times New Roman','color': 'green', 'size': '16'}
font2 = {'family': 'Times New Roman','color': 'blue', 'size': '24'}
plt.xlabel("x-axis", fontdict= font1)
plt.ylabel("y-axis", fontdict= font1)
# plt.title("A Graph of X against Y", fontdict= font2, loc= 'left')

# plt.plot(xpoints, ypoints) # To plot the graph
# plt.grid(axis = 'y') # To add gridlines
# plt.grid(color = 'blue', linestyle = '--', linewidth = 0.5) # Grid properties
# plt.subplot(2,1,1)
# plt.scatter(xpoints, ypoints) # scatter chart
# plt.bar(xpoints, ypoints, width=0.2) # Bar chart
plt.hist(xpoints) # Histogram
# plt.title("Chart displaying the distribution of fruits", fontdict= font2)

# plt.pie(y2, labels= ['apple', 'banana','cherry', 'udara'], startangle= 90)
# plt.show()

# Assignment

# Generate 10 arbitrary heights
heights = np.random.uniform(low=0.1, high=10.0, size=10)

# X positions
x = np.arange(len(heights))

# Random colors for bars 2–10
random_colors = np.random.rand(9, 3)    # 9 RGB colors

# First bar = permanent black
colors = [(0, 0, 0)] + list(random_colors)

fig, ax = plt.subplots(figsize=(10, 5))

# Draw bars with black edge
bars = ax.bar(x, heights, color=colors, edgecolor='black', linewidth=1.3)

# Optional: height labels
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height:.2f}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 5),
                textcoords="offset points",
                ha='center', va='bottom', fontsize=9)

# Clean formatting
ax.set_xticks(x)
ax.set_xticklabels([f'Bar {i+1}' for i in x])
ax.set_ylabel('Height')
ax.set_title('Histogram: First Bar Black, Others Random')

plt.tight_layout()
plt.show()