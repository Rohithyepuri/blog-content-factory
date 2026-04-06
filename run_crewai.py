#!/usr/bin/env python3
import os
import sys
from dotenv import load_dotenv
from crewai_blog_factory.crew import BlogCrew

load_dotenv()

def main():
    print("\n" + "="*60)
    print("🤖 CREWAI BLOG CONTENT FACTORY")
    print("="*60)
    
    # Check for API key
    if not os.getenv("GEMINI_API_KEY"):
        print("❌ Error: GEMINI_API_KEY not found in .env file")
        print("Please add your Gemini API key to the .env file")
        sys.exit(1)
    
    # Get topic from command line or prompt
    if len(sys.argv) > 1:
        topic = " ".join(sys.argv[1:])
    else:
        topic = input("\n📝 Enter blog topic: ").strip()
    
    if not topic:
        topic = "The Future of Artificial Intelligence"
        print(f"Using default topic: {topic}")
    
    try:
        # Create and run the crew
        blog_crew = BlogCrew(topic)
        result = blog_crew.run()
        
        # Save the result
        filename = blog_crew.save_output(result)
        
        print(f"\n{'='*60}")
        print("✅ BLOG GENERATION COMPLETE!")
        print(f"📁 Output saved to: {filename}")
        print(f"{'='*60}\n")
        
    except KeyboardInterrupt:
        print("\n\n⚠️ Process interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
