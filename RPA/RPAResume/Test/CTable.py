import sqlite3
conn = sqlite3.connect('Resume.sqlite3')
cursor = conn.cursor()
table = """ CREATE TABLE personal_details (
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
FName VARCHAR(255) NOT NULL,
Date_of_Birth VARCHAR(255) NOT NULL,
Website VARCHAR(255) NULL,
PhoneNumber VARCHAR(255) NOT NULL,
City VARCHAR(255) NOT NULL,
Degree VARCHAR(255) NULL,
Email VARCHAR(255) NULL,
Freelance VARCHAR(255) NULL); """
cursor.execute(table)
cursor.execute(
'''INSERT INTO personal_details (FName, Date_of_Birth, Website,PhoneNumber,City,Degree,Email,Freelance) VALUES 
('Pradeepkumar KS', '01-06-1991', 'www.examble.com','+91 9750278977','Chennai','Bachelor','pppradeepkumar376@gmail.com','Available')''')
print("Data Inserted in the table: ")
data=cursor.execute('''SELECT * FROM personal_details''')
for row in data:
	print(row)
conn.commit()
conn.close()
