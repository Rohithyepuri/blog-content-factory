from crewai import Task
from .agents import BlogAgents

agents = BlogAgents()

class BlogTasks:
    def research_task(self, topic):
        return Task(
            description=f"""
            Research the topic: "{topic}"
            
            Your research must include:
            1. KEY FACTS: Important statistics, dates, and fundamental information
            2. LATEST TRENDS: Current developments and future predictions
            3. EXPERT OPINIONS: Quotes and perspectives from thought leaders
            4. COMMON QUESTIONS: What people typically ask about this topic
            5. COMPETITOR ANALYSIS: What top-ranking articles cover
            6. SOURCES: List of authoritative sources for fact-checking
            
            Format this as a comprehensive research brief with clear sections.
            """,
            agent=agents.researcher(),
            expected_output="A detailed research brief with all required sections"
        )

    def writing_task(self, topic, research):
        return Task(
            description=f"""
            Using the research provided, write a compelling blog post about: "{topic}"
            
            Requirements:
            - HEADLINE: Create an engaging, click-worthy headline
            - INTRODUCTION: Hook the reader in the first paragraph
            - BODY: Well-structured with subheadings every 2-3 paragraphs
            - EXAMPLES: Include relevant examples and case studies
            - CONCLUSION: Strong finish with a call-to-action
            - WORD COUNT: 1500-2000 words
            - TONE: Professional yet accessible
            
            Use the research to ensure accuracy and depth.
            """,
            agent=agents.writer(),
            context=[research],
            expected_output="A complete first draft of the blog post"
        )

    def editing_task(self, draft):
        return Task(
            description=f"""
            Review and polish this blog post:
            
            {draft}
            
            EDITING CHECKLIST:
            1. GRAMMAR & SPELLING: Fix all errors
            2. CLARITY: Simplify complex sentences
            3. FLOW: Improve transitions between sections
            4. TONE: Ensure consistent voice throughout
            5. ACCURACY: Verify key facts
            6. ENGAGEMENT: Strengthen weak sections
            7. STRUCTURE: Check heading hierarchy
            
            Return the polished version with a summary of changes made.
            """,
            agent=agents.editor(),
            context=[draft],
            expected_output="A polished, error-free blog post with editorial notes"
        )

    def seo_task(self, edited_post, topic):
        return Task(
            description=f"""
            Optimize this blog post for search engines:
            
            {edited_post}
            
            SEO REQUIREMENTS:
            1. KEYWORD RESEARCH: Identify primary and 3-5 secondary keywords
            2. TITLE OPTIMIZATION: Include primary keyword naturally
            3. META DESCRIPTION: Write compelling 155-160 character description
            4. HEADING OPTIMIZATION: Include keywords in H2/H3 tags where relevant
            5. URL SLUG: Create SEO-friendly URL
            6. KEYWORD DENSITY: Maintain 1-2% without keyword stuffing
            7. IMAGE ALT TEXT: Suggest alt text for 3-5 potential images
            8. INTERNAL LINKING: Suggest related topics to link to
            
            Return the optimized post with a separate SEO recommendations section.
            """,
            agent=agents.seo_analyst(),
            context=[edited_post],
            expected_output="SEO-optimized blog post with detailed recommendations"
        )
