from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Sales API"
    app_description: str = "API para gerenciamento de vendas, vendedores e metas."
    app_about: str = "Esta API foi desenvolvida para fins de demonstração e aprendizado."
    db_url: str = "sqlite:///./sales.db"
    bearer_token: str = "changeme"
    debug: bool = False

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
