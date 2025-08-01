import bar_chart_race as bcr
import pandas as pd

# Load data
df = pd.read_csv("africa_gdp_processed.csv").set_index("Year")
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

bcr.bar_chart_race(
    df=df,
    filename="GDP.mp4",
    fig_kwargs={
        'figsize': (16, 9),
        'dpi': 144,  # Increased DPI for better quality
        'facecolor': '#F8FAFF',
       
    },
    orientation="h",
    sort="desc",
    n_bars=10,
    colors=colors,
    steps_per_period=30,  # Smoother animation
    period_length=1387,
    interpolate_period=True,  # Smoother transitions between years
    fixed_max=df.values.max() * 1.1,  # 10% buffer above highest value
    filter_column_colors=True,  # Better color consistency
    
    title={
        'label': 'Top 10 African Economies by GDP (1960-2022)\nSource: World Bank',
        'size': 24,
        'weight': 'bold',
        'pad': 20,  # Increased padding
        'color': '#000000'
    },
    
    period_label={
        'x': 0.95,
        'y': 0.25,  # Moved higher to avoid overlap
        'ha': 'right',
        'va': 'center',
        'size': 36,
        'weight': 'semibold',
        'color': '#333333',
        'bbox': dict(facecolor='white', alpha=0.7, edgecolor='none', pad=5)  # Added background
    },
    
    period_summary_func=lambda v, r: {
        'x': 0.98,
        'y': 0.08,  # Positioned lower
        's': f'Total GDP: ${v.sum():,.1f}B\n@Kioko_Steve',
        'ha': 'right',
        'size': 16,  # Slightly smaller
        'weight': 'bold',
        'color': '#333333',
        'bbox': dict(facecolor='white', alpha=0.7, edgecolor='none', pad=5)  # Added background
    },
    
    bar_label_font={
        'size': 14,
        
    },
    tick_label_font={
        'size': 12,
        'color': '#555555'
    },
    bar_kwargs={
        'alpha': 0.95,
        'lw': 0.5,
        'ec': 'white',
        'capstyle': 'round'  # Rounded bar edges
    },
    bar_texttemplate='${x:,.1f}B',
    period_template='{x:.0f}',
    #colors='dark24',  # Better color palette
    #cmap='dark24',  # Consistent colors
    scale='linear',
    bar_size=0.9,  # Slightly thinner bars for better spacing
    shared_fontdict={'family': 'sans-serif'},  # Consistent font
)