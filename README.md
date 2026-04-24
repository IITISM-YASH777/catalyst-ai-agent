Career Architect AI Technical Documentation

Project Description
Career Architect AI is an autonomous agentic system designed for the Catalyst Hackathon. The application analyzes the gap between a user's current resume and a specific job description. It utilizes a reasoning loop to identify missing skills and performs real-time web searches to provide a structured four week learning roadmap with live resources.

Core Features
PDF Ingestion: Extracts text from resume files using the pypdf library.
ReAct Agent Logic: Implemented via LangGraph to provide autonomous reasoning and tool use.
Live Scouting: Integrated with the Tavily Search API to find current and free learning materials.
Professional Interface: A modern dark mode user interface built with the Streamlit framework.

Technical Stack
Large Language Model: Llama 3.3 70B via Groq Cloud
Agent Framework: LangGraph and LangChain
Search Infrastructure: Tavily AI
Frontend Framework: Streamlit

Installation and Setup

Clone the repository
Use git clone followed by your repository URL to download the source code to your local machine.

Install dependencies
Run the command pip install -r requirements.txt to install all necessary Python libraries.

Configure API Keys
Open app.py and locate the key variables. Replace the placeholders with your valid Groq and Tavily API keys.

Execute the Application
Run the command python -m streamlit run app.py in your terminal to launch the interface in your browser.

Technical Architecture
The system operates on a Reasoning and Acting (ReAct) pattern. Upon receiving input, the agent performs a gap analysis, determines necessary search queries, and validates the quality of external resources before generating the final roadmap. This ensures that all learning paths are grounded in real-world data rather than model hallucinations.