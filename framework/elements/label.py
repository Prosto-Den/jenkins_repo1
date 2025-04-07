from .baseElement import BaseElement


class Label(BaseElement):
    def __init__(self, locator: str, name: str) -> None:
        super().__init__(locator, name)
