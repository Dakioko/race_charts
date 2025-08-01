import bar_chart_race as bcr
import pandas as pd

# Load and prepare data
df = pd.read_csv("data.csv").set_index("year") / 1_000_000  # Convert to millions

bcr.bar_chart_race(
    df=df,
    filename="Pop_Today.mp4",

    orientation="h",
    sort="desc",
    n_bars=11,
    steps_per_period=20,
    period_length=1000,
        interpolate_period=True,
    fixed_max=df.max().max() * 1.1,  # With buffer
    bar_size=.95,

    # Enhanced YouTube presentation
    fig_kwargs={
        'figsize': (16, 9),  # 16:9 aspect ratio
        'dpi': 120,
        'facecolor': '#F8FAFF',

    },

    # Professional styling
    colors=[
        "#CE1126", "#0072C6", "#F55536", "#FCD116", "#018749",
        "#00A1DE", "#D81920", "#4189DD", "#000000", "#17B636", "#FFD700"
    ],
    title={
        'label': 'Eastern Africa Population (1960-2022)\nSource: World Bank',
        'size': 48,
        'weight': 'bold',
        'pad': 15,
        'color': '#2E2E2E'
    },
    period_label={
        'x': .95, 'y': .25,  # Adjusted higher
        'ha': 'right',
        'size': 56,
        'weight': 'bold',
        'color': '#333333',
        'bbox': dict(facecolor='white', alpha=0.7, pad=5)
    },
    period_summary_func=lambda v, r: {
        'x': .98, 'y': .08,  # Positioned lower
        's': f'Total: {v.sum():,.1f}M\n@kioko_steve',
        's': f'Total: {v.sum() / 1_000_000:,.1f}M\n@kioko_steve',
        'ha': 'right',
        'size': 24,
        'weight': 'bold',
        'bbox': dict(facecolor='white', alpha=0.7, pad=5)
    },
    bar_kwargs={
        'alpha': .97,
        'lw': 0.5,
        'ec': 'white',
        'capstyle': 'round'
    },
    bar_texttemplate='{x:,.1f}M',
    period_template='{x:.0f}',
    shared_fontdict={'family': 'sans-serif'}
)
