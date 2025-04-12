import sys
import logging

def error_details(error,error_detail:sys):
    # it gives 3 outputes third gives us about what kind of error is occured,,in which line
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message = f"Error occurred in script [{file_name}] at line [{exc_tb.tb_lineno}] with message: [{error}]"
    return error_message

# when the error occured i call this function..
class custom_exception(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_details(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message
    
if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:
        logging.info("devided by 0 eeror ")
        raise custom_exception(e,sys)
