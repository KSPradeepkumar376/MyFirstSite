#Create Table
import sqlite3
connection_obj = sqlite3.connect('Resume.sqlite3')
cursor_obj = connection_obj.cursor()
cursor_obj.execute("DROP TABLE IF EXISTS personal_details")
table = """ CREATE TABLE personal_details (
id bigint NOT NULL PRIMARY KEY,
Name VARCHAR(255) NOT NULL,
Date_of_Birth VARCHAR(255) NOT NULL,
Website VARCHAR(255) NULL,
PhoneNumber VARCHAR(255) NOT NULL,
City VARCHAR(255) NOT NULL,
Degree VARCHAR(255) NULL,
Email VARCHAR(255) NULL,
Freelance VARCHAR(255) NULL); """
cursor_obj.execute(table)
cursor_obj.close()