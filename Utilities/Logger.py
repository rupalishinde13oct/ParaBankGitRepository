import inspect
import logging


class Logger:
    @staticmethod
    def logGen():

        logger = logging.getLogger()
        file = logging.FileHandler("D:\\Rupali Prathamesh Pandit\\ParaBank\\Logs\\ParaBank_LogFile.log")
        format = logging.Formatter("%(funcName)s : %(lineno)s : %(levelno)s : %(asctime)s : %(message)s ")
        file.setFormatter(format)
        logger.addHandler(file)
        logger.setLevel(logging.INFO)
        return logger