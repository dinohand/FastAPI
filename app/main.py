from fastapi import FastAPI
from fastapi import Response, Request, Body
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

from pydantic import BaseModel

from app.common.config_manager import Config_Manager
from app.common.log_manager import Log_Manager
from app.biz.route_service import Route_Service

from app.biz.queries import *
from app.common.const import *


logger = Log_Manager().getLogger("MAIN")

cm = Config_Manager() ## config manager
rs = Route_Service()

logger.debug( f'Main Module({__file__}) is activated' )

# swagger_ui_default_parameters: Annotated[
#     Dict[str, Any],
#     Doc(
#         # """
#         # Default configurations for Swagger UI.

#         # You can use it as a template to add any other configurations needed.
#         # """
#     ),
# ] = {
#     "dom_id": "#swagger-ui",
#     "layout": "BaseLayout",
#     "deepLinking": True,
#     "showExtensions": True,
#     "showCommonExtensions": True,
# }


app = FastAPI(
            # swagger_ui_parameters=swagger_ui_default_parameters,
            swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"},
            title='title',
            summary='summary',
            description='Boilerplate',
            version='0.1',
            docs_url='/api/v1/docs',
            redoc_url='/api/v1/redocs',
            terms_of_service="", ## "http://example.com/terms/",
            contact={
                "name": "JK.Youk",
                "url":  "https://github.com/dinohand",
                "email": "excelon@live.co.kr",
            },            
            license_info={
                "name": "Apache 2.0",
                "identifier": "MIT",
                #  "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
            },
        )

# tags_metadata = [
#     {
#         "name": "users",
#         "description": "Operations with users. The **login** logic is also here.",
#     },
#     {
#         "name": "items",
#         "description": "Manage items. So _fancy_ they have their own docs.",
#         "externalDocs": {
#             "description": "Items external docs",
#             "url": "https://fastapi.tiangolo.com/",
#         },
#     },
# ]
# app = FastAPI(openapi_tags=tags_metadata)

app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/NAS", StaticFiles(directory="NAS"), name="NAS")

#---------------------------------------------------
@app.get('/')
async def read_item():
    return await rs.root()

async def check_health():
    return await rs.heathCheck()

@app.post('/fileupload')
async def upload():
    f = request.files['file']
    f.save(f.filename)
    return '성공 여부 try except로 처리 계획'

@app.get('/item/{item}', response_class=HTMLResponse)
async def name_of_item(request : Request, item ):
    return await rs.item(request, item) 
 

# Oracle 테스트
@app.get("/test")
async def test():
    return await rs.test()


# class Item(BaseModel):
#     id: str
#     name: str | None = None
    
# # @app.post('/test/')
# # # async def test(request: Request):
# # async def test(item:Item ):
# #     return(item)
    
# #     # return await rs.do_test(id)
    
    
# @app.post('/test/')
# # async def test(request: Request):
# async def test(request: Request):
    
#     json_str = await  request.json()
    
#     print(json_str.get('id'))
#     return rs.do_test(json_str.get('id'))

# class TEST_M(BaseModel):
#     id : str


# @app.post('/test2')
# # async def test(request: Request):
# async def test(m: TEST_M):
#     # return(m.get('id'))
#     return rs.do_test(m.id )



