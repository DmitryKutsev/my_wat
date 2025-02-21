from langchain_together import Together
from langchain.schema import HumanMessage
from langchain.callbacks.tracers import trace  # Import the @trace decorator
from adapters.base import LLMAdapter


class TogetherAdapter(LLMAdapter):
    def __init__(self):
        super().__init__()
        model_name = self.settings.DEFAULT_TOGETHER_LLM
        self.client = Together(model=model_name, api_key=self.settings.TOGETHER_API_KEY)  # type: ignore https://github.com/pydantic/pydantic/issues/9557

    @trace
    def generate(self, prompt: str) -> str:
        response = self.client.invoke([HumanMessage(content=prompt)])
        return response
