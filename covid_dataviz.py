import pandas as pd
import plotly.express as px

# Create dataset manually
data = {
    "date": ["2020-01", "2020-06", "2021-01", "2021-06", "2022-01"],
    "USA": [1000, 2000000, 20000000, 33000000, 60000000],
    "India": [500, 500000, 10000000, 30000000, 40000000],
    "Malaysia": [100, 10000, 100000, 700000, 3000000]
}

df = pd.DataFrame(data)

# Convert to long format
df = df.melt(id_vars="date", var_name="Country", value_name="Total Cases")

# Create visualization
fig = px.line(
    df,
    x="date",
    y="Total Cases",
    color="Country",
    title="COVID-19 Cases Growth Comparison (2020–2022)",
    markers=True
)

# Improve design
fig.update_layout(
    title_x=0.5,
    xaxis_title="Date",
    yaxis_title="Total Cases",
    template="plotly_white"
)

fig.show()