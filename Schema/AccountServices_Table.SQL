CREATE TABLE AccountServices_Table (
    InstitutionID INT CHECK (InstitutionID > 0 AND InstitutionID < 100000),
    AccountID INT CHECK (AccountID > 0 AND AccountID < 1000000000000),
    ServiceType VARCHAR(255),
    StartDate DATE,
    StartTime TIME,
    EndDate DATE,
    PRIMARY KEY (InstitutionID, AccountID, StartDate, StartTime),
    FOREIGN KEY (InstitutionID, AccountID) REFERENCES Accounts_Table(InstitutionID, AccountID)     
);