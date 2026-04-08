"""
Groq Adapter for CrewAI
Converts Groq API to work with CrewAI's LangChain interface
"""

from langchain.llms.base import LLM
from typing import Optional, List, Mapping, Any
import os
from groq import Groq


class GroqCrewAIAdapter(LLM):
    """Adapter to make Groq work with CrewAI's LangChain-based interface"""
    
    model: str = "llama-3.3-70b-versatile"
    temperature: float = 0.7
    client: Any = None
    
    def __init__(self, model: str = "llama-3.3-70b-versatile", temperature: float = 0.7, **kwargs):
        super().__init__(**kwargs)
        self.model = model
        self.temperature = temperature
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY not found in environment variables")
        self.client = Groq(api_key=api_key)
    
    @property
    def _llm_type(self) -> str:
        return "groq"
    
    def _call(self, prompt: str, stop: Optional[List[str]] = None, **kwargs) -> str:
        """Call Groq API with the given prompt"""
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=self.temperature,
                max_tokens=4096
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error calling Groq: {e}")
            return f"Error: {str(e)}"
    
    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        return {"model": self.model, "temperature": self.temperature}
