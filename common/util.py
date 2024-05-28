from common.log_manager import Log_Manager

def file_save(file_name):
    logger = Log_Manager().getLogger('FILE')
    try:
        fs.save(file_name)
        logger.info('파일이 저장디었습니다')
        return "ok"
    except Exception as e:
        logger.error(e)
        return "fail"