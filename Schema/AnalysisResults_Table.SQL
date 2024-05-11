CREATE TABLE AnalysisResults_Table (
    Result_ID VARCHAR(255) PRIMARY KEY,
    AnlysisType VARCHAR(255),
    Generated_Date DATE,
    Bank INT CHECK (Bank > 0 AND Bank < 100000),
    Account INT CHECK (Account > 0 AND Account < 1000000000000),
    Bank_Fileset VARCHAR(1),
    ResultData NVARCHAR(MAX),
    FOREIGN KEY (Bank, Account) REFERENCES Accounts_Table
);