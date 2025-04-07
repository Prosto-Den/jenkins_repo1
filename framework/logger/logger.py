import logging as log


class Logger:
    instance: log.Logger = None

    @classmethod
    def init(cls, name: str, filename: str, level: str) -> None:
        if cls.instance is None:
            cls.instance = log.getLogger(name)
            log.basicConfig(filename=filename, encoding='utf-8', filemode='w', level=level, force = True)
