from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    # Websocket server
    WS_SERVER_HOST: str = Field(default="localhost")
    WS_SERVER_PORT: int = Field(default=8000)

    # Joystick limit values
    JS_INPUT_MIN: int = Field(default=-1000)
    JS_INPUT_MAX: int = Field(default=1000)
    JS_OUTPUT_MIN: int = Field(default=-32768)
    JS_OUTPUT_MAX: int = Field(default=32767)


settings = Settings()
