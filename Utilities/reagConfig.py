import configparser

config = configparser.RawConfigParser()
config.read("D:\\Rupali Prathamesh Pandit\\ParaBank\\Configuration\\config.ini")

class ReadConfig:

    @staticmethod
    def getURL():
        url = config.get('common info' , 'url')
        return url

    @staticmethod
    def getUsername():
        username = config.get('common info' , 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password