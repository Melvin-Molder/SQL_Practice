import pyodbc
from faker import Faker
import random
from datetime import datetime

fake = Faker()

# Establish a connection to the database
try:
    conn = pyodbc.connect(
        'DRIVER={SQL Server};'
        'SERVER=your_server_name;'
        'DATABASE=your_database_name;'
        'UID=your_username;'
        'PWD=your_password')
    cursor = conn.cursor()

    # Populate RegionCodes_Table
    regions = [(i, fake.country()) for i in range(1, 6)]
    cursor.executemany('INSERT INTO RegionCodes_Table (Code, Description) VALUES (?, ?)', regions)

    # Populate GroupCodes_Table
    groups = [('A', 'Type A'), ('B', 'Type B'), ('C', 'Type C')]
    cursor.executemany('INSERT INTO GroupCodes_Table (Code, Description) VALUES (?, ?)', groups)

    # Populate GroupsID_Table
    group_ids = [(i, g[0]) for i in range(1, 4) for g in groups]
    cursor.executemany('INSERT INTO GroupsID_Table (GroupID, GroupCode) VALUES (?, ?)', group_ids)

    # Populate Customer_Table
    customers = [(fake.name(), fake.address(), fake.email(), fake.phone_number()) for _ in range(10)]
    cursor.executemany('INSERT INTO Customer_Table (CustomerTitle, MailingAddress, EmailAddress, Phone) VALUES (?, ?, ?, ?)', customers)

    # Commit and fetch generated CustomerIDs to use in Accounts_Table
    conn.commit()
    cursor.execute('SELECT CustomerID FROM Customer_Table')
    customer_ids = [row[0] for row in cursor.fetchall()]

    # Populate Accounts_Table
    accounts = []
    for cid in customer_ids:
        account_id = random.randint(1000, 9999)
        region_code = random.randint(1, 5)
        group_info = random.choice(group_ids)
        date_opened = fake.date_this_decade()
        accounts.append((cid, 100, account_id, 'Default Account', group_info[1], group_info[0], region_code, 'Check', 'Plan A', date_opened, 'O'))
    cursor.executemany('INSERT INTO Accounts_Table (CustomerID, InstitutionID, AccountID, AccountTitle, GroupCode, GroupID, RegionCode, AccountCategory, ServicePlan, DateOpened, AccountStatus) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', accounts)

    # Populate Transactions_Table using Accounts information
    transactions = []
    for account in accounts:
        for _ in range(5):  # Assume each account has 5 transactions
            serial = fake.random_int(min=1000, max=9999)
            transaction_type = random.choice(['IS', 'CN', 'ST'])  # Issue, Cancel, Stop
            transaction_date = fake.date_this_year()
            transactions.append((account[5], serial, transaction_type, transaction_date, fake.random_number(digits=4), 'N', account[4]))

    cursor.executemany('INSERT INTO Transactions_Table (GroupID, Serial, TransactionType, TransactionDate, Amount, Status, GroupCode) VALUES (?, ?, ?, ?, ?, ?, ?)', transactions)

    # Commit changes and close connection
    conn.commit()

except Exception as e:
    print("An error occurred:", e)
    conn.rollback()

finally:
    cursor.close()
    conn.close()
