import streamlit as st
import os
import time
from datetime import datetime
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

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

st.markdown('<div class="main-header"><h1>🤖 Automated Blog Content Factory</h1><p>4 Specialized AI Agents | Powered by Groq (Free & Fast!) | SEO Optimized</p></div>', unsafe_allow_html=True)

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
    word_count = st.select_slider("Target Length", options=[500, 800, 1000, 1200, 1500], value=800)
with col2:
    creativity = st.slider("Creativity Level", 0.0, 1.0, 0.7)

# Groq API key
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    api_key = st.text_input("🔑 Groq API Key", type="password", 
                            help="Get free from console.groq.com")
    if not api_key:
        st.info("Please enter your Groq API key or add GROQ_API_KEY to .env file")
        st.stop()

client = Groq(api_key=api_key)

def call_groq(prompt):
    """Call Groq API with retry logic"""
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",  # Free, high quality, fast
            messages=[{"role": "user", "content": prompt}],
            temperature=creativity,
            max_tokens=2000
        )
        return response.choices[0].message.content
    except Exception as e:
        st.error(f"Error: {str(e)}")
        return None

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
            research = call_groq(f"Research the topic: '{topic}'. Provide 3 key facts and trends in 2-3 sentences.")
            
            if research:
                status.markdown("✍️ **Agent 2/4: Writing...**")
                progress.progress(50)
                draft = call_groq(f"Using this research: {research}\nWrite a {word_count}-word blog post about '{topic}'. Include an engaging headline, introduction, 3-4 body paragraphs with subheadings, and a conclusion.")
                
                if draft:
                    status.markdown("📝 **Agent 3/4: Editing...**")
                    progress.progress(75)
                    edited = call_groq(f"Edit this blog post for grammar, flow, and tone: {draft}. Fix any errors and improve readability.")
                    
                    if edited:
                        status.markdown("🎯 **Agent 4/4: SEO Optimization...**")
                        progress.progress(100)
                        final = call_groq(f"Add SEO optimization to this blog post: {edited}. Include primary keyword, secondary keywords, meta description (under 160 chars), and URL suggestion at the top.")
                        
                        if final:
                            st.markdown("---")
                            st.subheader("📄 Generated Blog Post")
                            st.markdown(final)
                            
                            # Save to file
                            os.makedirs("output", exist_ok=True)
                            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                            filename = f"output/blog_{topic.replace(' ', '_')}_{timestamp}.txt"
                            with open(filename, 'w', encoding='utf-8') as f:
                                f.write(final)
                            
                            # Download button
                            with open(filename, 'r', encoding='utf-8') as f:
                                st.download_button(
                                    label="📥 Download Blog Post",
                                    data=f.read(),
                                    file_name=f"blog_{topic.replace(' ', '_')}_{timestamp}.txt",
                                    mime="text/plain"
                                )
                            
                            st.success(f"✅ Blog generated in {time.time()-start:.1f} seconds! (Free Groq API)")
            
        except Exception as e:
            st.error(f"Error: {str(e)}")
        finally:
            progress.empty()
            status.empty()

# Sidebar with info
st.sidebar.markdown("---")
st.sidebar.subheader("⚡ Groq Free Tier")
st.sidebar.info("""
- **30 requests/minute**
- **1000+ requests/day**
- **Extremely fast** (500+ tokens/sec)
- **100% free** (no credit card)
""")

st.sidebar.markdown("---")
st.sidebar.subheader("🎯 4 AI Agents")
st.sidebar.markdown("""
1. 🔍 **Researcher** - Gathers facts & trends
2. ✍️ **Writer** - Creates engaging content
3. 📝 **Editor** - Polishes grammar & flow
4. 🎯 **SEO Analyst** - Optimizes for search
""")

st.sidebar.markdown("---")
st.sidebar.markdown("Built with ❤️ using **Groq** | 4 Specialized Agents")
