import os
import sys
import logging
# from logging.handlers import RotatingFileHandler

logfile = os.environ.get('LOGFILE')
if logfile:
    # logging.basicConfig(level=logging.INFO, format='%(asctime)s: %(name)s: %(levelname)s: %(message)s',
    #                     datefmt='%y-%m-%d %H:%M:%S', filename=logfile)
    logger = logging.getLogger()

    # Formatter
    # formatter = logging.Formatter('%(asctime)s - %(levelname)s: [%(name)s:%(lineno)d][%(funcName)s()]: %(message)s')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s: [%(name)s:%(lineno)d]: %(message)s')
    file_handler_info = logging.FileHandler(filename=logfile, encoding='utf-8')
    # file_handler_info = logging.handlers.RotatingFileHandler(filename=logfile, maxBytes=200*1024*1024, backupCount=5, encoding='utf-8')
    file_handler_info.setFormatter(formatter)
    file_handler_info.setLevel(logging.INFO)
    logger.addHandler(file_handler_info)
    logger.setLevel(logging.INFO)
    logger.error(f'logger={logger}')
else:
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: [%(name)s:%(lineno)d]: %(message)s',
                        datefmt='%y-%m-%d %H:%M:%S', stream=sys.stdout)
    logger = logging.getLogger()
    logger.error(f'logger={logger}')

logger.error(f'logfile={logfile}')
