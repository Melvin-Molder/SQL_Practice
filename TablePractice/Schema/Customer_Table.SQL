CREATE TABLE Customer_Table (
    Bank INT CHECK (Bank > 0 AND Bank < 100000),
    Account INT CHECK (Account > 0 AND Account < 1000000000000),
    Account_Title VARCHAR(255),
    Mailing_Address VARCHAR(255),
    Email_Address VARCHAR(255),
    Phone VARCHAR(255),
    PRIMARY KEY (Bank, Account)    
);