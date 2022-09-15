from json import dumps as jsondumps
from json import loads as jsonloads
from os import environ
import logging
from httplogging import HttpHandler

# Settings -------------------------------------------------------------------------

LOGBOT_USERNAME = environ["LOGBOT_USERNAME"]
LOGBOT_PASSWORD = environ["LOGBOT_PASSWORD"]
TELEGRAM_CHATID = environ["TELEGRAM_CHATID"]

with open('config.json', 'r') as file:
	config = jsonloads(file.read())

APPNAME = config["project_name"]
LOGURL  = config["log_url"]

CMDFORMAT  = '%(levelname)s - %(message)s'
DATEFORMAT = '%y/%m/%d - %H:%M:%S'
JSONFORMAT = {
    'time'      : '%(asctime)s',
    'appname'   : '%(name)s',
    'pathname'  : '%(pathname)s',
    'line'      : '%(lineno)d',
    'loglevel'  : '%(levelname)s',
    'message'   : '%(message)s'
}

INFOFORMAT = {
    'time'      : '%(asctime)s',
    'loglevel'  : '%(levelname)s',
    'message'   : '%(message)s'
}


# Critical Handler Initialization ----------------------------------------------------

http_critical = HttpHandler(LOGURL, silent=False, level_specific=True)
http_critical.setLevel(logging.CRITICAL)

critical_format = logging.Formatter(jsondumps(JSONFORMAT), datefmt=DATEFORMAT)
http_critical.setFormatter(critical_format)

http_critical.setCredentials(LOGBOT_USERNAME, LOGBOT_PASSWORD)
http_critical.setTelegramChatId(TELEGRAM_CHATID)


# Info Handler Initialization ----------------------------------------------------

http_info = HttpHandler(LOGURL, silent=True, level_specific=True)
http_info.setLevel(logging.INFO)

info_format = logging.Formatter(jsondumps(INFOFORMAT), datefmt=DATEFORMAT)
http_info.setFormatter(info_format)

http_info.setCredentials(LOGBOT_USERNAME, LOGBOT_PASSWORD)


# Logging settings -----------------------------------

log_level = logging.INFO
logging.basicConfig(format=CMDFORMAT, datefmt=DATEFORMAT, level=log_level)


# Create logger for errors -----------------------------------

logger = logging.getLogger(APPNAME)
logger.addHandler(http_critical) 
logger.addHandler(http_info)
 
