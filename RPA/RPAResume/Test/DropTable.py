#Drop Table
# importing sqlite module
import sqlite3
connection = sqlite3.connect('Resume.sqlite3')
connection.execute("DROP TABLE personal_details")
print("data dropped successfully")
connection.close()
