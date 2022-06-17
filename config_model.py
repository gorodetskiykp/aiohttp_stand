from pydantic import BaseModel


class WebAppConfig(BaseModel):
    host: str = '127.0.0.1'
    port: int = 8080


class MainConfig(BaseModel):
    app: WebAppConfig