import pandas as pd

data = {
    "Name": ["Hans", "Lisa", "Tobi"],
    "Alter": [10, 12, 15],
    "Stadt": ["Stuttgart", "München", "Hamburg"],
}

df = pd.DataFrame(data)

df.head(2)

print(df.head(2))
