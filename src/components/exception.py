
import sys
from src.components.logger import logging

import traceback
import inspect

def error_message_detail():
    exc_type, exc_value, exc_tb = sys.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno - 1  # Adjust line number to where the error occurs in the function
    error_message = f"Error occurred in Python script: {file_name}, line number: {line_number}, error message: {str(exc_value)}"
    return error_message

class CustomException(Exception):
    
    def __init__(self):
        error_message = error_message_detail()
        super().__init__(error_message)
        self.error_message = error_message

    def __str__(self):
        return self.error_message
    
