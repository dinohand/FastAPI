from common.config_manager import Config_Manager

class Flask_obj:

    def __init__(self) -> None:
        setProperty()

    def setProperty(self):
        cm =  Config_Manager()
        self.__port = cm.getProperty("FLASK","PORT")
        self.__url_rule  = cm.getProperty("FLASK","URL_RULE")
    @property
    def port(self)
        return self._port
    
    @property
    def url_rule(self)
        return self._url_rule
        