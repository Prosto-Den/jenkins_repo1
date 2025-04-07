from framework.baseDataManipulator.BaseDataManipulator import BaseDataManipulator
from .models import UserDataModel, AlertDataModel, ProgressBarDataModel
import json
import os


class UserDataGenerator:
    @staticmethod
    def get_user() -> UserDataModel:
        data_path = os.path.dirname(__file__)
        with open(f"{data_path}/user_data.json") as file:
            data = dict(json.load(file))

        for value in data.values():
            yield UserDataModel(**value)


class AlertDataManipulator(BaseDataManipulator):
    __data: AlertDataModel | None = None

    @classmethod
    def init(cls):
        if cls.__data is None:
            data_path = os.path.dirname(__file__)
            with open(f'{data_path}/alerts_data.json', encoding='utf-8') as file:
                data = json.load(file)

            cls.__data = AlertDataModel(**data)

    @classmethod
    def data_as_tuple(cls) -> tuple:
        return cls.__data.as_tuple()

    @classmethod
    def data(cls) -> AlertDataModel:
        return cls.__data

    @classmethod
    def clear(cls):
        cls.__data = None


class ProgressBarDataManipulator(BaseDataManipulator):
    __data: ProgressBarDataModel | None = None

    @classmethod
    def init(cls):
        if cls.__data is None:
            data_path = os.path.dirname(__file__)
            with open(f'{data_path}/progress_bar_data.json', encoding='utf-8') as file:
                data = json.load(file)

            cls.__data = ProgressBarDataModel(**data)

    @classmethod
    def data(cls) -> ProgressBarDataModel:
        return cls.__data

    @classmethod
    def data_as_tuple(cls) -> tuple:
        return cls.__data.as_tuple()

    @classmethod
    def clear(cls):
        cls.__data = None