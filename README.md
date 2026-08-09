# Career Architect AI

**Live app:** https://catalyst-ai-agent-yashsaxena3779.streamlit.app/

An autonomous agent that reads a resume and a target job description, identifies the skill gap
between them, and builds a four-week learning roadmap grounded in resources it retrieves live from
the web rather than recalled from model weights.

Built for the Catalyst Hackathon.

## How it works

The system runs on a ReAct (Reasoning and Acting) loop rather than a single prompt. Given a resume
and a job description, the agent:

1. Performs a gap analysis to identify which required skills are missing or underevidenced.
2. Decides for itself what to search for, generating its own queries from that gap analysis.
3. Calls the Tavily search API to retrieve current, freely available learning material.
4. Evaluates the returned resources for relevance and quality before including them.
5. Assembles a week-by-week roadmap where every recommended resource is one it actually retrieved.

The design decision that matters here is step 3. A model asked to recommend learning resources from
memory will produce plausible-looking course names and dead links, because it is generating rather
than retrieving. Grounding every recommendation in a live search result means the roadmap points at
things that exist right now.

## Stack

| Layer | Technology |
|---|---|
| Language model | Llama 3.3 70B via Groq Cloud |
| Agent framework | LangGraph, LangChain |
| Search | Tavily API |
| Document parsing | pypdf |
| Interface | Streamlit |
| Deployment | Streamlit Community Cloud |

## Running it locally

```bash
git clone <repository-url>
cd <repository-directory>
pip install -r requirements.txt
```

Create a `.env` file in the project root with your API keys:

```
GROQ_API_KEY=your_groq_key_here
TAVILY_API_KEY=your_tavily_key_here
```

Both are free to obtain — Groq at console.groq.com, Tavily at tavily.com. The `.env` file is
gitignored and keys are never committed.

Then:

```bash
python -m streamlit run app.py
```

## Notes

Resume text is parsed in memory and not persisted anywhere. The hosted app is a demo; it runs on
free-tier API quotas, so heavy concurrent use may hit rate limits.
