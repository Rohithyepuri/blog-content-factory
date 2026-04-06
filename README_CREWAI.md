# CrewAI Blog Factory

## 4 Specialized Agents
- 🔍 **Researcher** - Gathers comprehensive information
- ✍️ **Writer** - Creates engaging blog content  
- 📝 **Editor** - Polishes and refines
- 🎯 **SEO Analyst** - Optimizes for search engines

## Quick Start
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements-crewai.txt
python run_crewai.py "Your topic"Files

    agents.py - Agent definitions

    tasks.py - Task definitions

    crew.py - Orchestrator

    gemini_adapter.py - Gemini connector

    tools.py - Web tools
    EOF

echo "✅ Ready to upload!"
## 🎯 **What's Missing & Needs to be Added**

| File | Status | Action Needed |
|------|--------|---------------|
| `run_crewai.py` | ⚠️ Missing | Create it (see above) |
| `requirements-crewai.txt` | ⚠️ Missing | Create it |
| `.env` | ⚠️ Missing | Add API key |
| `README_CREWAI.md` | ⚠️ Missing | Create documentation |
| `output/` | ⚠️ Missing | Create directory |

## 📝 **Create Missing Files**

```bash
cd /home/sandeep/backups/blog-content-factory-backup/blog-content-factory

# Create requirements
cat > requirements-crewai.txt << 'EOF'
crewai==0.28.8
crewai-tools==0.1.6
langchain==0.1.12
google-generativeai==0.3.0
python-dotenv==1.0.0
beautifulsoup4==4.12.3
requests==2.31.0
