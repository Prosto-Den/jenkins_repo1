from pydantic import BaseModel


class ConfigModel(BaseModel):
    URL: str
    current_browser: str
    language: str
    delay: int
    fullscreen: bool
    incognito: bool
    load_strategy: str
    level_log: str