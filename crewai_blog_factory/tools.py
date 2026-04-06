from crewai_tools import BaseTool
import requests
from bs4 import BeautifulSoup
from typing import Type
from pydantic import BaseModel, Field

class WebSearchTool(BaseTool):
    name: str = "Web Search Tool"
    description: str = "Search the web for current information on a topic"
    
    def _run(self, query: str) -> str:
        """Simulate web search (in production, use a real search API)"""
        return f"Search results for: {query}\n[In production, this would return real search results]"
    
    async def _arun(self, query: str) -> str:
        return self._run(query)

class WebScraperTool(BaseTool):
    name: str = "Web Scraper"
    description: str = "Scrape content from a given URL"
    
    def _run(self, url: str) -> str:
        """Scrape content from URL"""
        try:
            response = requests.get(url, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Remove script and style elements
            for script in soup(["script", "style"]):
                script.decompose()
            
            # Get text
            text = soup.get_text()
            
            # Break into lines and remove leading/trailing space
            lines = (line.strip() for line in text.splitlines())
            # Break multi-headlines into a line each
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            # Drop blank lines
            text = '\n'.join(chunk for chunk in chunks if chunk)
            
            return text[:5000]  # Return first 5000 chars
        except Exception as e:
            return f"Error scraping URL: {str(e)}"
    
    async def _arun(self, url: str) -> str:
        return self._run(url)
