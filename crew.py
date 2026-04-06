from crewai import Crew, Process
from agents import BlogAgents
from tasks import BlogTasks
import json
from datetime import datetime
import os

class BlogCrew:
    def __init__(self, topic):
        self.topic = topic
        self.agents = BlogAgents()
        self.tasks = BlogTasks()

    def run(self):
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

        # Create crew
        crew = Crew(
            agents=[researcher, writer, editor, seo],
            tasks=[research_task, writing_task, editing_task, seo_task],
            process=Process.sequential,  # Tasks will be executed in sequence
            verbose=True
        )

        # Execute the crew
        result = crew.kickoff()
        
        return result

def save_output(content, topic):
    # Create output directory if it doesn't exist
    os.makedirs("output", exist_ok=True)
    
    # Generate filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"output/{topic.replace(' ', '_')}_{timestamp}.txt"
    
    # Save content
    with open(filename, "w") as f:
        f.write(str(content))
    
    print(f"\n✅ Blog post saved to: {filename}")
    return filename

if __name__ == "__main__":
    print("=" * 50)
    print("🤖 Automated Blog Content Factory")
    print("=" * 50)
    
    # Get topic from user
    topic = input("\n📝 Enter your blog topic: ").strip()
    
    if not topic:
        topic = "The Future of Artificial Intelligence in 2024"
        print(f"Using default topic: {topic}")
    
    print(f"\n🚀 Starting blog generation for: '{topic}'")
    print("This may take a few minutes...\n")
    
    # Run the crew
    blog_crew = BlogCrew(topic)
    result = blog_crew.run()
    
    # Save and display result
    filename = save_output(result, topic)
    
    print(f"\n🎉 Blog post generated successfully!")
    print(f"📁 Check the output folder for your blog post")
