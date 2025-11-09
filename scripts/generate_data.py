import pandas as pd
from faker import Faker
import random
import os

fake = Faker()

def generate_sales_data(branch_id, n=1000):
    records = []
    for _ in range(n):
        records.append({
            "sale_id": fake.uuid4(),
            "branch_id": branch_id,
            "customer_id": fake.uuid4(),
            "product_id": random.randint(1000, 9999),
            "quantity": random.randint(1, 10),
            "price": round(random.uniform(5.0, 500.0), 2),
            "date": fake.date_between(start_date="-90d", end_date="today")
        })
    return pd.DataFrame(records)

def generate_customers_data(branch_id, n=500):
    records = []
    for _ in range(n):
        records.append({
            "customer_id": fake.uuid4(),
            "branch_id": branch_id,
            "name": fake.name(),
            "email": fake.email(),
            "city": fake.city(),
            "signup_date": fake.date_between(start_date="-2y", end_date="today")
        })
    return pd.DataFrame(records)

def generate_inventory_data(branch_id, n=200):
    records = []
    for _ in range(n):
        records.append({
            "product_id": random.randint(1000, 9999),
            "branch_id": branch_id,
            "product_name": fake.word().capitalize(),
            "category": random.choice([
                "Electronics", "Clothing", "Groceries", "Furniture", "Accessories"
            ]),
            "stock_quantity": random.randint(0, 500),
            "unit_price": round(random.uniform(10.0, 300.0), 2)
        })
    return pd.DataFrame(records)

if __name__ == "__main__":
    base_path = "data/raw"
    os.makedirs(f"{base_path}/sales", exist_ok=True)
    os.makedirs(f"{base_path}/customers", exist_ok=True)
    os.makedirs(f"{base_path}/products", exist_ok=True)

    num_branches = 5  # adjust this if you want more branches

    for branch_id in range(1, num_branches + 1):
        sales_df = generate_sales_data(branch_id)
        customers_df = generate_customers_data(branch_id)
        inventory_df = generate_inventory_data(branch_id)

        sales_path = f"{base_path}/sales/branch_{branch_id}_sales.csv"
        customers_path = f"{base_path}/customers/branch_{branch_id}_customers.csv"
        products_path = f"{base_path}/products/branch_{branch_id}_inventory.csv"

        sales_df.to_csv(sales_path, index=False)
        customers_df.to_csv(customers_path, index=False)
        inventory_df.to_csv(products_path, index=False)

        print(f"Data generated for Branch {branch_id}")

    print("\nAll branch datasets generated successfully!")
