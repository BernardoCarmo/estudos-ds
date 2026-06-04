-- EX1
SELECT *
FROM Person.Person

-- EX2
SELECT FirstName, LastName
FROM Person.Person

-- EX3
SELECT JobTitle, Gender, BirthDate
FROM HumanResources.Employee

-- EX4
SELECT *
FROM Person.Person
WHERE PersonType = 'EM'

-- EX5
SELECT FirstName, LastName
FROM Person.Person
WHERE LastName = 'Smith'

-- EX6
SELECT *
FROM HumanResources.Employee
WHERE Gender = 'F'

-- EX7
SELECT *
FROM HumanResources.Employee
WHERE VacationHours > 80

-- EX8
SELECT *
FROM HumanResources.Employee
WHERE Gender = 'F' AND MaritalStatus = 'M'

-- EX9
SELECT DISTINCT BusinessEntityID
FROM Person.Person

-- EX10
SELECT DISTINCT JobTitle
FROM HumanResources.Employee

-- EX11
SELECT COUNT (DISTINCT BusinessEntityID)
FROM Person.Person

-- EX12
SELECT COUNT (DISTINCT BusinessEntityID)
FROM HumanResources.Employee

-- EX13
SELECT COUNT (DISTINCT BusinessEntityID)
FROM HumanResources.Employee
WHERE Gender = 'M'

-- EX14
SELECT COUNT (DISTINCT JobTitle)
FROM HumanResources.Employee

-- EX15
SELECT COUNT (DISTINCT BusinessEntityID)
FROM HumanResources.Employee
WHERE SickLeaveHours > 40

--EX16
SELECT JobTitle, BirthDate
FROM HumanResources.Employee
WHERE MaritalStatus = 'M' AND VacationHours > 90