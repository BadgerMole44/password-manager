import sqlite3, os

class LPWMDB_CRUD:
    def __init__(self):
        self._connection = sqlite3.connect("LPWM.db")
