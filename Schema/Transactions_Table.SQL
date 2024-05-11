CREATE TABLE Transactions_Table (
    GroupID INT CHECK (GroupID > 0 AND GroupID < 100000),
    Serial INT,
    TransactionType VARCHAR(2),
    TransactionDate DATE,
    Amount MONEY,
    Status VARCHAR(1),
    GroupCode VARCHAR(1),
    PRIMARY KEY (GroupCode, GroupID, Serial, TransactionType),
    FOREIGN KEY (GroupCode, GroupID) REFERENCES GroupsID_Table(GroupCode, GroupID)     
);