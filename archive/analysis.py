import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("archive/clean_prices.csv")
orders = pd.read_csv("archive/orders.csv")

df.drop_duplicates(inplace=True)

# Fill missing inventory with median
df['calc_inven'] = df['calc_inven'].fillna(df['calc_inven'].median())

# Remove rows with missing price
df = df.dropna(subset=['price'])

print("Dataset Overview")
print(df.info())

print("\nOrders Dataset")
print(orders.info())

median_price = df.groupby("platform")["price"].median()

plt.figure(figsize=(8,5))
sns.barplot(x=median_price.index, y=median_price.values)

plt.title("Median Price by Platform")
plt.xlabel("Platform")
plt.ylabel("Median Price")

plt.show()
plt.figure(figsize=(8,5))
sns.histplot(df["price"], bins=20, kde=True)

plt.title("Price Distribution of Power Drills")
plt.xlabel("Price")
plt.ylabel("Frequency")

plt.show()

plt.figure(figsize=(8,5))
sns.boxplot(x="ads", y="price", data=df)

plt.title("Price Comparison (Ads vs Non Ads)")
plt.xlabel("Ads")
plt.ylabel("Price")

plt.show()
sns.scatterplot(x="calc_inven", y="rank", data=df)

plt.title("Inventory vs Product Rank")
plt.xlabel("Inventory")
plt.ylabel("Rank")

plt.show()

shipping_avg = df.groupby("platform")["shipping_price"].mean()

plt.figure(figsize=(8,5))
shipping_avg.plot(kind="bar")

plt.title("Average Shipping Cost by Platform")
plt.xlabel("Platform")
plt.ylabel("Shipping Price")

plt.show()

df['date'] = pd.to_datetime(df['date'])

trend = df.groupby("date")["price"].median()

plt.figure(figsize=(10,5))
trend.plot()

plt.title("Median Price Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Median Price")

plt.show()

orders_summary = orders.groupby("Category")["Quantity"].sum().sort_values(ascending=False)

plt.figure(figsize=(8,5))
orders_summary.plot(kind="bar")

plt.title("Orders Distribution by Category")
plt.xlabel("Category")
plt.ylabel("Total Quantity")

plt.show()