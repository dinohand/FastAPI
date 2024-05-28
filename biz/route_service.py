from common.log_manager import Log_Manager
class Route_Service:
    logger = None
    def __init__(self) -> None:
        self.logger = Log_Manager().getLogger( type(self).__name__ )

    async def heathCheck(self):
        # self.logger.info("health check ---------------")
        return {"message":"ok", "code":200}
    
    def hello(self):
        # self.logger.info("hello----------------")
        return "You need REST Api call"
    