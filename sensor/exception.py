import sys

def error_message_detail(error,error_detal:sys):

    _,_,exc_tb = error_detal.exc_info()

    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = "Error occurrred python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )


class sensorException(Exception):
    
    def __init__(self, error_message, error_detail:sys):
        """
        :param error message: error message in string format
        """
        super().__init__(error_message)

        self.error_message = error_message_detail(error_message, error_detal=error_detail)

    
    def __str__(self):

        return self.error_message
