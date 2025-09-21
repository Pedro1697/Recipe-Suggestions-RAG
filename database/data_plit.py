import pandas as pd

import pandas as pd

df = pd.read_csv("data/recipes.csv")

df_sample = df.sample(n=20000, random_state=42)

df_sample.to_csv("data/recipes_20k.csv", index=False)

