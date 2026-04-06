import google.generativeai as genai
from langchain.llms.base import LLM
from typing import Optional, List, Mapping, Any
import os

class GeminiCrewAIAdapter(LLM):
    """Adapter to make Gemini work with CrewAI's LangChain-based interface"""
    
    model: str = "models/gemini-2.5-flash"
    temperature: float = 0.7
    client: Any = None
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.client = genai.GenerativeModel(self.model)
    
    @property
    def _llm_type(self) -> str:
        return "gemini"
    
    def _call(self, prompt: str, stop: Optional[List[str]] = None, **kwargs) -> str:
        """Call Gemini API with the given prompt"""
        try:
            response = self.client.generate_content(
                prompt,
                generation_config={
                    "temperature": self.temperature,
                    "max_output_tokens": 4096,
                }
            )
            return response.text
        except Exception as e:
            print(f"Error calling Gemini: {e}")
            return f"Error: {str(e)}"
    
    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        return {"model": self.model, "temperature": self.temperature}
