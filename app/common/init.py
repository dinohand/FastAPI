from app.common.log_manager import Log_Manager
import os

logger = Log_Manager().getLogger("Init")

def do_1st():
    dirs = ['NAS/REF' , 
            'NAS/CODE']
    cwd = os.getcwd()
    
    # 필수 디렉토리 생성
    for dir in dirs :
        new_dir = cwd + "/" + dir
        if os.path.isdir(new_dir) ==False: 
            os.makedirs(new_dir)
            logger.info(f'{new_dir} folder is created')