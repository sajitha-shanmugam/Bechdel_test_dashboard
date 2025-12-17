import kagglehub
import pandas as pd

# 1) Download + load
path = kagglehub.dataset_download("nliabzd/movies-imdb-and-bechdel-information")
csv_path = f"{path}/Bechdel_IMDB_Merge0524.csv"

print("CSV path:", csv_path)
df = pd.read_csv(csv_path)

print(df.head())
print(df.columns)

# 2) OPTIONAL: rename column to easier name
df = df.rename(columns={'bechdelRating': 'bechdel_rating'})

# 3) Clean
df = df.dropna(subset=['bechdel_rating', 'year'])
df['year'] = pd.to_numeric(df['year'], errors='coerce')
df = df[df['year'] >= 1900]

# 4) Save cleaned file
df.to_csv('cleaned_data.csv', index=False)
print("Saved cleaned_data.csv")
