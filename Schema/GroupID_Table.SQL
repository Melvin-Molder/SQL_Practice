CREATE TABLE GroupsID_Table (
    GroupID INT CHECK (GroupID >= 1 AND GroupID <= 99999),
    GroupCode CHAR(1),
    PRIMARY KEY (GroupCode, GroupID),
    FOREIGN KEY (GroupCode) REFERENCES GroupCodes_Table(Code)
);
