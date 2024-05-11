from faker import Faker
import random

fake = Faker()

def generate_account():
    bank = random.randint(1, 99999)
    account = random.randint(1, 999999999999)
    short_bank = random.randint(1, 99999)
    bank_region = random.choice([1, 2, 3, 4, 9])
    date_opened = fake.date_between(start_date='-30y', end_date='today')

    # Set Bank_Fileset based on Bank_Region
    if bank_region == 1:
        bank_fileset = random.choice(['F', 'G', 'H', 'I', 'J'])
    elif bank_region == 2:
        bank_fileset = random.choice(['A', 'K'])
    elif bank_region == 3:
        bank_fileset = random.choice(['B', 'C', 'D'])
    elif bank_region == 4:
        bank_fileset = 'E'
    elif bank_region == 9:
        bank_fileset = 'L'

    # Set Plan_Type from the specified options
    plan_type = random.choice(['Full', 'Partial', 'Deposit', 'Full Pos Pay', 'Part Pos Pay'])

    # Set Account_Type from the Plan_Type
    if plan_type == 'Deposit':
        account_type = 'D'
    else:
        account_type = 'C'

    # Set Account_Status and potentially Closed_Date
    account_status = random.choice(['O', 'C'])
    closed_date = None
    if account_status == 'C':
        closed_date = fake.date_between(start_date=date_opened, end_date='today')

    return {
        'Bank': bank,
        'Account': account,
        'Bank_Fileset': bank_fileset,
        'Short_Bank': short_bank,
        'Bank_Region': bank_region,
        'Account_Type': account_type,
        'Plan_Type': plan_type,
        'Date_Opened': date_opened,
        'Account_Status': account_status,
        'Closed_Date': closed_date
    }

# Generate 10 mock records for demonstration
mock_accounts = [generate_account() for _ in range(10)]
mock_accounts