import pandas as pd
df = pd.read_csv("raw_data.csv")
df.drop_duplicates(inplace=True)
df.dropna(subset=['id'], inplace=True)
df.columns = df.columns.str.lower().str.strip()
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df.to_csv("cleaned_data.csv", index=False)
