import bar_chart_race as bcr
import pandas as pd

# Load and prepare data
df = pd.read_csv("data.csv").set_index("year")
print(df.index.dtype)  # Verify index is int64

# Define colors and styling
colors = [
    "#CE1126", "#0072C6", "#F55536", "#FCD116", "#018749",
    "#00A1DE", "#D81920", "#4189DD", "#000000", "#17B636", "#FFD700"
]

# Create the bar chart race
bcr.bar_chart_race(
    df=df,
    filename="Population_4.mp4",
    img_label_folder="bar_image_labels",

    # Figure settings
    fig_kwargs={
        'figsize': (28, 15.75),
        'dpi': 120,
        'facecolor': '#F8FAFF'
    },

    # Animation controls
    orientation="h",
    sort="desc",
    n_bars=11,
    steps_per_period=30,
    period_length=1500,

    # Colors
    colors=colors,

    # Title (updated)
    title={
        'label': 'Eastern Africa Population (1960 - 2022) \nSource: World Bank',
        'size': 48,
        'weight': 'bold',
        'pad': 12,
        'color': '#000000'
    },

    # Year label
    period_label={
        'x': .95, 'y': .18,
        'ha': 'right',
        'va': 'center',
        'size': 72,
        'weight': 'semibold',
        'color': '#333333'
    },

    # Summary (updated to show millions)
    period_summary_func=lambda v, r: {
        'x': .99, 'y': .1,
        's': f'Total: {v.sum() / 1_000_000:,.1f}M\n@kioko_steve',
        'ha': 'right',
        'size': 24,
        'weight': 'semibold'
    },

    # Font settings
    bar_label_font={'size': 27},
    tick_label_font={'size': 27},

    # Bar appearance
    bar_kwargs={
        'alpha': .99,
        'lw': 0
    },

    # Number formatting
    bar_texttemplate='{x:,.0f}',
    period_template='{x:.0f}'
)