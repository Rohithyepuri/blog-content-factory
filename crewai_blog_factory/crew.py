from crewai import Crew, Process
from .agents import BlogAgents
from .tasks import BlogTasks
from datetime import datetime
import os

class BlogCrew:
    def __init__(self, topic):
        self.topic = topic
        self.agents = BlogAgents()
        self.tasks = BlogTasks()

    def run(self):
        researcher = self.agents.researcher()
        writer = self.agents.writer()
        editor = self.agents.editor()
        seo = self.agents.seo_analyst()

        research_task = self.tasks.research_task(self.topic)
        writing_task = self.tasks.writing_task(self.topic, research_task)
        editing_task = self.tasks.editing_task(writing_task)
        seo_task = self.tasks.seo_task(editing_task, self.topic)

        crew = Crew(
            agents=[researcher, writer, editor, seo],
            tasks=[research_task, writing_task, editing_task, seo_task],
            process=Process.sequential,
            verbose=True
        )
        return crew.kickoff()

    def save_output(self, result):
        os.makedirs("output", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"output/crewai_groq_{self.topic.replace(' ', '_')}_{timestamp}.txt"
        with open(filename, "w") as f:
            f.write(str(result))
        return filename
