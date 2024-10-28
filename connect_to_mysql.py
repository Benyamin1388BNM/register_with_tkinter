import mysql.connector 
conn=mysql.connector.connect(user='root12341234',password='root',host='localhost')
mycursor=conn.cursor()
mycursor.execute('CREATE DATABASE IF NOT EXISTS school_usernames')
mycursor.execute('USE school_usernames')
mycursor.execute('''
    CREATE TABLE IF NOT EXISTS members(
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(255),
        password VARCHAR(255)
        )''')