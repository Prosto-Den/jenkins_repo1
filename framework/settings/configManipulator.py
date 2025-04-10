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
            cls.__read_env_var(data)
            cls.__data = ConfigModel(**data)

    @staticmethod
    def __read_env_var(data: dict) -> None:
        if (env_config := os.environ.get('config')) is not None:
            data = json.loads(env_config)
            return

        for key in data.keys():
            if (env_var := os.environ.get(key)) is not None:
                data[key] = env_var

    @classmethod
    def data(cls) -> ConfigModel:
        return cls.__data

    @classmethod
    def clear(cls):
        cls.__data = None

    @classmethod
    def data_as_tuple(cls) -> NotImplemented:
        return NotImplemented
