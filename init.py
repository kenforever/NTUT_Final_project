import sqlite3
import uuid
class init(object):
    def __init__(self,uid):
        self.conn = sqlite3.connect("./test.db")
        self.uid = uid