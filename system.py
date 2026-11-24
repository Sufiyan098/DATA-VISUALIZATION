import numpy as np
import matplotlib.pyplot as plt

plt.style.use("dark_background")

# ==================================
# DATA
# ==================================

days = np.arange(1, 11)

stock_price = np.array([
    420, 435, 450, 470, 460,
    490, 510, 530, 545, 560
])

volume = np.array([
    100000, 120000, 150000,
    180000, 200000,
    240000, 260000,
    280000, 300000,
    350000
])

sentiment = np.array([
    50, 55, 60, 65, 70,
    75, 80, 82, 88, 95
])

marketing = np.array([
    20, 25, 30, 32, 35,
    40, 45, 50, 55, 60
])

returns = np.array([
    1.2, 2.3, 1.8, -1.1,
    3.5, 2.0, 1.5, 2.7,
    3.1, 2.9
])
# ==================================
# FIGURE
# ==================================

fig = plt.figure(figsize=(16,10))
# ==================================
# 1. 3D SCATTER
# ==================================

ax1 = fig.add_subplot(
    221,
    projection="3d"
)

scatter = ax1.scatter(
    stock_price,
    volume,
    sentiment,
    c=sentiment,
    cmap="viridis",
    s=200
)

ax1.set_title(
    "Stock Price vs Volume vs Sentiment"
)

ax1.set_xlabel("Price")
ax1.set_ylabel("Volume")
ax1.set_zlabel("Sentiment")
# ==================================
# 2. MARKETING VS PRICE
# ==================================

ax2 = fig.add_subplot(222)

ax2.scatter(
    marketing,
    stock_price,
    color="cyan",
    s=150
)

for i in range(len(days)):
    ax2.annotate(
        f"Day {days[i]}",
        (marketing[i], stock_price[i])
    )

ax2.set_title(
    "Marketing Spend vs Stock Price"
)

ax2.set_xlabel(
    "Marketing Budget"
)

ax2.set_ylabel(
    "Stock Price"
)
# ==================================
# 3. HORIZONTAL HISTOGRAM
# ==================================

ax3 = fig.add_subplot(223)

ax3.hist(
    returns,
    bins=5,
    orientation="horizontal",
    color="orange",
    edgecolor="white"
)

ax3.set_title(
    "Distribution of Daily Returns"
)

ax3.set_xlabel(
    "Frequency"
)

ax3.set_ylabel(
    "Daily Return %"
)
# ==================================
# 4. HEATMAP
# ==================================

ax4 = fig.add_subplot(224)

data = np.array([
    stock_price,
    volume/10000,
    sentiment,
    marketing
])

heat = ax4.imshow(
    data,
    cmap="hot",
    aspect="auto"
)

ax4.set_title(
    "Business Metrics Heatmap"
)

ax4.set_yticks(
    [0,1,2,3]
)

ax4.set_yticklabels([
    "Price",
    "Volume",
    "Sentiment",
    "Marketing"
])

ax4.set_xlabel("Days")

fig.colorbar(
    heat,
    ax=ax4
)
plt.tight_layout()
plt.show()
