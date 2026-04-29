from pydantic import BaseModel


class Settings(BaseModel):
    app_name: str = "Microplastic Risk Platform API"
    api_prefix: str = ""


settings = Settings()
