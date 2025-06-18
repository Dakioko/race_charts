import pandas as pd
import bar_chart_race as bcr

data = pd.read_csv("Req.csv")
data = data.set_index('Date')

bcr.bar_chart_race(
    df=data,
    filename='Requests_June.mp4',
    title={
        'label': 'SOPs Requests Over Time',
        'size': 48,
        'weight': 'bold',
        'pad': 10
    },
    fig_kwargs={
        'figsize': (28, 15.75),
        'dpi': 120,
        'facecolor': '#F8FAFF'
    },
    orientation='h',
    sort='desc',
    n_bars=10,
    steps_per_period=30,  # Reduced from 45
    period_length=1500,  # Reduced from 2000
    #fixed_max=True,
    filter_column_colors=True,
    
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
        's': f'Total: {v.nlargest(52).sum():,.0f} requests \n@kioko_steve',
        'ha': 'right',
        'size': 24, 
        'weight': 'semibold'
    },
    
    bar_label_font={'size': 27},
    tick_label_font={'size': 27},
    bar_kwargs={'alpha': .99, 'lw': 0},
    bar_texttemplate='{x:,.0f}',
)