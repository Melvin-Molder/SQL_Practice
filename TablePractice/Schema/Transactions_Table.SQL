CREATE TABLE Transactions_Table (
    Short_Bank INT CHECK (Short_Bank > 0 AND Short_Bank < 100000),
    Serial INT,
    Transaction_Type VARCHAR(2),
    Transaction_Date DATE,
    Amount MONEY,
    Status VARCHAR(1),
    Bank_Fileset VARCHAR(1),
    PRIMARY KEY (Bank_Fileset, Short_Bank, Serial, Transaction_Type)     
);