#%%

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# %%
index = ["Time", "Connected", "URLs"]

df = pd.read_csv("~/track.txt",
                 sep=";",
                 names=index,
                 header=0)

df["Datetime"] = pd.to_datetime(df["Time"], unit="s")
df.set_index("Datetime", inplace=True)

df["Connected"] = df["Connected"].eq(" True")

# %%

fl = df.Connected.astype(float)
fl.loc["2021-12-02"].plot(figsize=(12, 5))
# %%


