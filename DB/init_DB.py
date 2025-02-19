import sqlite3

con = sqlite3.connect("LPWM.db")
cur = con.cursor()
cur.executescript("""
     CREATE TABLE IF NOT EXISTS Applications(
         application_ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
         name TEXT CHECK(LENGTH(name) <= 100) NOT NULL UNIQUE
     );
     CREATE TABLE IF NOT EXISTS Usernames(
         username_ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
         username TEXT CHECK(LENGTH(username) <= 100) NOT NULL UNIQUE
     );
     CREATE TABLE IF NOT EXISTS Passwords(
         password_ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
         password TEXT CHECK(LENGTH(password) <= 100) NOT NULL UNIQUE
     );
     CREATE TABLE IF NOT EXISTS Recovery_info(
         recovery_info_ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
         email TEXT CHECK(email LIKE '%_@_%._%') NULL,
         phone TEXT CHECK(LENGTH(phone) BETWEEN 10 AND 15) NULL
         );
     CREATE TABLE IF NOT EXISTS Accounts(
         account_ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
         application_ID INTEGER NOT NULL,
         username_ID INTEGER NOT NULL,
         password_ID INTEGER NOT NULL UNIQUE,
         recovery_info_ID INTEGER NULL,
         FOREIGN KEY (application_ID) REFERENCES Applications(application_ID) ON DELETE RESTRICT,
         FOREIGN KEY (username_ID) REFERENCES Usernames(username_ID) ON DELETE RESTRICT,
         FOREIGN KEY (password_ID) REFERENCES Passwords(password_ID) ON DELETE CASCADE,
         FOREIGN KEY (recovery_info_ID) REFERENCES Recovery_info(recovery_info_ID) ON DELETE RESTRICT,
         UNIQUE(application_ID, username_ID, password_ID, recovery_info_ID)
         );
""")
res = cur.execute("SELECT name FROM sqlite_master")
print(res.fetchall())