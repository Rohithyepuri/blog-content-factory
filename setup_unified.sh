#!/bin/bash
echo "🚀 Setting up Unified Blog Factory..."

# Remove old venvs
rm -rf venv_unified venv_crewai_new venv_simple 2>/dev/null

# Create new venv
python3 -m venv venv_unified
source venv_unified/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install streamlit google-generativeai python-dotenv plotly pandas
pip install requests beautifulsoup4
pip install crewai==0.28.8
pip install crewai-tools==0.1.6

echo "✅ Setup complete!"
echo "🚀 Run: streamlit run unified_app.py"
