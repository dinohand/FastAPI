import os
import configparser


class Config_Manager:
    """_summary_ : 실행 모드 환경 변수 값과 config.ini 에 설정된 환경변수 값을 읽어들인다
    """
    def __init__(self) -> None:
        self._run_mode = os.getenv("RUN_MODE")

        if  self._run_mode =="PRD":
            pass
        elif   self._run_mode =="DEV":
            pass
        elif   self._run_mode =="TEST":
            pass
        else :
              self._run_mode =="TEST"
        print('runmode is  ',self._run_mode)

        self._config = configparser.ConfigParser()
        config_file = "./config/" + self._run_mode.lower() + "_config.ini"
        # print("==== /////// " , config_file)
        self._config.read(config_file)
    
    
    def getProperty(self, sec:str, key:str):
        try:
            return self._config[sec][key]
        except:
            return None

    @property
    def run_mode(self):
        return self._run_mode
    
    def set_Properties(self):
        pass
