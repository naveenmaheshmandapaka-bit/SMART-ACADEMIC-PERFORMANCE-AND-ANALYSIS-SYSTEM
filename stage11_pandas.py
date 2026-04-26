import pandas as pd

data = {
    "Name": ["Ram", "Ravi"],
    "Marks": [80, 70]
}

df = pd.DataFrame(data)
print(df.describe())
