CREATE TABLE Accounts_Table (
    CustomerID INT,
    InstitutionID INT CHECK (InstitutionID > 0 AND InstitutionID < 100000),
    AccountID INT CHECK (AccountID > 0 AND AccountID < 1000000000000),
    AccountTitle VARCHAR(255),
    GroupCode VARCHAR(1),
    GroupID INT,
    RegionCode INT,
    AccountCategory VARCHAR(14),
    ServicePlan VARCHAR(255),
    DateOpened DATE NOT NULL,
    DateClosed DATE,
    AccountStatus VARCHAR(1) CHECK (AccountStatus IN ('O', 'C')),
    PRIMARY KEY (InstitutionID, AccountID),
    FOREIGN KEY (CustomerID) REFERENCES Customer_Table(CustomerID),
    FOREIGN KEY (RegionCode) REFERENCES RegionCodes_Table(Code),
    FOREIGN KEY (GroupCode, GroupID) REFERENCES GroupsID_Table(GroupCode, GroupID)
);