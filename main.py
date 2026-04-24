import os
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage


GROQ_KEY = "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"
TAVILY_KEY = "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"


llm = ChatGroq(
    model="openai/gpt-oss-120b", 
    temperature=0.1, 
    groq_api_key=GROQ_KEY
)


search_tool = TavilySearchResults(
    max_results=3, 
    tavily_api_key=TAVILY_KEY
)
tools = [search_tool]


SYSTEM_PROMPT = """You are a Career Growth Agent. 
1. Identify 3 skill gaps between Resume and JD.
2. Find 'Adjacent Skills' the candidate can learn.
3. Search for free resources for these skills.
4. Output a 4-week learning plan in a Markdown table."""


agent = create_react_agent(llm, tools, prompt=SYSTEM_PROMPT)

def run_assessment(resume_text, jd_text):
    query = f"RESUME:\n{resume_text}\n\nJD:\n{jd_text}"
    try:
        result = agent.invoke({"messages": [HumanMessage(content=query)]})
        return result["messages"][-1].content
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    test_resume = "Python developer, knows SQL."
    test_jd = "Senior Backend, needs AWS and Docker."
    print("Agent is thinking...")
    print(run_assessment(test_resume, test_jd))