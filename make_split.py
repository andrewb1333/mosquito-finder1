import pandas as pd
from sklearn.model_selection import train_test_split

# Load the csv file
df = pd.read_csv("smallabundance1622.csv")

# Group by 'code' column and calculate the mean of 'total' for each group
df = df.groupby('code').agg({'total': 'mean'}).reset_index()

# Add a new column 'label'
df['label'] = df['total'].apply(lambda x: 1 if x > 20 else (0 if x < 5 else 'drop'))

# Remove rows with 'label' == 'drop'
df = df[df['label'] != 'drop']

# Make sure 'label' is integer
df['label'] = df['label'].astype(int)

# Split the dataframe into train, validation, and test
train_df, temp_df = train_test_split(df, train_size=0.8, stratify=df['label'], random_state=42)
val_df, test_df = train_test_split(temp_df, test_size=0.5, stratify=temp_df['label'], random_state=42)

# Add a new column 'split' with either 'train', 'val', or 'test'
df['split'] = df.index.map(lambda x: 'train' if x in train_df.index else ('val' if x in val_df.index else 'test'))

print(df[df['split']=='test'])
df.to_csv("split_mos.csv")