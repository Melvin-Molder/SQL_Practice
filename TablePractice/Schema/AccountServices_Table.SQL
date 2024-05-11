CREATE TABLE AccountServices_Table (
    Bank INT CHECK (Bank > 0 AND Bank < 100000),
    Account INT CHECK (Account > 0 AND Account < 1000000000000),
    Service_Type VARCHAR(255),
    Start_Date DATE,
    End_Date DATE,
    PRIMARY KEY (Bank, Account, Start_Date)  
);