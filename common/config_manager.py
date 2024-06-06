from configparser import ConfigParser
from common.entities import ORACLE_DB
import os

class Config_Manager:
    ## 
    properties = None
    ora_info =  None
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Config_Manager, cls).__new__(cls)
            
            run_mode = os.getenv("RUN_MODE")
            if not( run_mode == 'PRD' or run_mode =='DEV') : run_mode = 'TEST'
            
            
            cfg = ConfigParser()
            cfg.read("./config/" + run_mode.lower() + "_config.ini", encoding='UTF-8')
            
            
            oracle_db = ORACLE_DB()
            oracle_db.NAME = cfg['DATABASE']['NAME']
            oracle_db.HOST = cfg['DATABASE']['HOST']
            oracle_db.PORT = cfg['DATABASE']['PORT']
            oracle_db.USER_ID = cfg['DATABASE']['USER_ID']
            oracle_db.USER_PW = cfg['DATABASE']['USER_PW']
            oracle_db.DB_NAME = cfg['DATABASE']['DB_NAME']
            
            Config_Manager.ora_info = oracle_db
            Config_Manager.properties = cfg
            
        return cls.instance     
        
    def __init__(self) -> None:
        self.setOracle()

    def setOracle(self):
        pass
        # cfg = Config_Manager.properties
        # oracle_db = ORACLE_DB()
        # oracle_db.NAME = cfg['DATABASE']['NAME']
        # oracle_db.HOST = cfg['DATABASE']['HOST']
        # oracle_db.PORT = cfg['DATABASE']['PORT']
        # oracle_db.USER_ID = cfg['DATABASE']['USER_ID']
        # oracle_db.USER_PW = cfg['DATABASE']['USER_PW']
        # oracle_db.DB_NAME = cfg['DATABASE']['DB_NAME']
        # Config_Manager.ora_info = oracle_db

        # print(oracle_db )        

    def setDB_Conn(self):
        log_level = cm.properties['DEFAULT']['LOG_LEVEL2'] if 'LOG_LEVEL2' in cm.properties['DEFAULT'] else '10'
        print(log_level)
        pass
    
    def getProperty(self, sec:str, key:str):
        """Section과 Key해당되는 value를 리턴한다

        Args:
            sec (str): section
            key (str): key
        Returns:
            any : key에 지정된 값
        """
        try:
            return self._config[sec][key]
        except:
            return None