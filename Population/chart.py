import bar_chart_race as bcr
import pandas as pd

# Load data
df = pd.read_csv("data.csv").set_index("year")

# Create bar chart race without image flags
bcr.bar_chart_race(
    df=df,
    filename="Population_F.mp4",
    fig_kwargs={
        'figsize': (28, 15.75),
        'dpi': 120,
        'facecolor': '#F8FAFF'
    },
    orientation="h",
    sort="desc",
    n_bars=11,
    steps_per_period=30,
    period_length=1500,
    colors = [
    "#CE1126", "#0072C6", "#F55536", "#FCD116", "#018749",
    "#00A1DE", "#D81920", "#4189DD", "#000000", "#17B636", "#FFD700"
    ],

    title={
        'label': 'Eastern Africa Population (1960 - 2022) \nSource: World Bank',
        'size': 48,
        'weight': 'bold',
        'pad': 10,
        'color': '#000000'
    },
    period_label={
        'x': .95, 'y': .18,
        'ha': 'right',
        'va': 'center',
        'size': 72,
        'weight': 'semibold',
        'color': '#333333'
    },
    period_summary_func=lambda v, r: {
        'x': .99, 'y': .1,
        's': f'Total: {v.sum() / 1_000_000:,.1f}M\n@kioko_steve',
        'ha': 'right',
        'size': 24,
        'weight': 'semibold'
    },
    bar_label_font={'size': 27},
    tick_label_font={'size': 27},
    bar_kwargs={'alpha': .99, 'lw': 0},
    bar_texttemplate='{x:,.0f}',
    period_template='{x:.0f}'
)
