import streamlit as st
import os
import sys

# Better import handling with error messages
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    st.warning("python-dotenv not found, using environment variables directly")

try:
    from google import genai
    from google.genai import types
except ImportError:
    st.error("google-genai not installed. Please check requirements.txt")
    st.stop()

import time
from datetime import datetime
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(
    page_title="Blog Factory | AI Content Generation",
    page_icon="🤖",
    layout="wide"
)

st.markdown("""
<style>
    .stApp { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }
    .main-header { text-align: center; padding: 2rem; background: rgba(255,255,255,0.95); border-radius: 20px; margin-bottom: 2rem; }
    .agent-card { text-align: center; padding: 1rem; background: white; border-radius: 10px; margin: 0.5rem; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header"><h1>🤖 Automated Blog Content Factory</h1><p>4 Specialized AI Agents | 45-60 Second Generation | SEO Optimized</p></div>', unsafe_allow_html=True)

# Display agents
col1, col2, col3, col4 = st.columns(4)
agents = [("🔍", "Researcher", "Gathers information"), ("✍️", "Writer", "Creates content"), ("📝", "Editor", "Polishes text"), ("🎯", "SEO", "Optimizes search")]
for col, (emoji, name, desc) in zip([col1, col2, col3, col4], agents):
    with col:
        st.markdown(f'<div class="agent-card"><div style="font-size:40px">{emoji}</div><div style="font-weight:bold">{name}</div><div style="font-size:12px">{desc}</div></div>', unsafe_allow_html=True)

# Input
topic = st.text_input("📝 Blog Topic", placeholder="e.g., The Future of Artificial Intelligence")
col1, col2 = st.columns(2)
with col1:
    word_count = st.select_slider("Target Length", options=[500, 1000, 1500, 2000], value=1500)
with col2:
    creativity = st.slider("Creativity Level", 0.0, 1.0, 0.7)

# Get API key from secrets (Streamlit Cloud) or .env (local)
api_key = None

# Try different methods to get API key
try:
    api_key = st.secrets.get("GEMINI_API_KEY")
except:
    pass

if not api_key:
    api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("❌ GEMINI_API_KEY not found! Please add it to Streamlit Secrets or .env file")
    st.info("""
    **For Streamlit Cloud:**
    1. Go to your app dashboard
    2. Click Settings → Secrets
    3. Add: `GEMINI_API_KEY = "your_key_here"`
    
    **For Local:**
    Create a `.env` file with: `GEMINI_API_KEY=your_key_here`
    """)
    st.stop()

try:
    client = genai.Client(api_key=api_key)
except Exception as e:
    st.error(f"Failed to initialize Gemini client: {e}")
    st.stop()

if st.button("🚀 Generate Blog Post", type="primary", use_container_width=True):
    if not topic:
        st.error("Please enter a topic!")
    else:
        progress = st.progress(0)
        status = st.empty()
        start = time.time()
        
        try:
            status.markdown("🔍 **Agent 1/4: Researching...**")
            progress.progress(25)
            r = client.models.generate_content(
                model="gemini-2.5-flash", 
                contents=f"Research topic: {topic}. Provide key facts, statistics, and trends.",
                config=types.GenerateContentConfig(temperature=creativity)
            )
            research = r.text
            
            status.markdown("✍️ **Agent 2/4: Writing...**")
            progress.progress(50)
            w = client.models.generate_content(
                model="gemini-2.5-flash", 
                contents=f"Using this research: {research}\nWrite a {word_count}-word blog post about '{topic}'. Include headline, introduction, body with subheadings, and conclusion.",
                config=types.GenerateContentConfig(temperature=creativity)
            )
            draft = w.text
            
            status.markdown("📝 **Agent 3/4: Editing...**")
            progress.progress(75)
            e = client.models.generate_content(
                model="gemini-2.5-flash", 
                contents=f"Edit this blog post for grammar, flow, and tone: {draft}",
                config=types.GenerateContentConfig(temperature=creativity)
            )
            edited = e.text
            
            status.markdown("🎯 **Agent 4/4: SEO Optimization...**")
            progress.progress(100)
            s = client.models.generate_content(
                model="gemini-2.5-flash", 
                contents=f"Add SEO optimization (keywords, meta description, URL suggestions) to this blog post: {edited}",
                config=types.GenerateContentConfig(temperature=creativity)
            )
            final = s.text
            
            st.markdown("---")
            st.subheader("📄 Generated Blog Post")
            st.markdown(final)
            
            # Save option
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            st.download_button(
                label="📥 Download Blog Post",
                data=final,
                file_name=f"blog_{topic.replace(' ', '_')}_{timestamp}.txt",
                mime="text/plain"
            )
            
            st.success(f"✅ Blog generated in {time.time()-start:.1f} seconds!")
            
        except Exception as e:
            st.error(f"Error during generation: {str(e)}")
        finally:
            progress.empty()
            status.empty()

st.markdown("---")
st.markdown("Built with ❤️ using Google Gemini AI | 4 Specialized Agents")
