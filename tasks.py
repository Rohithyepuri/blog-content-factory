from crewai import Task
from agents import BlogAgents

agents = BlogAgents()

class BlogTasks:
    def research_task(self, topic):
        return Task(
            description=f"""
            Research the topic: "{topic}"
            
            Your research should include:
            1. Key facts and statistics
            2. Latest trends and developments
            3. Expert opinions and quotes
            4. Common questions people have about this topic
            5. Competitor analysis (what are top-ranking articles covering)
            
            Compile this into a comprehensive research brief.
            """,
            agent=agents.researcher(),
            expected_output="A detailed research brief with key findings and sources"
        )

    def writing_task(self, topic, research):
        return Task(
            description=f"""
            Using the research provided, write a compelling blog post about: "{topic}"
            
            Requirements:
            - Engaging headline
            - Strong introduction that hooks the reader
            - Well-structured body with subheadings
            - Conclusion with call-to-action
            - Word count: 1500-2000 words
            - Include placeholders for images
            """,
            agent=agents.writer(),
            context=[research],
            expected_output="A complete first draft of the blog post"
        )

    def editing_task(self, draft):
        return Task(
            description="""
            Review and polish the blog post draft:
            
            1. Check for grammatical errors and typos
            2. Improve sentence flow and readability
            3. Ensure consistent tone and voice
            4. Verify factual accuracy
            5. Suggest improvements for engagement
            6. Check structure and formatting
            
            Provide the edited version with track changes.
            """,
            agent=agents.editor(),
            context=[draft],
            expected_output="A polished, error-free blog post with editorial notes"
        )

    def seo_task(self, edited_post, topic):
        return Task(
            description=f"""
            Optimize this blog post for SEO:
            
            1. Research and suggest primary and secondary keywords
            2. Optimize title and headings with keywords
            3. Suggest meta description
            4. Ensure proper keyword density (1-2%)
            5. Add internal/external linking suggestions
            6. Create SEO-friendly URL structure
            7. Suggest image alt text
            """,
            agent=agents.seo_analyst(),
            context=[edited_post],
            expected_output="SEO-optimized blog post with optimization notes"
        )
