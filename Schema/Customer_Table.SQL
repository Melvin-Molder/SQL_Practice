CREATE TABLE Customer_Table (
    CustomerID INT IDENTITY(1,1) PRIMARY KEY,
    CustomerTitle VARCHAR(255),
    MailingAddress VARCHAR(255),
    EmailAddress VARCHAR(255),
    Phone VARCHAR(255)
);