CREATE TABLE Customer_Table (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,
    CustomerTitle VARCHAR(255),
    MailingAddress VARCHAR(255),
    EmailAddress VARCHAR(255),
    Phone VARCHAR(255),
    FOREIGN KEY (InstitutionID, AccountID) REFERENCES Accounts_Table   
);