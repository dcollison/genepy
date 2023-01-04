from genepy.config import Config


class Logger:
    @classmethod
    def debug(cls, message):
        if Config.debug:
            print(message)
