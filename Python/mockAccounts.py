from faker import Faker
import random

fake = Faker()

# Dictionary to track the count of each category
category_count = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}

def generate_account():
    id = random.randint(1, 10000)
    region_code = random.choice([10, 20, 30, 40, 50])
    category = random.choice(['A', 'B', 'C', 'D', 'E'])
    type = random.choice(['Basic', 'Premium'])
    open_date = fake.date_between(start_date='-10y', end_date='today')
    
    status = random.choice(['Active', 'Inactive'])
    close_date = None
    if status == 'Inactive':
        close_date = fake.date_between(start_date=open_date, end_date='today')

    # Increment the category counter
    category_count[category] += 1

    return {
        'ID': id,
        'Region_Code': region_code,
        'Category': category,
        'Type': type,
        'Open_Date': open_date,
        'Status': status,
        'Close_Date': close_date,
        'Category_Counter': category_count[category]
    }

# Generate 10 mock records for demonstration
mock_accounts = [generate_account() for _ in range(10)]
mock_accounts
