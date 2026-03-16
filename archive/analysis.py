import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("archive/clean_prices.csv")
df.drop_duplicates(inplace=True)

df['calc_inven'] = df['calc_inven'].fillna(df['calc_inven'].median())

print(df.head())
print(df.info())

orders = pd.read_csv("archive/orders.csv")

print(orders.head())
print(orders.info())

df = df.dropna(subset=['price'])





# Check again
print("Total rows after cleaning:", len(df))

avg_price = df.groupby("platform")["price"].mean()

print(avg_price)


plt.figure(figsize=(8,5))

sns.barplot(x=avg_price.index, y=avg_price.values)

plt.title("Average Price by Retailer")
plt.xlabel("Retailer Platform")
plt.ylabel("Average Price")

plt.show()

ads_rank = df.groupby("ads")["rank"].mean()

print(ads_rank)

sns.barplot(x=ads_rank.index, y=ads_rank.values)

plt.title("Average Rank (Ads vs Non Ads)")
plt.xlabel("Ads")
plt.ylabel("Average Rank")

plt.show()

sns.scatterplot(x="shipping_price", y="rank", data=df)

plt.title("Shipping Price vs Product Rank")

plt.show()

sns.scatterplot(x="calc_inven", y="price", data=df)

plt.title("Inventory vs Price")

plt.show()

df['date'] = pd.to_datetime(df['date'])

price_trend = df.groupby("date")["price"].mean()

plt.figure(figsize=(10,5))
price_trend.plot()

plt.title("Price Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Average Price")

plt.show()

orders_count = orders.groupby("Category")["Quantity"].sum()

plt.figure()

orders_count.plot(kind="bar")

plt.title("Total Orders by Category")
plt.xlabel("Category")
plt.ylabel("Quantity Sold")

plt.show()