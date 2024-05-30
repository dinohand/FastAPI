from common.log_manager import Log_Manager

from fastapi import FastAPI
from fastapi import Request, Response, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


# 라우트에 따른 처리 프로세스
class Route_Service:
    logger = None
    def __init__(self) -> None:
        self.logger = Log_Manager().getLogger( type(self).__name__ )
        self.templates = Jinja2Templates(directory="static")   ### templates.TemplateResponse를 사용하려면 Route_Service에서 선언되어야 있어야 한다

    ## root page route
    def root(self) -> str:
        status_code = 200
        message =  "This is root page !"
        return {"message": message, "code": status_code}

    async def heathCheck(self) -> str:
        # self.logger.info("health check ---------------")
        return {"message":"ok", "code":200}
    
    def hello(self):
        # self.logger.info("hello----------------")
        return "You need REST Api call"

    # Static html을 서비스하는 route
    async def item(self, request : Request,  item : str, response_class=HTMLResponse ):
        return self.templates.TemplateResponse(
            request=request, name="test.html", context={"item_name": item}
        )

    # async def read_item(request: Request, item: str):
#     return templates.TemplateResponse(
#         request=request, name="test.html", context={"item_name": item}
#     )   
    def test(self):
        pass