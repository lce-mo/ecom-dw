import random, pandas as pd
from faker import Faker
from datetime import datetime, timedelta

fake = Faker("zh_CN")
random.seed(42)

users = pd.DataFrame([{"user_id": i, "name": fake.name(), "city": fake.city(),
                       "register_date": fake.date_between("-1y", "-30d")} for i in range(1, 1001)])

products = pd.DataFrame([{"product_id": i, "category": random.choice(["数码","服饰","食品","家居"]),
                          "price": round(random.uniform(10, 2000), 2)} for i in range(1, 201)])

orders = []
start = datetime(2026, 10, 1)
for oid in range(1, 20001):
    orders.append({"order_id": oid, "user_id": random.randint(1, 1000),
                   "product_id": random.randint(1, 200), "quantity": random.randint(1, 5),
                   "order_time": start + timedelta(minutes=random.randint(0, 30*24*60)),
                   "status": random.choice(["paid","paid","paid","cancelled","refunded"])})
orders = pd.DataFrame(orders)

# 故意加脏数据：重复行、空 user_id、负数数量
orders = pd.concat([orders, orders.sample(200)])
orders.loc[orders.sample(50).index, "user_id"] = None
orders.loc[orders.sample(30).index, "quantity"] = -1

for name, df in [("users", users), ("products", products), ("orders", orders)]:
    df.to_csv(f"data/raw/{name}.csv", index=False)
print("done")
