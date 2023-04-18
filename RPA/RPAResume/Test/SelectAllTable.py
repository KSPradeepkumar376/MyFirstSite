
#SelectAll Table
# importing sqlite module
import sqlite3
connection = sqlite3.connect('Resume.sqlite3')
a = connection.execute("SELECT * FROM SocialMedia")
print(a.fetchall())
connection.close()
