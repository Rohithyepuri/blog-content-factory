from crewai import Agent
from .gemini_adapter import GeminiCrewAIAdapter
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize Gemini LLM
llm = GeminiCrewAIAdapter(
    model="models/gemini-2.5-flash",
    temperature=0.7
)

class BlogAgents:
    def researcher(self):
        return Agent(
            role="Research Specialist",
            goal="Find comprehensive, accurate, and up-to-date information on the given topic",
            backstory="""You are an expert researcher with years of experience in 
            gathering information from reliable sources. You excel at finding facts, 
            statistics, and expert opinions on any topic. You provide well-structured,
            detailed research briefs.""",
            llm=llm,
            verbose=True,
            allow_delegation=False,
            max_iter=3
        )

    def writer(self):
        return Agent(
            role="Content Writer",
            goal="Transform research into engaging, well-structured blog content",
            backstory="""You are a professional blog writer known for creating 
            compelling, easy-to-read content that keeps readers engaged. You have 
            a knack for explaining complex topics simply and creating narratives 
            that flow naturally.""",
            llm=llm,
            verbose=True,
            allow_delegation=False,
            max_iter=3
        )

    def editor(self):
        return Agent(
            role="Senior Editor",
            goal="Polish and refine the blog post to ensure high quality and consistency",
            backstory="""With 10+ years of editing experience, you have an impeccable 
            eye for detail. You ensure content flows well, maintains consistent tone, 
            and is free from errors. You also verify factual accuracy and improve 
            readability.""",
            llm=llm,
            verbose=True,
            allow_delegation=True,
            max_iter=3
        )

    def seo_analyst(self):
        return Agent(
            role="SEO Specialist",
            goal="Optimize content for search engines while maintaining readability",
            backstory="""You are an SEO expert who understands search intent and 
            how to structure content for better rankings. You balance keyword 
            optimization with natural language, ensuring content ranks well while 
            remaining valuable to readers.""",
            llm=llm,
            verbose=True,
            allow_delegation=False,
            max_iter=3
        )
