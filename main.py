# from main import app 
from fastapi import FastAPI
from fastapi import Response, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

#  import uvicorn
from common.config_manager import Config_Manager
from common.log_manager import Log_Manager
from biz.route_service import Route_Service

logger = Log_Manager().getLogger("MAIN")

cm = Config_Manager() ## config manager
rs = Route_Service()

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
            icense_info={
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
templates = Jinja2Templates(directory="static")
# app.include_router(static.router)

#--------------------------
# @app.get('/')
# def root():
#     return rs.root()

@app.get('/',  response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html", context={} 
    )
async def check_health():
    return await rs.heathCheck()
    
    # return {'message':'health check ok', 'code': 200}

## shutdown
# @app.route("/shutdown", methods=["POST"])
@app.post('/shutdown')
def shutdown():
    logger.fatal("Dying...")

@app.post('/fileupload')
async def upload():
    f = request.files['file']
    f.save(f.filename)
    return '성공 여부 try except로 처리 계획'

@app.get('/item/{item}', response_class=HTMLResponse)
async def name_of_item(request : Request, item ):
    return await rs.item(request, item) 
 



