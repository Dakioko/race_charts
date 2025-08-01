import bar_chart_race as bcr
import pandas as pd

# ===== DATA PREPARATION =====
# Load and convert population to millions
df = pd.read_csv("Top_15_africa.csv").set_index("Year") / 1_000_000

# ===== COUNTRY COLOR MAPPING =====
country_colors = {
    # North Africa
    'Algeria': '#006633',
    'Egypt': '#C8102E',
    'Libya': '#239E46',
    'Morocco': '#B7312C',
    'Tunisia': '#E70013',
    'Sudan': '#DA121A',
    'South Sudan': '#000000',
    
    # West Africa
    'Nigeria': '#008751',
    'Ghana': '#006B3F',
    'Senegal': '#00853F',
    'Ivory Coast': '#F77F00',
    'Mali': '#14B53A',
    'Burkina Faso': '#EF3340',
    'Niger': '#E05206',
    'Benin': '#008751',
    'Togo': '#FFCE00',
    'Liberia': '#002868',
    'Sierra Leone': '#1EB53A',
    'Guinea': '#CE1126',
    'Guinea-Bissau': '#CE1126',
    'Gambia': '#3A7728',
    'Cape Verde': '#003893',
    'Mauritania': '#006233',
    
    # Central Africa
    'DRC': '#007fff',
    'Angola': '#FF0000',
    'Cameroon': '#007A5E',
    'Chad': '#002664',
    'Central African Republic': '#0033A0',
    'Congo, Rep': '#009543',
    'Gabon': '#3A75C4',
    'Equatorial Guinea': '#3E9A00',
    'Sao Tome and Principe': '#12AD2B',
    
    # East Africa
    'Ethiopia': '#FCDD09',
    'Kenya': '#008C51',
    'Tanzania': '#1EB53A',
    'Uganda': '#FCDC04',
    'Rwanda': '#00A1DE',
    'Burundi': '#1EB53A',
    'Somalia': '#4189dd',
    'Djibouti': '#6AB2E7',
    'Eritrea': '#EA0437',
    'Seychelles': '#003F87',
    'Comoros': '#009639',
    'Madagascar': '#F9423A',
    
    # Southern Africa
    'South Africa': '#001489',
    'Namibia': '#003580',
    'Botswana': '#75AADB',
    'Zimbabwe': '#FFD100',
    'Zambia': '#198A00',
    'Malawi': '#CE1126',
    'Mozambique': '#008E49',
    'Lesotho': '#00209F',
    'Eswatini': '#3E5EB9',
    'Mauritius': '#EA2839'
}

# Get colors in dataset order (default gray for missing countries)
colors = [country_colors.get(country, '#555555') for country in df.columns]

# ===== BAR CHART RACE =====
bcr.bar_chart_race(
    df=df,
    filename="Pop_T_15_new.mp4",
    img_label_folder="bar_image_labels",
    fig_kwargs={
        'figsize': (28, 15.75),  # 4K-ready dimensions
        'dpi': 120,
        'facecolor': '#F8FAFF'
    },
    orientation="h",
    sort="desc",
    n_bars=11,
    steps_per_period=30,
    period_length=462.5,
    interpolate_period=True,
    fixed_max=True,
    colors=colors,
    title={
        'label': 'African Population Growth (1960-2024) \nSource: World Bank',
        'size': 48,
        'weight': 'bold',
        'pad': 15,
        'color': '#2E2E2E'
    },
    period_label={
        'x': .95, 'y': .20,
        'ha': 'right',
        'size': 72,
        'weight': 'bold',
        'color': '#333333',
        
    },
    period_summary_func=lambda v, r: {
        'x': .98, 'y': .08,
        's': f'Total: {v.sum():,.1f}M\n@kioko_Steve',
        'ha': 'right',
        'size': 24,
        'weight': 'bold',
        
    },
    bar_label_font={'size': 22},
    tick_label_font={'size': 20},
    bar_kwargs={
        'alpha': 0.97,
        'lw': 0.5,
        'ec': 'white',
        'capstyle': 'round'
    },
    bar_texttemplate='{x:,.1f}M',  # Displays values as "X.XM"
    period_template='{x:.0f}',
    bar_size=0.90,
    shared_fontdict={'family': 'sans-serif'}
)

print("Complete:")
