# adapters/base.py
import os

from abc import ABC, abstractmethod
from settings import settings


# Enable LangChain Tracing (requires LangSmith API key)
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = settings.LANGCHAIN_API_KEY

class LLMAdapter(ABC):
    """Abstract Base Class for LLM Adapters with LangSmith Tracing"""

    def __init__(self):
        self.settings = settings

    @abstractmethod
    def generate(self, prompt: str) -> str:
        """Generate response from LLM"""
        pass