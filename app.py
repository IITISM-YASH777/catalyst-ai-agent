import streamlit as st
from pypdf import PdfReader
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage


st.set_page_config(page_title="Career Architect AI", page_icon="▲", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Mono:wght@400;500&family=Syne:wght@400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Syne', sans-serif;
    }

    .stApp {
        background-color: #0f1117;
        color: #e8e6e0;
    }

   
    header[data-testid="stHeader"] { background: transparent; }
    .block-container { padding-top: 2rem; padding-bottom: 4rem; max-width: 900px; }

    
    .ca-eyebrow {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        font-size: 11px;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        color: #c8b89a;
        background: rgba(200,184,154,0.08);
        border: 1px solid rgba(200,184,154,0.18);
        padding: 5px 14px;
        border-radius: 100px;
        margin-bottom: 20px;
    }

    .ca-title {
        font-family: 'DM Serif Display', serif;
        font-size: 48px;
        font-weight: 400;
        line-height: 1.08;
        color: #f0ede6;
        text-align: center;
        margin-bottom: 14px;
        letter-spacing: -0.01em;
    }

    .ca-title em {
        font-style: italic;
        color: #c8b89a;
    }

    .ca-subtitle {
    font-size: 15px;
    color: #555a6b;
    text-align: center !important;
    max-width: 460px;
    margin: 0 auto 48px !important;
    line-height: 1.7;
    display: block;
    width: 100%;

    }

    div[data-testid="stVerticalBlock"] > div:has(div.stFileUploader),
    div[data-testid="stVerticalBlock"] > div:has(div.stTextArea) {
        background: #13151d;
        border: 1px solid #1e2029;
        border-radius: 16px;
        padding: 24px !important;
    }

    /* ---- LABELS ---- */
    .stFileUploader label, .stTextArea label {
        font-size: 11px !important;
        font-weight: 600 !important;
        letter-spacing: 0.1em !important;
        text-transform: uppercase !important;
        color: #555a6b !important;
    }

    /* ---- FILE UPLOADER ---- */
    [data-testid="stFileUploader"] section {
        background: rgba(255,255,255,0.015) !important;
        border: 1.5px dashed #252837 !important;
        border-radius: 12px !important;
        transition: border-color 0.2s, background 0.2s;
    }

    [data-testid="stFileUploader"] section:hover {
        border-color: rgba(200,184,154,0.3) !important;
        background: rgba(200,184,154,0.03) !important;
    }

    [data-testid="stFileUploadDropzone"] p {
        color: #555a6b !important;
        font-size: 13px !important;
    }

    [data-testid="stFileUploader"] button {
        background: rgba(200,184,154,0.1) !important;
        color: #c8b89a !important;
        border: 1px solid rgba(200,184,154,0.2) !important;
        border-radius: 6px !important;
        font-size: 12px !important;
        font-weight: 600 !important;
        letter-spacing: 0.04em !important;
        text-transform: uppercase !important;
    }

    /* ---- TEXTAREA ---- */
    .stTextArea textarea {
        background: rgba(255,255,255,0.02) !important;
        border: 1px solid #1e2029 !important;
        border-radius: 12px !important;
        color: #9fa4b4 !important;
        font-family: 'Syne', sans-serif !important;
        font-size: 13px !important;
        line-height: 1.7 !important;
        caret-color: #c8b89a;
    }

    .stTextArea textarea::placeholder { color: #333744 !important; }

    .stTextArea textarea:focus {
        border-color: rgba(200,184,154,0.3) !important;
        box-shadow: none !important;
    }

    /* ---- FEATURE CHIPS ---- */
    .ca-features {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 12px;
        margin: 16px 0;
    }

    .ca-feature-chip {
        background: #13151d;
        border: 1px solid #1e2029;
        border-radius: 10px;
        padding: 14px 16px;
        display: flex;
        align-items: flex-start;
        gap: 10px;
    }

    .ca-chip-dot {
        width: 6px; height: 6px;
        border-radius: 50%;
        background: #c8b89a;
        margin-top: 5px;
        flex-shrink: 0;
    }

    .ca-chip-text { font-size: 12px; color: #555a6b; line-height: 1.5; }
    .ca-chip-text strong {
        display: block;
        color: #7a8099;
        font-weight: 600;
        font-size: 11px;
        letter-spacing: 0.06em;
        text-transform: uppercase;
        margin-bottom: 2px;
    }

    /* ---- CTA BUTTON ---- */
    .stButton > button {
        width: 100%;
        background: #c8b89a !important;
        color: #0f1117 !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 18px 28px !important;
        font-family: 'Syne', sans-serif !important;
        font-size: 14px !important;
        font-weight: 700 !important;
        letter-spacing: 0.06em !important;
        text-transform: uppercase !important;
        transition: background 0.2s, transform 0.1s !important;
        height: auto !important;
    }

    .stButton > button:hover {
        background: #d9cab0 !important;
        transform: translateY(-1px);
        box-shadow: 0 8px 24px rgba(200,184,154,0.15) !important;
    }

    .stButton > button:active { transform: scale(0.99); }

    /* ---- SUCCESS / ERROR MESSAGES ---- */
    .stSuccess {
        background: rgba(200,184,154,0.08) !important;
        border: 1px solid rgba(200,184,154,0.2) !important;
        border-radius: 10px !important;
        color: #c8b89a !important;
    }

    .stAlert { border-radius: 10px !important; }

    /* ---- STATUS WIDGET ---- */
    .stStatusWidget {
        background: #13151d !important;
        border: 1px solid #1e2029 !important;
        border-radius: 12px !important;
    }

    /* ---- OUTPUT SECTION ---- */
    .ca-output {
        background: #13151d;
        border: 1px solid #1e2029;
        border-radius: 16px;
        padding: 28px;
        margin-top: 16px;
    }

    .ca-output-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 20px;
        padding-bottom: 16px;
        border-bottom: 1px solid #1e2029;
    }

    .ca-output-title {
        font-size: 11px;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        color: #555a6b;
        font-weight: 600;
    }

    .ca-output-badge {
        font-size: 10px;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        color: rgba(200,184,154,0.6);
        background: rgba(200,184,154,0.07);
        border: 1px solid rgba(200,184,154,0.12);
        border-radius: 4px;
        padding: 3px 8px;
    }

    /* Markdown output styling */
    .stMarkdown h3 { color: #c8b89a !important; font-family: 'DM Serif Display', serif !important; font-weight: 400 !important; }
    .stMarkdown p, .stMarkdown li { color: #7a8099 !important; font-size: 14px !important; line-height: 1.8 !important; }
    .stMarkdown table { border-radius: 10px; overflow: hidden; border: 1px solid #1e2029; }
    .stMarkdown th { background: #1a1c26 !important; color: #c8b89a !important; font-size: 11px !important; letter-spacing: 0.08em !important; text-transform: uppercase !important; padding: 12px 16px !important; }
    .stMarkdown td { background: #13151d !important; color: #c8c4bc !important; font-size: 15px !important; padding: 12px 16px !important; border-top: 1px solid #1e2029 !important; }
    </style>
    """, unsafe_allow_html=True)


st.markdown('<div style="text-align:center; margin-bottom: 8px;"><span class="ca-eyebrow" style="font-size:14px; letter-spacing:0.08em;">&#x25CF;&nbsp; Career Architect AI</span></div>', unsafe_allow_html=True)
st.markdown('<h1 class="ca-title">Bridge the gap between your resume<br>and your <em>dream role.</em></h1>', unsafe_allow_html=True)
st.markdown('<div style="text-align:center; width:100%;"><p class="ca-subtitle" style="text-align:center; margin:0 auto;">Upload your resume. Paste a job description. Get a precision-built 4-week learning plan grounded in real skill gaps.</p></div>', unsafe_allow_html=True)

def extract_text_from_pdf(file):
    pdf_reader = PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() or ""
    return text

GROQ_KEY = "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"
TAVILY_KEY = "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"


col1, col2 = st.columns(2)

with col1:
    uploaded_file = st.file_uploader("📄 Resume", type="pdf", label_visibility="visible")
    resume_text = ""
    if uploaded_file is not None:
        resume_text = extract_text_from_pdf(uploaded_file)
        st.success("Resume loaded successfully.")

with col2:
    jd_text = st.text_area("💼 Job Description", height=220, placeholder="Paste the full job description here — responsibilities, required skills, and qualifications...")


st.markdown("""
<div class="ca-features">
  <div class="ca-feature-chip">
    <div class="ca-chip-dot"></div>
    <div class="ca-chip-text"><strong>Gap Analysis</strong>Identifies the 3 most critical missing skills from your profile</div>
  </div>
  <div class="ca-feature-chip">
    <div class="ca-chip-dot"></div>
    <div class="ca-chip-text"><strong>Live Search</strong>Finds current, free learning resources curated to your gaps</div>
  </div>
  <div class="ca-feature-chip">
    <div class="ca-chip-dot"></div>
    <div class="ca-chip-text"><strong>4-Week Plan</strong>Structured weekly milestones to close the gap efficiently</div>
  </div>
</div>
""", unsafe_allow_html=True)


if st.button("Generate My Learning Path ↗"):
    if resume_text and jd_text:
        with st.status("Agent is searching and reasoning...", expanded=True) as status:
            llm = ChatGroq(model="openai/gpt-oss-120b", groq_api_key=GROQ_KEY)
            search_tool = TavilySearchResults(max_results=3, tavily_api_key=TAVILY_KEY)
            SYSTEM_PROMPT = "Compare resume and JD. Find 3 skill gaps and adjacent skills. Find free resources. Output a 4-week table."
            agent = create_react_agent(llm, [search_tool], prompt=SYSTEM_PROMPT)
            query = f"RESUME:\n{resume_text}\n\nJD:\n{jd_text}"
            response = agent.invoke({"messages": [HumanMessage(content=query)]})
            status.update(label="Analysis complete.", state="complete")

        st.markdown("""
        <div class="ca-output">
          <div class="ca-output-header">
            <span class="ca-output-title">Your Personalized 4-Week Plan</span>
            <span class="ca-output-badge">AI Generated</span>
          </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(response["messages"][-1].content)

    else:
        st.error("Please upload a Resume PDF and paste a Job Description before generating.")
