Career Architect AI Technical Documentation

Project Description

Career Architect AI is an autonomous agentic system designed for the Catalyst Hackathon. The application analyzes the gap between a user's current resume and a specific job description. It utilizes a reasoning loop to identify missing skills and performs real-time web searches to provide a structured four week learning roadmap with live resources.

Core Features

PDF Ingestion: Extracts text from resume files using the pypdf library.
ReAct Agent Logic: Implemented via LangGraph to provide autonomous reasoning and tool use.
Live Scouting: Integrated with the Tavily Search API to find current and free learning materials.
Professional Interface: A modern dark mode user interface built with the Streamlit framework.

Technical Stack

Large Language Model: Llama 3.3 70B via Groq Cloud,
Agent Framework: LangGraph and LangChain,
Search Infrastructure: Tavily AI,
Frontend Framework: Streamlit

Local Setup Instructions.
To run Career Architect AI locally, follow these steps:

1. Prerequisites

Ensure you have Python 3.10+ installed.
Obtain a Groq API Key and a Tavily API Key.

2. Clone and Install

git clone https://github.com/IITISM-YASH777/catalyst-ai-agent.git
cd catalyst-ai-agent

python -m pip install -r requirements.txt

3. Configure Environment
   
Open app.py and enter your API keys in the designated variables:
GROQ_KEY = "your_key_here"
TAVILY_KEY = "your_key_here"

4. Launch the Application

Run  
python -m streamlit run app.py.
in your terminal to launch the interface in your browser.

Technical Architecture

The system operates on a Reasoning and Acting (ReAct) pattern. Upon receiving input, the agent performs a gap analysis, determines necessary search queries, and validates the quality of external resources before generating the final roadmap. This ensures that all learning paths are grounded in real-world data rather than model hallucinations.
