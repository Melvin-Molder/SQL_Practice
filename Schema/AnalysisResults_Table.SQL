CREATE TABLE AnalysisResults_Table (
    ResultID VARCHAR(255) PRIMARY KEY,
    AnlysisType VARCHAR(255),
    GeneratedDate DATE,
    InstitutionID INT,
    AccountID INT,
    GroupCode CHAR(1),
    GroupID INT,
    ResultData NVARCHAR(MAX),
    FOREIGN KEY (InstitutionID, AccountID) REFERENCES Accounts_Table(InstitutionID, AccountID),
    FOREIGN KEY (GroupCode, GroupID) REFERENCES GroupsID_Table(GroupCode, GroupID)
);