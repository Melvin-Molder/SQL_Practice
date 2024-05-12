import pyodbc
from faker import Faker
from datetime import datetime, timedelta
import random

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
    # conn.commit()

    # Populate RegionCodes_Table
    regions = [(i, fake.country()) for i in range(1, 6)]
    cursor.executemany('INSERT INTO RegionCodes_Table (Code, Description) VALUES (?, ?)', regions)

    # Populate GroupCodes_Table
    groups = [('A', 'Type A'), ('B', 'Type B'), ('C', 'Type C')]
    cursor.executemany('INSERT INTO GroupCodes_Table (Code, Description) VALUES (?, ?)', groups)

    # Populate InstitutionIDs based on GroupCodes
    institution_ids = {'A': 101, 'B': 201, 'C': 301}

    # Fetch GroupCodes with their corresponding GroupIDs for dynamic InstitutionID assignment
    cursor.execute('SELECT GroupCode, GroupID FROM GroupsID_Table')
    # print("Institution IDs:", institution_ids)
    group_id_mapping = {row.GroupCode: (row.GroupID, institution_ids[row.GroupCode]) for row in cursor.fetchall()}    
    print("Group ID Mapping:", group_id_mapping)

    # Populate Customer_Table
    customers = [(fake.name(), fake.address(), fake.email(), fake.phone_number()) for _ in range(10)]
    cursor.executemany('INSERT INTO Customer_Table (CustomerTitle, MailingAddress, EmailAddress, Phone) VALUES (?, ?, ?, ?)', customers)
    conn.commit()
    cursor.execute('SELECT CustomerID FROM Customer_Table')
    customer_ids = [row[0] for row in cursor.fetchall()]

    accounts = []
    accountCount = 0
    # Populate Accounts_Table
    for group_code, description in groups:
        cursor.execute('SELECT GroupID FROM GroupsID_Table WHERE GroupCode = ?', (group_code,))
        result = cursor.fetchone()
        # print("Group Code:", group_code)
        account_id = 1000
        group_id = 1
        if result is None:
            # Insert GroupCode only if it does not exist
            cursor.execute('INSERT INTO GroupsID_Table (GroupCode, GroupID) VALUES (?, ?)', (group_code, group_id))
            # print("GroupCode:", group_code, "GroupID:", group_id)
            conn.commit()  # Commit to ensure GroupID is generated
            cursor.execute('SELECT GroupID FROM GroupsID_Table WHERE GroupCode = ?', (group_code,))
            group_id = cursor.fetchone()[0]
        else:
            group_id = result[0]

        # Every customer will get between 1 and 3 accounts assigned to them    
        for cid in customer_ids:
            num_accounts = random.randint(1, 3)
            region_code = random.randint(1, 5)
            for _ in range(num_accounts):
                account_id = account_id + 1
                date_opened = fake.date_this_decade()
                fdate_opened = date_opened.strftime('%Y-%m-%d')
                account_status = random.choice(['O', 'C'])
                if account_status == 'C':
                    additional_days = random.randint(1, 3650)
                    date_closed = date_opened + timedelta(days=additional_days)
                    fdate_closed = str(date_closed)
                else:
                    fdate_closed = None
                institution_id = institution_ids[group_code]
                accounts.append((int(cid), institution_id, account_id, 'Default Account', str(group_code), int(group_id), region_code, 'Check', 'Plan A', fdate_opened, fdate_closed, account_status))
                group_id = group_id + 1
        # Every account has a groupID assigned to them depending on the GroupCode
        # This will create those groupID before accounts are added
        for gID in range(2, group_id):
            cursor.execute('INSERT INTO GroupsID_Table (GroupCode, GroupID) VALUES (?, ?)', (group_code, gID))
            accountCount = accountCount + 1
                
    conn.commit()
    print("Accounts to add:", accountCount)
    print("Inserting Account data")
    # Someone Save me its 2 in the morning and I could not think anymore this should be fixed....
    i = 0
    for ac in (accounts):
        print("count is at:", i)
        print(accounts[i])
        cursor.execute('INSERT INTO Accounts_Table (CustomerID, InstitutionID, AccountID, AccountTitle, GroupCode, GroupID, RegionCode, AccountCategory, ServicePlan, DateOpened, DateClosed, AccountStatus) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', accounts[i])      
        print(accounts[i])
        i = i + 1

    conn.commit()
    print("Account update successful")

    # Populate Transactions_Table using Accounts information
    transactions = []
    for account in accounts:
        for _ in range(5):  # Each account will get this many transactions added
            serial = fake.random_int(min=1000, max=9999)
            transaction_type = random.choice(['IS', 'CN', 'ST'])  # Issue, Cancel, Stop
            transaction_date = fake.date_this_year().strftime('%Y-%m-%d')
            transactions.append((account[5], serial, transaction_type, transaction_date, fake.random_number(digits=4), 'N', account[4]))

    cursor.executemany('INSERT INTO Transactions_Table (GroupID, Serial, TransactionType, TransactionDate, Amount, Status, GroupCode) VALUES (?, ?, ?, ?, ?, ?, ?)', transactions)
    conn.commit()

except Exception as e:
    print("An error occurred:", {e})
    if conn:
        print("Rolling Back...")
        conn.rollback()

finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()