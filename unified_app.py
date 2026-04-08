import streamlit as st
import os
import time
import sys
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="Blog Factory | Groq + CrewAI",
    page_icon="🤖",
    layout="wide"
)

st.markdown("""
<style>
    .stApp { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }
    .main-header { text-align: center; padding: 2rem; background: rgba(255,255,255,0.95); border-radius: 20px; margin-bottom: 2rem; }
    .agent-card { text-align: center; padding: 1rem; background: white; border-radius: 10px; margin: 0.5rem; transition: transform 0.3s; }
    .agent-card:hover { transform: translateY(-5px); }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header"><h1>🤖 Automated Blog Content Factory</h1><p>4 Specialized AI Agents | Powered by Groq</p></div>', unsafe_allow_html=True)

# Display agents
col1, col2, col3, col4 = st.columns(4)
agents = [("🔍", "Researcher", "Gathers information"), ("✍️", "Writer", "Creates content"), ("📝", "Editor", "Polishes text"), ("🎯", "SEO", "Optimizes search")]
for col, (emoji, name, desc) in zip([col1, col2, col3, col4], agents):
    with col:
        st.markdown(f'<div class="agent-card"><div style="font-size:40px">{emoji}</div><div style="font-weight:bold">{name}</div><div style="font-size:12px">{desc}</div></div>', unsafe_allow_html=True)

# Sidebar - Version Selection
st.sidebar.markdown("## ⚙️ Configuration")

version = st.sidebar.radio(
    "Select AI Engine",
    ["🚀 Groq Direct (Fast & Free)", "🤖 CrewAI (Multi-Agent Framework)"],
    help="Groq Direct: 30 req/min, 500+ tokens/sec\nCrewAI: Full multi-agent orchestration"
)

if "Direct" in version:
    st.sidebar.info("⚡ **Groq Direct Mode**\n- 30 requests/minute\n- 500+ tokens/second\n- 100% free")
else:
    st.sidebar.info("🤖 **CrewAI Mode**\n- Full multi-agent orchestration\n- Role delegation\n- Sequential pipeline")

# API Key
api_key = st.sidebar.text_input(
    "🔑 GROQ_API_KEY",
    type="password",
    help="Get from console.groq.com",
    value=os.getenv("GROQ_API_KEY", "")
)

if not api_key:
    st.sidebar.warning("Please enter your GROQ_API_KEY")
    st.stop()

os.environ["GROQ_API_KEY"] = api_key

# Model selection
model_options = {
    "llama-3.3-70b-versatile": "🚀 Llama 3.3 70B (Best Quality)",
    "llama-3.1-8b-instant": "⚡ Llama 3.1 8B (Fastest)",
    "mixtral-8x7b-32768": "🧠 Mixtral 8x7B (Long Context)"
}
selected_model = st.sidebar.selectbox("🤖 Model", options=list(model_options.keys()), format_func=lambda x: model_options[x])

# Input section
st.markdown("---")
topic = st.text_input("📝 Blog Topic", placeholder="e.g., The Future of Artificial Intelligence")

col1, col2 = st.columns(2)
with col1:
    word_count = st.select_slider("Target Length", options=[500, 800, 1000, 1200, 1500], value=800)
with col2:
    creativity = st.slider("Creativity Level", 0.0, 1.0, 0.7, 0.1)

def call_groq_direct(prompt):
    """Direct Groq API call"""
    try:
        from groq import Groq
        client = Groq(api_key=api_key)
        response = client.chat.completions.create(
            model=selected_model,
            messages=[{"role": "user", "content": prompt}],
            temperature=creativity,
            max_tokens=2000
        )
        return response.choices[0].message.content
    except Exception as e:
        st.error(f"Groq Error: {str(e)}")
        return None

def call_crewai(topic):
    """Run CrewAI with Groq"""
    try:
        sys.path.insert(0, os.getcwd())
        from crewai_blog_factory.crew import BlogCrew
        blog_crew = BlogCrew(topic)
        result = blog_crew.run()
        return str(result)
    except Exception as e:
        st.error(f"CrewAI Error: {str(e)}")
        return None

if st.button("🚀 Generate Blog Post", type="primary", use_container_width=True):
    if not topic:
        st.error("Please enter a topic!")
    else:
        progress = st.progress(0)
        status = st.empty()
        start = time.time()
        
        try:
            if "Direct" in version:
                # Groq Direct Mode
                status.markdown("🔍 **Agent 1/4: Researching...**")
                progress.progress(25)
                research = call_groq_direct(f"Research the topic: '{topic}'. Provide 3 key facts and trends in 2-3 sentences.")
                
                if research:
                    status.markdown("✍️ **Agent 2/4: Writing...**")
                    progress.progress(50)
                    draft = call_groq_direct(f"Using: {research}\nWrite {word_count}-word blog on '{topic}'. Include headline, intro, body, conclusion.")
                    
                    if draft:
                        status.markdown("📝 **Agent 3/4: Editing...**")
                        progress.progress(75)
                        edited = call_groq_direct(f"Edit for grammar, flow: {draft}")
                        
                        if edited:
                            status.markdown("🎯 **Agent 4/4: SEO...**")
                            progress.progress(100)
                            final = call_groq_direct(f"Add SEO (keywords, meta description): {edited}")
                            final_content = final
                else:
                    final_content = None
            else:
                # CrewAI Mode
                status.markdown("🤖 **Running CrewAI Multi-Agent System...**")
                status.markdown("🔍 **Agent 1/4: Researcher working...**")
                progress.progress(25)
                status.markdown("✍️ **Agent 2/4: Writer working...**")
                progress.progress(50)
                status.markdown("📝 **Agent 3/4: Editor working...**")
                progress.progress(75)
                status.markdown("🎯 **Agent 4/4: SEO working...**")
                progress.progress(100)
                final_content = call_crewai(topic)
            
            if final_content:
                st.markdown("---")
                st.subheader("📄 Generated Blog Post")
                st.markdown(final_content)
                
                os.makedirs("output", exist_ok=True)
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                version_tag = "groq" if "Direct" in version else "crewai"
                filename = f"output/blog_{version_tag}_{topic.replace(' ', '_')}_{timestamp}.txt"
                
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(f"Version: {version}\n")
                    f.write(f"Topic: {topic}\n")
                    f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                    f.write("="*60 + "\n\n")
                    f.write(final_content)
                
                with open(filename, 'r', encoding='utf-8') as f:
                    st.download_button("📥 Download Blog", f.read(), file_name=f"blog_{timestamp}.txt", mime="text/plain")
                
                st.success(f"✅ Generated in {time.time()-start:.1f}s using {version}")
            
        except Exception as e:
            st.error(f"Error: {str(e)}")
        finally:
            progress.empty()
            status.empty()

st.sidebar.markdown("---")
st.sidebar.subheader("⚡ Groq Free Tier")
st.sidebar.info("30 req/min | 1000+ req/day | 500+ tokens/sec | FREE")

st.sidebar.markdown("---")
st.sidebar.subheader("🎯 4 AI Agents")
st.sidebar.markdown("🔍 Researcher | ✍️ Writer | 📝 Editor | 🎯 SEO")

st.sidebar.markdown("---")
st.sidebar.markdown("Built with ❤️ using **Groq + CrewAI**")
