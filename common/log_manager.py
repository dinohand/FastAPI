import logging, coloredlogs

class Log_Manager:
    """_summary_ : logger를 생성하여 리턴한다
    """
    def __init__(self) -> None:
        pass
    
    def getLogger(self, name):
        logger = logging.getLogger(name)   
        logger.setLevel(logging.INFO)

        ## log file
        fh = logging.FileHandler('app.log')
        fh.setLevel(logging.DEBUG)

        # log console
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # log format
        formatter = logging.Formatter( '%(asctime)s - [%(name)s] - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)

        logger.addHandler(ch)
        logger.addHandler(fh)

        coloredlogs.install()

        return logger