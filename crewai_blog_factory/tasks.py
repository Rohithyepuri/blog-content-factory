from crewai import Task
from .agents import BlogAgents

agents = BlogAgents()

class BlogTasks:
    def research_task(self, topic):
        return Task(
            description=f"Research topic: '{topic}'. Include key facts, trends, expert opinions.",
            agent=agents.researcher(),
            expected_output="Detailed research brief"
        )

    def writing_task(self, topic, research):
        return Task(
            description=f"Write blog post about '{topic}' using research. Include headline, intro, body, conclusion.",
            agent=agents.writer(),
            context=[research],
            expected_output="Complete blog draft"
        )

    def editing_task(self, draft):
        return Task(
            description=f"Edit blog post for grammar, flow, tone: {draft}",
            agent=agents.editor(),
            context=[draft],
            expected_output="Polished blog post"
        )

    def seo_task(self, edited_post, topic):
        return Task(
            description=f"Add SEO optimization to blog post. Include keywords, meta description.",
            agent=agents.seo_analyst(),
            context=[edited_post],
            expected_output="SEO-optimized blog post"
        )
