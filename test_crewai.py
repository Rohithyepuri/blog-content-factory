#!/usr/bin/env python3
import os
from dotenv import load_dotenv
import google.generativeai as genai

def test_setup():
    print("🔍 Testing CrewAI Blog Factory Setup...")
    
    # Check .env file
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("❌ GEMINI_API_KEY not found in .env file")
        return False
    print("✅ API key found")
    
    # Test Gemini connection
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('models/gemini-2.5-flash')
        response = model.generate_content("Say 'Hello' in one word")
        print(f"✅ Gemini connection working: {response.text}")
    except Exception as e:
        print(f"❌ Gemini connection failed: {e}")
        return False
    
    # Test imports
    try:
        from crewai_blog_factory import BlogCrew, BlogAgents, BlogTasks
        print("✅ CrewAI modules imported successfully")
    except Exception as e:
        print(f"❌ Import failed: {e}")
        return False
    
    print("\n✅ All systems ready! You can now run: python run_crewai.py")
    return True

if __name__ == "__main__":
    test_setup()
