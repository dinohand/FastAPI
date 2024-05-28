# from main import app 
from fastapi import FastAPI
#  import uvicorn
from common.config_manager import Config_Manager
from common.log_manager import Log_Manager
from biz.route_service import Route_Service

logger = Log_Manager().getLogger("MAIN")

cm = Config_Manager() ## config manager
rs = Route_Service()


app = FastAPI()
# app.include_router(static.router)

logger.info("App is started !")


@app.get('/')
@app.post('/')
def hello():
    return 'Hello'

@app.get('/health')
async def healthcheck():
    return await rs.heathCheck()
    
    # return {'message':'health check ok', 'code': 200}

## shutdown
# @app.route("/shutdown", methods=["POST"])
@app.post('/shutdown')
def shutdown():
    logger.fatal("Dying...")
