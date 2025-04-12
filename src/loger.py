# this is used for that we can console the errors
import logging
import os
from datetime import datetime

Log_FILE=F"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",Log_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,Log_FILE)
logging.basicConfig(
    # give the file name where you want to save it...
    filename=LOG_FILE_PATH,
    format="[%(asctime)s]%(lineno)d%(name)s -%(levelname)s -%(message)s",
    level=logging.INFO

)

if __name__=="__main__":
    logging.info("loggging is started : ")