from framework.settings.model import ConfigModel
from framework.baseDataManipulator.BaseDataManipulator import BaseDataManipulator
import json
import os


class ConfigManipulator(BaseDataManipulator):
    __data: ConfigModel | None = None

    @classmethod
    def init(cls, file_path: str = None):
        if cls.__data is None:
            if file_path is None:
                file_path =  os.path.dirname(__file__) + '/config.json'

            with open(file_path, encoding='utf-8') as file:
                data = json.load(file)

            cls.__data = ConfigModel(**data)

    @classmethod
    def data(cls) -> ConfigModel:
        return cls.__data

    @classmethod
    def clear(cls):
        cls.__data = None

    @classmethod
    def data_as_tuple(cls) -> NotImplemented:
        return NotImplemented