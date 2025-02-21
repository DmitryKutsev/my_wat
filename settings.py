import yaml
from pydantic_settings import BaseSettings


class ProjectSettings(BaseSettings):
    TAVILY_API_KEY: str

    # LangChain Settings
    LANGCHAIN_API_KEY: str
    LANGCHAIN_TRACING_V2: bool
    LANGCHAIN_ENDPOINT: str
    LANGCHAIN_PROJECT: str

    # OpenAI Settings
    OPENAI_API_KEY: str
    OPENAI_DEFAULT_MODEL: str
    OPENAI_EMBEDDING_MODEL: str

    # Together API
    TOGETHER_API_KEY: str
    DEFAULT_TOGETHER_LLM: str


    @classmethod
    def from_yaml(cls, file_path: str):
        with open(file_path, "r") as file:
            yaml_data = yaml.safe_load(file)
        return cls(**yaml_data)


settings = ProjectSettings.from_yaml("config.yaml")
