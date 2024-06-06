from common.config_manager import Config_Manager
import logging, coloredlogs

class Log_Manager:
    """_summary_ : logger를 생성하여 리턴한다
    """
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Log_Manager, cls).__new__(cls)
        return cls.instance
    
    def __init__(self) -> None:
        pass
    
    def getLogger(self, name):
        cm = Config_Manager()
        log_level = cm.properties['DEFAULT']['LOG_LEVEL'] if 'LOG_LEVEL' in cm.properties['DEFAULT'] else '30'
        
        #  print('LOG_LEVEL is ', log_level)
        
        logger = logging.getLogger(name)   
        logger.setLevel(int(log_level))

        ## log file
        fh = logging.FileHandler('app.log')
        fh.setLevel(int(log_level))

        # log console
        ch = logging.StreamHandler()
        ch.setLevel(int(log_level))

        # log format
        formatter = logging.Formatter( '%(asctime)s - [%(name)s] - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)

        logger.addHandler(ch)
        logger.addHandler(fh)

        coloredlogs.install()

        return logger