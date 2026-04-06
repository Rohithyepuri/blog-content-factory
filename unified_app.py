import streamlit as st
from dotenv import load_dotenv
import os
import time
from datetime import datetime
import plotly.graph_objects as go
import pandas as pd

# NEW SDK IMPORT
from google import genai
from google.genai import types

load_dotenv()

# Page config
st.set_page_config(
    page_title="Blog Factory - AI Content Generation",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Automated Blog Content Factory")
st.markdown("4 Specialized AI Agents | 45-60 Second Generation | SEO Optimized")

# Get API key
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    st.error("❌ GEMINI_API_KEY not found! Please add to .env file")
    st.stop()

# Initialize Gemini client
client = genai.Client(api_key=api_key)

# Input section
topic = st.text_input("📝 Blog Topic", placeholder="e.g., The Future of Artificial Intelligence")

col1, col2 = st.columns(2)
with col1:
    word_count = st.select_slider("Target Length", options=[500, 1000, 1500, 2000], value=1500)
with col2:
    creativity = st.slider("Creativity Level", 0.0, 1.0, 0.7)

selected_model = st.selectbox("AI Model", ["gemini-2.5-flash", "gemini-2.5-pro", "gemini-2.0-flash"])

if st.button("🚀 Generate Blog Post", type="primary"):
    if not topic:
        st.error("Please enter a topic!")
    else:
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        try:
            # Agent 1: Research
            status_text.markdown("🔍 **Agent 1/4: Researching...**")
            progress_bar.progress(25)
            
            research_response = client.models.generate_content(
                model=selected_model,
                contents=f"You are an expert researcher. Research the topic: '{topic}'. Provide key facts, statistics, and trends.",
                config=types.GenerateContentConfig(temperature=creativity)
            )
            research = research_response.text
            
            # Agent 2: Write
            status_text.markdown("✍️ **Agent 2/4: Writing...**")
            progress_bar.progress(50)
            
            write_response = client.models.generate_content(
                model=selected_model,
                contents=f"Using this research: {research}\nWrite a {word_count}-word blog post about '{topic}'. Include headline, introduction, body, and conclusion.",
                config=types.GenerateContentConfig(temperature=creativity)
            )
            draft = write_response.text
            
            # Agent 3: Edit
            status_text.markdown("📝 **Agent 3/4: Editing...**")
            progress_bar.progress(75)
            
            edit_response = client.models.generate_content(
                model=selected_model,
                contents=f"Edit this blog post for grammar, flow, and tone: {draft}",
                config=types.GenerateContentConfig(temperature=creativity)
            )
            edited = edit_response.text
            
            # Agent 4: SEO
            status_text.markdown("🎯 **Agent 4/4: SEO Optimization...**")
            progress_bar.progress(100)
            
            seo_response = client.models.generate_content(
                model=selected_model,
                contents=f"Add SEO optimization (keywords, meta description) to: {edited}",
                config=types.GenerateContentConfig(temperature=creativity)
            )
            final = seo_response.text
            
            # Display result
            status_text.markdown("✅ **Blog Generation Complete!**")
            st.markdown("---")
            st.subheader("📄 Generated Blog Post")
            st.markdown(final)
            
            # Save output
            os.makedirs("output", exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"output/blog_{topic.replace(' ', '_')}_{timestamp}.txt"
            with open(filename, 'w') as f:
                f.write(final)
            st.success(f"✅ Saved to: {filename}")
            
        except Exception as e:
            st.error(f"Error: {str(e)}")
        
        progress_bar.empty()
        status_text.empty()

st.markdown("---")
st.markdown("Built with Google Gemini AI | 4 Specialized Agents")
