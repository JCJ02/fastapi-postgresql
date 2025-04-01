from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PORT: int
    PROJECT_ENV: str
    
    # Database Configuration
    DATABASE_USERNAME: str
    DATABASE_PASSWORD: str
    DATABASE_NAME: str
    DATABASE_HOST: str
    DATABASE_PORT: str
    DATABASE_URL: str
    
    # JWT Configuration
    JWT_SECRET_KEY: str
    JWT_REFRESH_KEY: str
    JWT_EXPIRES_IN: int
    JWT_REFRESH_EXPIRES_IN: int
    
    # API Configuration
    API_KEY: str
    
    # URLs
    PORT_FORWARD_URL: str
    STAGING_URL: str

    class Config:
        env_file = ".env"

settings = Settings()