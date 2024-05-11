CREATE TABLE Accounts_Table (
    Bank INT CHECK (Bank > 0 AND Bank < 100000),
    Account INT CHECK (Account > 0 AND Account < 1000000000000),
    Bank_Fileset VARCHAR(1),
    Short_Bank INT CHECK (Short_Bank > 0 AND Short_Bank < 100000),
    Bank_Region INT CHECK (Bank_Region IN (1, 2, 3, 4, 9)),
    Account_Type VARCHAR(1),
    Plan_Type VARCHAR(255) NOT NULL,
    Date_Opened DATE,
    Date_Closed DATE,
    Account_Status VARCHAR(1),
    PRIMARY KEY (Bank, Account)
);