from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    DEBUG: bool = False

    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str

    @property
    def DATABASE_URL_asyncpg(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    BOT_TOKEN: str
    BOT_NAME: str
    BOT_SHORT_DESCRIPTION: str
    BOT_DESCRIPTION: str

    ADMIN_IDS: list
    SKIP_UPDATES: bool = False

    SUPABASE_API_KEY: str
    SUPABASE_URL: str
    SUPABASE_BUCKET: str
    SUPABASE_KEY: str
    SUPABASE_KEY_ACCESS: str
    SUPABASE_REGION: str
    SUPABASE_PROJECT_ID: str

    model_config = SettingsConfigDict(env_file='../.env', extra='ignore')


settings = Settings()
