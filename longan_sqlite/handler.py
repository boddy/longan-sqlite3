import sqlite3


class DBHandler:

    def __init__(self, db_path, debug=False):
        self._debug = debug
        self._connect = sqlite3.connect(db_path)
        self._cursor = self._connect.cursor()

    def execute(self, sql, pre=None):
        if self._debug:
            print("[Longan Debug]", end='\t')
            print(sql)
        if pre:
            self._cursor.execute(sql, pre)
        else:
            self._cursor.execute(sql)

        return self._cursor.fetchall()

    def commit(self):
        self._connect.commit()

    def close(self):
        self._cursor.close()
        self._connect.close()

    def desc(self):
        return self._cursor.description

    def affect(self):
        return self._cursor.rowcount

    def last_id(self):
        return self._cursor.lastrowid
