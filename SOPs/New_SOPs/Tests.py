import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# ----- 1. Sample Data -----
years = list(range(2000, 2020))
np.random.seed(0)
data = {
    'Kenya': np.cumsum(np.random.rand(len(years)) * 5 + 1),
    'Nigeria': np.cumsum(np.random.rand(len(years)) * 6 + 1),
    'South Africa': np.cumsum(np.random.rand(len(years)) * 4 + 2),
    'Egypt': np.cumsum(np.random.rand(len(years)) * 3 + 3),
}
df = pd.DataFrame(data, index=pd.Index(years, name='Year'))

# ----- 2. Interpolation -----
df = df.reindex(pd.date_range(start='2000', end='2019', freq='M'))
df = df.interpolate()

# ----- 3. Set up plot -----
plt.style.use('seaborn-poster')
fig, ax = plt.subplots(figsize=(12, 6))
colors = {
    'Kenya': '#1f77b4',
    'Nigeria': '#ff7f0e',
    'South Africa': '#2ca02c',
    'Egypt': '#d62728',
}
lines = {}
trails = {}
labels = {}

for country in df.columns:
    lines[country], = ax.plot([], [], lw=3, color=colors[country])
    trails[country], = ax.plot([], [], lw=1.5, color=colors[country], alpha=0.3, linestyle='--')
    labels[country] = ax.text(0, 0, '', fontsize=11, color=colors[country])

ax.set_xlim(df.index[0], df.index[-1])
ax.set_ylim(0, df.max().max() * 1.1)
ax.set_title('Line Chart Race', fontsize=16)
ax.set_xlabel('Year')
ax.set_ylabel('Value')
ax.grid(True)

# ----- 4. Animation function -----
def update(frame):
    t = df.index[frame]
    for country in df.columns:
        x = df.index[:frame+1]
        y = df[country].values[:frame+1]
        lines[country].set_data(x, y)
        trails[country].set_data(x[:-5], y[:-5])  # show trail with delay
        labels[country].set_position((x[-1], y[-1]))
        labels[country].set_text(f'{country} ({y[-1]:.0f})')

    # Highlight top country
    top_country = df.iloc[frame].idxmax()
    for country in df.columns:
        lw = 5 if country == top_country else 3
        lines[country].set_linewidth(lw)

    ax.set_title(f'Line Chart Race – {t.strftime("%Y-%m")}', fontsize=16)
    return list(lines.values()) + list(labels.values())

# ----- 5. Create animation -----
ani = FuncAnimation(fig, update, frames=len(df), interval=100, blit=False)

# ----- 6. Save -----
ani.save('line_chart_race.mp4', writer='ffmpeg', dpi=200)
