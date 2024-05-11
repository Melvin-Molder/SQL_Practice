CREATE TABLE GroupsID_Table (
    GroupID INT,
    GroupCode CHAR(1),
    PRIMARY KEY (GroupID, GroupCode),
    FOREIGN KEY (GroupCode) REFERENCES GroupCodes_Table(Code)
    CHECK (GroupID >= 1 AND GroupID <= 99999)
);
