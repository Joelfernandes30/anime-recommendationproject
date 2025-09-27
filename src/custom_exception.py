import sys
import traceback

class CustomException(Exception):
    def __init__(self, error_message, error_detail):
        super().__init__(error_message)
        self.error_message = self.get_detailed_error_message(error_message)

    @staticmethod
    def get_detailed_error_message(error_message):
        exc_type, exc_value, exc_tb = sys.exc_info()  # ✅ correct way
        if exc_tb is not None:
            file_name = exc_tb.tb_frame.f_code.co_filename
            line_number = exc_tb.tb_lineno
            return (f"Error occurred in script: [{file_name}] at line number: [{line_number}] "
                    f"with message: [{error_message}]")
        else:
            return f"Error: [{error_message}] (No traceback available)"

    def __str__(self):
        return self.error_message