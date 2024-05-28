import pymysql
import sqlite3
from  common.log_manager import Log_Manager

class DM_Manager:
    logger = None
    def __init__(self) -> None:
        logger = Log_Manager().getLogger(type(self).__name__)

    def gegSQLite(self, conn_str):
        conn = sqlite3.connect(conn_str)
        return conn

class SQLite(DM_Manager):
    def __init__(self):
        super.__init__(self)
    
    def getConn():
        pass