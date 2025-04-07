from .baseElement import BaseElement


class Button(BaseElement):
    def __init__(self, locator: str, name: str) -> None:
        super().__init__(locator, name)