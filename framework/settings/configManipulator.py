from framework.settings.model import ConfigModel
from framework.baseDataManipulator.BaseDataManipulator import BaseDataManipulator
import json
import os


class ConfigManipulator(BaseDataManipulator):
    __data: ConfigModel | None = None

    @classmethod
    def init(cls, file_path: str = None):
        if cls.__data is None:
            file_path = os.path.dirname(__file__) + '/config.json' if file_path is None else file_path
            data = cls.__read_config(file_path)
            cls.__data = ConfigModel(**data)

    @staticmethod
    def __read_config(file_path: str) -> dict:
        if (env_config := os.environ.get('config')) is not None:
            return json.loads(env_config)

        with open(file_path, encoding='utf-8') as file:
            result: dict = json.load(file)

        for key in result.keys():
            if (env_var := os.environ.get(key)) is not None:
                result[key] = env_var

        return result

    @classmethod
    def data(cls) -> ConfigModel:
        return cls.__data

    @classmethod
    def clear(cls):
        cls.__data = None

    @classmethod
    def data_as_tuple(cls) -> NotImplemented:
        return NotImplemented
