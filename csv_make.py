import pandas as pd
import numpy as np

try:
    global_df = pd.read_csv('GLB.Ts+dSST.csv', header=1)
    global_df = global_df[['Year', 'J-D']]
    global_df.rename(columns={'J-D': 'Global'}, inplace=True)
except (FileNotFoundError, KeyError) as e:
    print(f"Error processing GLB.Ts+dSST.csv: {e}")
    print("Please ensure the file is downloaded and has the expected 'Year' and 'J-D' columns.")
    exit()

try:
    zonal_df = pd.read_csv('ZonAnn.Ts+dSST.csv') # No header=1 needed
    zonal_df = zonal_df[['Year', '64N-90N', '24N-44N', 'EQU-24N', '24S-EQU', '44S-24S', '90S-64S']]
    zonal_df.rename(columns={
        '64N-90N': 'Arctic',
        '24N-44N': 'N_Mid_Lat',
        'EQU-24N': 'N_Tropic',
        '24S-EQU': 'S_Tropic',
        '44S-24S': 'S_Mid_Lat',
        '90S-64S': 'Antarctic'
    }, inplace=True)
except (FileNotFoundError, KeyError) as e:
    print(f"Error processing ZonAnn.Ts+dSST.csv: {e}")
    print("Please ensure the file is downloaded and has the expected regional columns.")
    exit()

df = pd.merge(global_df, zonal_df, on='Year', how='inner')

for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')

for col in df.columns.drop('Year'):
    df[col] = df[col] / 100.0

df = df.dropna()
df = df[df['Year'] >= 1880].copy()

df['Year'] = df['Year'].astype(int)

df_json = df.round(6).to_dict(orient='records')

import json
with open('climate_data.json', 'w') as f:
    json.dump(df_json, f, indent=2)

print("✅ Success! ")