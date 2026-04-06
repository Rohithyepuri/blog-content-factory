
# 🤖 Automated Blog Content Factory

**4 Specialized AI Agents | 45-60 Second Generation | SEO Optimized**

## Overview
Multi-Agent AI system that generates high-quality, SEO-optimized blog posts using 4 specialized agents working in sequence.

## Agents
- 🔍 **Researcher** - Gathers facts, statistics, expert opinions
- ✍️ **Writer** - Creates engaging blog content
- 📝 **Editor** - Polishes grammar and flow
- 🎯 **SEO Analyst** - Optimizes for search engines


## 📁 Project Structure

```
blog-content-factory/
│
├── 📄 unified_app.py              # MAIN APPLICATION - Streamlit UI with 4 agents
├── 📄 requirements.txt             # Python dependencies
├── 📄 .env.example                 # API key template (copy to .env)
├── 📄 .gitignore                   # Git ignore rules
├── 📄 LICENSE                      # MIT License
├── 📄 README.md                    # This documentation
│
├── 📁 output/                      # Generated blog posts storage
│   ├── .gitkeep                    # Keeps directory in git
│   └── blog_*.txt                  # Your generated blogs (gitignored)
│
└── 📁 .streamlit/                  # Streamlit configuration
    └── config.toml                 # UI theme & server settings
```

## 📋 File Descriptions

| File | Lines | Purpose |
|------|-------|---------|
| **unified_app.py** | ~250 | Main application with 4 agents, Streamlit UI |
| **requirements.txt** | 5 | Python package dependencies |
| **.env.example** | 3 | Template for API key configuration |
| **.gitignore** | 15 | Prevents committing sensitive files |
| **LICENSE** | 21 | MIT open source license |
| **README.md** | ~150 | Complete project documentation |

## 🔄 Data Flow

```
User Input (Topic)
       │
       ▼
┌──────────────┐
│ Agent 1      │
│ RESEARCHER   │ ──► Research Brief
└──────────────┘
       │
       ▼
┌──────────────┐
│ Agent 2      │
│ WRITER       │ ──► Blog Draft
└──────────────┘
       │
       ▼
┌──────────────┐
│ Agent 3      │
│ EDITOR       │ ──► Polished Post
└──────────────┘
       │
       ▼
┌──────────────┐
│ Agent 4      │
│ SEO ANALYST  │ ──► SEO-Optimized Blog
└──────────────┘
       │
       ▼
┌──────────────┐
│   OUTPUT     │
│  *.txt file  │
└──────────────┘
```

## 🧠 Agent Responsibilities

| Agent | Function | Input | Output |
|-------|----------|-------|--------|
| **Researcher** | Gathers information | Topic string | Facts, stats, trends, expert opinions |
| **Writer** | Creates content | Research brief | Blog draft with headline, intro, body, conclusion |
| **Editor** | Polishes text | Blog draft | Grammar-fixed, flow-improved post |
| **SEO Analyst** | Optimizes search | Edited post | Keywords, meta description, SEO suggestions |

## 📊 Technology Stack

```
┌─────────────────────────────────────────────────────────┐
│                    PRESENTATION LAYER                    │
│                      Streamlit UI                        │
├─────────────────────────────────────────────────────────┤
│                   APPLICATION LAYER                      │
│                    unified_app.py                        │
│              (4 Agent Sequential Pipeline)               │
├─────────────────────────────────────────────────────────┤
│                      AI MODEL LAYER                      │
│                   Google Gemini API                      │
│              (gemini-2.5-flash / pro)                    │
├─────────────────────────────────────────────────────────┤
│                     STORAGE LAYER                        │
│                    output/*.txt                          │
└─────────────────────────────────────────────────────────┘
```

## 🔧 Dependencies

```txt
streamlit>=1.28.0      # Web framework
google-genai>=0.1.0    # Gemini API client
python-dotenv>=1.0.0   # Environment variables
plotly>=5.17.0         # Analytics charts
pandas>=2.0.0          # Data manipulation
```

## 📈 Directory Growth

```
After 1 run:      output/ (4 KB)     - 1 blog
After 10 runs:    output/ (40 KB)    - 10 blogs
After 100 runs:   output/ (400 KB)   - 100 blogs
Total project (excluding venv): ~2 MB
```

## 🗂️ File Naming Convention

Generated blogs follow this pattern:
```
output/blog_{topic}_{YYYYMMDD_HHMMSS}.txt

Example:
output/blog_Artificial_Intelligence_20260406_143022.txt
```

## 🔒 Git Ignored Files

The following files are NOT committed to git:
- `.env` (contains your actual API key)
- `venv/`, `__pycache__/` (Python environment)
- `output/*.txt` (generated blogs)
- `.DS_Store`, `*.log` (system files)

## 🚀 Deployment Structure

When deployed to Streamlit Cloud:
```
Streamlit Cloud
├── Reads from: GitHub repository
├── Installs: requirements.txt
├── Runs: unified_app.py
├── Secrets: GEMINI_API_KEY (configured in dashboard)
└── Output: Available at https://blog-content-factory.streamlit.app
```

EOF

echo "✅ Project structure added to README.md"
```

## 📋 **Quick Preview**

```bash
cd /home/sandeep/backups/blog-content-factory-backup/blog-content-factory

# View the added structure
tail -80 README.md
```

## ✅ **Complete README.md Sections Now Include**

| Section | Content |
|---------|---------|
| Overview | Project description |
| Agents | 4 specialized agent details |
| Quick Start | Setup commands |
| **Project Structure** | ✅ File tree diagram |
| **File Descriptions** | ✅ Table with line counts |
| **Data Flow** | ✅ Pipeline diagram |
| **Agent Responsibilities** | ✅ Input/Output table |
| **Technology Stack** | ✅ Layer diagram |
| **Dependencies** | ✅ Package list |
| **Directory Growth** | ✅ Size estimates |
| **File Naming** | ✅ Convention explanation |
| **Git Ignored** | ✅ Security info |
| **Deployment** | ✅ Streamlit Cloud setup |

## Quick Start

```bash
# Clone repository
git clone https://github.com/Rohithyepuri/blog-content-factory.git
cd blog-content-factory

# Setup virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set API key
cp .env.example .env
# Edit .env with your Gemini API key

# Run app
streamlit run unified_app.py
Live Demo

https://blog-content-factory.streamlit.app
Tech Stack

    Python 3.12

    Streamlit

    Google Gemini API

    Plotly

Author

Y Rohith (99230040464) - KARE Emerging Tech Credit Program
License

MIT
EOF

echo "✅ README.md created"
text


### **Step 6: Create unified_app.py (Final Clean Version)**

```bash
cat > unified_app.py << 'EOF'
import streamlit as st
from dotenv import load_dotenv
import os
import time
from datetime import datetime
import plotly.graph_objects as go
import pandas as pd
from google import genai
from google.genai import types

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

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    st.error("❌ GEMINI_API_KEY not found! Add to .env file")
    st.stop()

client = genai.Client(api_key=api_key)

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
            r = client.models.generate_content(model="gemini-2.5-flash", contents=f"Research topic: {topic}. Provide facts, stats, trends.", config=types.GenerateContentConfig(temperature=creativity))
            research = r.text
            
            status.markdown("✍️ **Agent 2/4: Writing...**")
            progress.progress(50)
            w = client.models.generate_content(model="gemini-2.5-flash", contents=f"Using: {research}\nWrite {word_count}-word blog on '{topic}'. Include headline, intro, body, conclusion.", config=types.GenerateContentConfig(temperature=creativity))
            draft = w.text
            
            status.markdown("📝 **Agent 3/4: Editing...**")
            progress.progress(75)
            e = client.models.generate_content(model="gemini-2.5-flash", contents=f"Edit for grammar, flow, tone: {draft}", config=types.GenerateContentConfig(temperature=creativity))
            edited = e.text
            
            status.markdown("🎯 **Agent 4/4: SEO...**")
            progress.progress(100)
            s = client.models.generate_content(model="gemini-2.5-flash", contents=f"Add SEO (keywords, meta description): {edited}", config=types.GenerateContentConfig(temperature=creativity))
            final = s.text
            
            st.markdown("---")
            st.subheader("📄 Generated Blog")
            st.markdown(final)
            
            os.makedirs("output", exist_ok=True)
            fname = f"output/blog_{topic.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            with open(fname, 'w') as f:
                f.write(final)
            st.success(f"✅ Saved to {fname} | Time: {time.time()-start:.1f}s")
            
        except Exception as e:
            st.error(f"Error: {e}")
        finally:
            progress.empty()
            status.empty()
EOF

echo "✅ unified_app.py created"
