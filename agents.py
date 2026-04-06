from crewai import Agent
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize LLM (OpenAI or local)
llm = ChatOpenAI(
    model=os.getenv("OPENAI_MODEL_NAME", "gpt-4"),
    temperature=0.7,
    api_key=os.getenv("OPENAI_API_KEY")
)

class BlogAgents:
    def researcher(self):
        return Agent(
            role="Research Specialist",
            goal="Find comprehensive, accurate, and up-to-date information on the given topic",
            backstory="""You are an expert researcher with years of experience in 
            gathering information from reliable sources. You excel at finding facts, 
            statistics, and expert opinions on any topic.""",
            tools=[],  # Add search tools here if needed
            llm=llm,
            verbose=True,
            allow_delegation=False
        )

    def writer(self):
        return Agent(
            role="Content Writer",
            goal="Transform research into engaging, well-structured blog content",
            backstory="""You are a professional blog writer known for creating 
            compelling, easy-to-read content that keeps readers engaged from start 
            to finish. You have a knack for explaining complex topics simply.""",
            tools=[],
            llm=llm,
            verbose=True,
            allow_delegation=False
        )

    def editor(self):
        return Agent(
            role="Senior Editor",
            goal="Polish and refine the blog post to ensure high quality and consistency",
            backstory="""With 10+ years of editing experience, you have an impeccable 
            eye for detail. You ensure the content flows well, maintains consistent 
            tone, and is free from errors.""",
            tools=[],
            llm=llm,
            verbose=True,
            allow_delegation=True
        )

    def seo_analyst(self):
        return Agent(
            role="SEO Specialist",
            goal="Optimize content for search engines while maintaining readability",
            backstory="""You are an SEO expert who knows how to balance keyword 
            optimization with natural language. You understand search intent and 
            how to structure content for better rankings.""",
            tools=[],
            llm=llm,
            verbose=True,
            allow_delegation=False
        )
