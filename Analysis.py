import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


prices = pd.read_csv("archive/clean_prices.csv")

prices = prices.drop_duplicates()

prices["calc_inven"].fillna(prices["calc_inven"].median(), inplace=True)

prices = prices.dropna(subset=["price"])

print(prices.head())
print(prices.info())
print("Total rows after cleaning:", prices.shape[0])

orders = pd.read_csv("archive/orders.csv")

print(orders.head())
print(orders.info())

avg_price = prices.groupby("platform")["price"].mean()
print(avg_price)

plt.figure(figsize=(8,5))
sns.barplot(x=avg_price.index, y=avg_price.values)
plt.title("Average Price by Retailer")
plt.xlabel("Retailer Platform")
plt.ylabel("Average Price")
plt.show()

ads_rank = prices.groupby("ads")["rank"].mean()
print(ads_rank)

plt.figure(figsize=(7,4))
sns.barplot(x=ads_rank.index, y=ads_rank.values)
plt.title("Average Rank (Ads vs Non Ads)")
plt.xlabel("Ads")
plt.ylabel("Average Rank")
plt.show()

plt.figure(figsize=(7,4))
sns.scatterplot(data=prices, x="shipping_price", y="rank")
plt.title("Shipping Price vs Product Rank")
plt.show()

plt.figure(figsize=(7,4))
sns.scatterplot(data=prices, x="calc_inven", y="price")
plt.title("Inventory vs Price")
plt.show()

prices["date"] = pd.to_datetime(prices["date"])
price_trend = prices.groupby("date")["price"].mean()

plt.figure(figsize=(10,5))
price_trend.plot()
plt.title("Price Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Average Price")
plt.show()

orders_count = orders.groupby("Category")["Quantity"].sum()

plt.figure(figsize=(8,5))
orders_count.plot(kind="bar")
plt.title("Total Orders by Category")
plt.xlabel("Category")
plt.ylabel("Quantity Sold")
plt.show()