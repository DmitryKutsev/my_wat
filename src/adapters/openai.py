# adapters/openai_adapter.py
from langchain_openai import OpenAI
from langchain.schema import HumanMessage
from langchain.callbacks.tracers import trace  # Import the @trace decorator
from adapters.base import LLMAdapter


class OpenAIAdapter(LLMAdapter):
    def __init__(self):
        super().__init__()
        model_name = self.settings.OPENAI_DEFAULT_MODEL
        self.client = OpenAI(model=model_name, api_key=self.settings.OPENAI_API_KEY)  # type: ignore https://github.com/pydantic/pydantic/issues/9557

    @trace
    def generate(self, prompt: str) -> str:
        response = self.client.invoke([HumanMessage(content=prompt)])
        return response
