from pydantic import BaseSettings

class Settings(BaseSettings):
    GOOGLE_PAGESPEED_API_KEY: str
    HOTJAR_API_KEY: str
    MARKETMUSE_API_KEY: str
    EYEQUANT_API_KEY: str
    DARKTRACE_API_KEY: str

    class Config:
        env_file = ".env"

settings = Settings()