import bar_chart_race as bcr
import pandas as pd

# Load and prepare data
df = pd.read_csv("east_africa_population.csv").set_index("Year") / 1_000_000

# Define colors and styling
colors = [
    "#CE1126", "#0072C6", "#F55536", "#FCD116", "#018749",
    "#00A1DE", "#4189DD", "#000000", "#D81920", "#17B636", "#FFD700"
]

# Create the bar chart race
bcr.bar_chart_race(
    df=df,
    filename="Population_July_2025.mp4",
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
    period_length=1387,
    interpolate_period=True,
    fixed_order=False,  # Allows natural ranking changes
    bar_size=.9,  # Makes bars slightly more dynamic
    fixed_max=True,  # Keep x-axis consistent

    # Colors
    colors=colors,

    # Title (updated)
    title={
        'label': 'Eastern Africa Population (1960 - 2024) \nSource: World Bank',
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
        's': f'Total: {v.sum():,.1f}M\n @kioko_Steve',
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
    bar_texttemplate='{x:,.1f}M',
    period_template='{x:.0f}'
)
