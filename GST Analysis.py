import pandas as pd
df = pd.read_csv(r"-------.csv")
print(df.head())
print(df.info())
# Calculation Year over Year Growth, and the share of Domestic & Import
df["Year"] = df["Year"].str[:4].astype(int)
df["YOY Growth"] = df["Total GST Collection"].pct_change()*100
df["Domestic Share"] = round(((df["Total GST Collection"] - df["Import"]) / df["Total GST Collection"])*100,2)
df["Import Share"] = round((df["Import"] / df["Total GST Collection"])*100,2)

# Calculate CAGR Growth
start_value = df["Total GST Collection"].iloc[0]
end_value = df["Total GST Collection"].iloc[-1]
years = df["Year"].iloc[-1]-df["Year"].iloc[0]
df["CAGR"] = round(((end_value/start_value)**(1/years)-1)*100,2)
print(df.head())

import matplotlib.pyplot as plt
plt.figure(figsize=(8,6))
plt.plot(df["Year"], df["Total GST Collection"], marker = "o", color = "Blue")
plt.title("Total GST Collection over Years")
plt.xlabel("Years")
plt.ylabel("Total GST Collection (In - Crores)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()


plt.figure(figsize=(8,5))
plt.bar(df["Year"], df["Domestic Share"], label = "Domestic Share", color = "Green")
plt.bar(df["Year"], df["Import Share"], bottom=df["Domestic Share"], label = "Import Share", color = "orange")
plt.title("Domestic VS Import Share of GST Collection")
plt.xlabel("Year")
plt.ylabel("Percentage %")
plt.legend()
plt.tight_layout()
plt.show()

df.to_csv(r"-------", index=False)

