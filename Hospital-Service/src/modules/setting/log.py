import logging
import logging.config
import json
import os

def info_log(message):
    
    with open('./modules/setting/logging.json','rt') as file:
        config = json.load(file)

    logging.config.dictConfig(config)
    logger = logging.getLogger()

    logger.info(message)

def debug_log(message):
    
    with open('./modules/setting/logging.json','rt') as file:
        config = json.load(file)

    logging.config.dictConfig(config)
    logger = logging.getLogger()

    logger.debug(message)

def error_log(error_message):
    with open('./modules/setting/logging.json','rt') as file:
        config = json.load(file)

    logging.config.dictConfig(config)
    logger = logging.getLogger()
    
    logger.error(error_message)

# if __name__ ==  '__main__':

#     with open('logging.json','rt') as file:
#         config = json.load(file)

#     logging.config.dictConfig(config)
#     logger = logging.getLogger()

#     logger.info("test!!!")