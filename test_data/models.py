from pydantic import BaseModel


class UserDataModel(BaseModel):
    first_name: str
    last_name: str
    email: str
    age: int
    salary: int
    department: str

    def as_tuple(self) -> tuple:
        return tuple(value for value in self.model_dump().values())


class AlertDataModel(BaseModel):
    is_accept: bool
    message: str

    def as_tuple(self):
        return self.is_accept, self.message


class ProgressBarDataModel(BaseModel):
    age: int

    def as_tuple(self):
        return (self.age, )