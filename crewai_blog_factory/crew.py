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
        print(f"\n{'='*60}")
        print(f"🚀 CREWAI BLOG FACTORY - Topic: {self.topic}")
        print(f"{'='*60}\n")
        
        # Create instances of agents
        researcher = self.agents.researcher()
        writer = self.agents.writer()
        editor = self.agents.editor()
        seo = self.agents.seo_analyst()

        # Create tasks
        research_task = self.tasks.research_task(self.topic)
        writing_task = self.tasks.writing_task(self.topic, research_task)
        editing_task = self.tasks.editing_task(writing_task)
        seo_task = self.tasks.seo_task(editing_task, self.topic)

        # Create crew with sequential process
        crew = Crew(
            agents=[researcher, writer, editor, seo],
            tasks=[research_task, writing_task, editing_task, seo_task],
            process=Process.sequential,
            verbose=True
        )

        # Execute the crew
        result = crew.kickoff()
        
        return result

    def save_output(self, result):
        """Save the blog post to a file"""
        os.makedirs("output", exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"output/crewai_{self.topic.replace(' ', '_')}_{timestamp}.txt"
        
        with open(filename, "w") as f:
            f.write(f"TOPIC: {self.topic}\n")
            f.write(f"GENERATED: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"{'='*60}\n\n")
            f.write(str(result))
        
        print(f"\n✅ Blog saved to: {filename}")
        return filename
