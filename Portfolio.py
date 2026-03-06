import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import requests

# ─── UPDATE YOUR GITHUB RESUME LINKS HERE ─────────────────────────────────────
GITHUB_RESUME_VIEW = "https://github.com/akash0123-pride/akash0123-pride/blob/main/Akash_Pathak_Resume.pdf"
GITHUB_RESUME_URL  = "https://raw.githubusercontent.com/akash0123-pride/akash0123-pride/main/Akash_Pathak_Resume.pdf"

# ─── Page Config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Akash Pathak | AI/ML Engineer",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─── CSS ───────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Syne:wght@400;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Syne', sans-serif;
    background-color: #050510;
    color: #e2e2f0;
}
.stApp {
    background: linear-gradient(135deg, #050510 0%, #0d0d2e 50%, #050510 100%);
}
[data-testid="stSidebar"] {
    background: rgba(8,8,32,0.98) !important;
    border-right: 1px solid rgba(100,100,255,0.2);
}
[data-testid="stSidebar"] * { color: #e2e2f0 !important; }

.stRadio label {
    font-family: 'Space Mono', monospace !important;
    font-size: 13px !important;
    color: #aaaacc !important;
}
/* Expander */
[data-testid="stExpander"] {
    background: rgba(255,255,255,0.02) !important;
    border: 1px solid rgba(120,120,255,0.2) !important;
    border-radius: 12px !important;
    margin-bottom: 10px !important;
}
[data-testid="stExpander"]:hover {
    border-color: rgba(120,120,255,0.5) !important;
}
details summary {
    font-family: 'Syne', sans-serif !important;
    font-weight: 600 !important;
    color: #e2e2f0 !important;
    font-size: 0.95rem !important;
}
/* Buttons */
.stButton>button {
    background: linear-gradient(135deg,#7b7bff,#a78bfa) !important;
    color: white !important;
    border: none !important;
    border-radius: 8px !important;
    font-family: 'Space Mono', monospace !important;
    font-size: 13px !important;
}
/* Inputs */
.stTextInput>div>div>input {
    background: rgba(255,255,255,0.04) !important;
    border: 1px solid rgba(120,120,255,0.3) !important;
    border-radius: 8px !important;
    color: #e2e2f0 !important;
    font-family: 'Space Mono', monospace !important;
}
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 1.5rem !important; max-width: 900px !important; }

/* Custom classes */
.glow-title {
    font-family: 'Syne', sans-serif;
    font-size: 2.8rem;
    font-weight: 800;
    background: linear-gradient(90deg,#7b7bff,#a78bfa,#38bdf8,#7b7bff);
    background-size: 300%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: shimmer 4s linear infinite;
    line-height: 1.2;
    margin-bottom: 12px;
}
@keyframes shimmer { 0%{background-position:0%} 100%{background-position:300%} }

.sub-label {
    font-family: 'Space Mono', monospace;
    font-size: 0.72rem;
    color: #7b7bff;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 6px;
}
.sec-title {
    font-family: 'Syne', sans-serif;
    font-size: 1.8rem;
    font-weight: 800;
    color: #e2e2f0;
    padding-bottom: 10px;
    border-bottom: 2px solid rgba(120,120,255,0.3);
    margin-bottom: 22px;
}
.card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(120,120,255,0.18);
    border-radius: 14px;
    padding: 22px 24px;
    margin-bottom: 16px;
}
.tag {
    display: inline-block;
    background: rgba(120,120,255,0.12);
    border: 1px solid rgba(120,120,255,0.28);
    color: #a78bfa;
    border-radius: 20px;
    padding: 3px 12px;
    font-family: 'Space Mono', monospace;
    font-size: 11px;
    margin: 3px 2px;
}
.stat-box {
    background: rgba(120,120,255,0.07);
    border: 1px solid rgba(120,120,255,0.22);
    border-radius: 12px;
    padding: 16px 10px;
    text-align: center;
}
.stat-num { font-family:'Space Mono',monospace; font-size:1.6rem; font-weight:700; color:#7b7bff; }
.stat-lbl { font-size:0.68rem; color:#7777aa; text-transform:uppercase; letter-spacing:1.5px; margin-top:4px; }

.link-btn {
    display: inline-block;
    background: rgba(120,120,255,0.13);
    border: 1px solid rgba(120,120,255,0.32);
    border-radius: 8px;
    padding: 9px 18px;
    color: #a78bfa !important;
    text-decoration: none;
    font-family: 'Space Mono', monospace;
    font-size: 12px;
    margin: 4px 4px 4px 0;
}
.link-btn-primary {
    display: inline-block;
    background: linear-gradient(135deg,#7b7bff,#a78bfa);
    border-radius: 8px;
    padding: 9px 18px;
    color: white !important;
    text-decoration: none;
    font-family: 'Space Mono', monospace;
    font-size: 12px;
    margin: 4px 4px 4px 0;
}
.link-btn-green {
    display: inline-block;
    background: rgba(74,222,128,0.1);
    border: 1px solid rgba(74,222,128,0.3);
    border-radius: 8px;
    padding: 9px 18px;
    color: #4ade80 !important;
    text-decoration: none;
    font-family: 'Space Mono', monospace;
    font-size: 12px;
    margin: 4px 4px 4px 0;
}
.chat-user {
    background: rgba(120,120,255,0.14);
    border: 1px solid rgba(120,120,255,0.3);
    border-radius: 12px 12px 2px 12px;
    padding: 11px 15px;
    margin: 8px 0;
    font-size: 0.9rem;
    text-align: right;
}
.chat-bot {
    background: rgba(56,189,248,0.07);
    border: 1px solid rgba(56,189,248,0.18);
    border-radius: 2px 12px 12px 12px;
    padding: 11px 15px;
    margin: 8px 0;
    font-size: 0.9rem;
    font-family: 'Space Mono', monospace;
    line-height: 1.6;
}
</style>
""", unsafe_allow_html=True)


# ─── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style='text-align:center;padding:16px 0 10px;'>
        <div style='width:72px;height:72px;border-radius:50%;
             background:linear-gradient(135deg,#7b7bff,#38bdf8);
             margin:0 auto;display:flex;align-items:center;justify-content:center;
             font-size:1.8rem;border:2px solid rgba(120,120,255,0.5);
             box-shadow:0 0 18px rgba(120,120,255,0.35);'>🤖</div>
        <div style='margin-top:10px;font-family:Syne,sans-serif;font-size:1rem;font-weight:700;'>Akash Pathak</div>
        <div style='font-family:Space Mono,monospace;font-size:0.65rem;color:#7b7bff;letter-spacing:2px;margin-top:3px;'>AI/ML ENGINEER</div>
        <div style='margin-top:8px;font-size:0.7rem;color:#4ade80;'>● Open to Opportunities</div>
    </div>
    """, unsafe_allow_html=True)
    st.divider()
    page = st.radio("Navigate", [
        "🏠 Home", "🎓 Education", "💼 Experience",
        "🚀 Projects", "📊 Skills", "📜 Certifications",
        "🤖 AI Chatbot", "📞 Contact"
    ], label_visibility="collapsed")


# ══════════════════════════════════════════════════════════════════════════════
# 🏠 HOME
# ══════════════════════════════════════════════════════════════════════════════
if page == "🏠 Home":

    st.markdown("<div class='sub-label'>AI / ML ENGINEER · DATA SCIENCE</div>", unsafe_allow_html=True)
    st.markdown("<div class='glow-title'>Akash Pathak</div>", unsafe_allow_html=True)
    st.markdown("""
    <p style='font-size:1rem;color:#aaaacc;line-height:1.8;max-width:640px;'>
    Building intelligent systems that learn, adapt, and solve real-world problems.
    From scalable ML pipelines to GenAI-powered applications — I bridge research and production.
    </p>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div style='margin:16px 0 24px;flex-wrap:wrap;'>
        <a class='link-btn' href='https://www.linkedin.com/in/akash-pathak-44a082212' target='_blank'>🔗 LinkedIn</a>
        <a class='link-btn' href='https://github.com/akash0123-pride' target='_blank'>🐙 GitHub</a>
        <a class='link-btn-primary' href='{GITHUB_RESUME_VIEW}' target='_blank'>📄 View Resume</a>
        <a class='link-btn-green' href='{GITHUB_RESUME_URL}' download>⬇️ Download CV</a>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    # Stats — 4 columns
    c1, c2, c3, c4 = st.columns(4)
    for col, (n, l) in zip([c1,c2,c3,c4], [("1+","Year at TCS"),("6+","Projects"),("5","Certs"),("8.32","CGPA")]):
        with col:
            st.markdown(f"<div class='stat-box'><div class='stat-num'>{n}</div><div class='stat-lbl'>{l}</div></div>", unsafe_allow_html=True)

    st.divider()

    # Core Stack tags
    st.markdown("<div class='sub-label'>Core Stack</div>", unsafe_allow_html=True)
    tags = ["Python","TensorFlow","PyTorch","LangChain","LangGraph","RAG",
            "HuggingFace","Docker","AWS","MLOps","Scikit-learn","SQL","Tableau","Streamlit"]
    st.markdown(" ".join([f"<span class='tag'>{t}</span>" for t in tags]), unsafe_allow_html=True)

    st.divider()

    # Radar chart
    st.markdown("<div class='sub-label'>Capability Radar</div>", unsafe_allow_html=True)
    cats   = ["ML / DL", "Generative AI", "MLOps", "Data Eng.", "Cloud/DevOps", "Programming"]
    vals   = [88, 85, 78, 82, 75, 90]
    fig = go.Figure(go.Scatterpolar(
        r=vals+[vals[0]], theta=cats+[cats[0]],
        fill='toself', fillcolor='rgba(123,123,255,0.13)',
        line=dict(color='#7b7bff', width=2),
        marker=dict(color='#a78bfa', size=7)
    ))
    fig.update_layout(
        polar=dict(
            bgcolor='rgba(0,0,0,0)',
            radialaxis=dict(visible=True, range=[0,100], color='#555577', gridcolor='rgba(120,120,255,0.12)'),
            angularaxis=dict(color='#aaaacc', gridcolor='rgba(120,120,255,0.12)')
        ),
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        font=dict(family='Space Mono,monospace', color='#aaaacc'),
        height=360, margin=dict(l=50,r=50,t=20,b=20)
    )
    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # Quick links to other pages
    st.markdown("<div class='sub-label'>Explore Portfolio</div>", unsafe_allow_html=True)
    r1, r2, r3 = st.columns(3)
    with r1:
        if st.button("💼 Experience", use_container_width=True): st.session_state["nav"] = "💼 Experience"
    with r2:
        if st.button("🚀 Projects", use_container_width=True): st.session_state["nav"] = "🚀 Projects"
    with r3:
        if st.button("🤖 AI Chatbot", use_container_width=True): st.session_state["nav"] = "🤖 AI Chatbot"


# ══════════════════════════════════════════════════════════════════════════════
# 🎓 EDUCATION
# ══════════════════════════════════════════════════════════════════════════════
elif page == "🎓 Education":
    st.markdown("<div class='sec-title'>🎓 Education</div>", unsafe_allow_html=True)

    for edu in [
        ("B.Tech — Computer Science Eng. (Data Science)",
         "Oriental Institute of Science & Technology, Bhopal",
         "2020 – 2024", "CGPA 8.32", "#4ade80",
         "Specialized in Data Science track covering Machine Learning, Deep Learning, Statistics, Big Data technologies, and AI system design."),
        ("Intermediate — Class XII",
         "Maharishi Vidya Mandir, Jabalpur",
         "", "69.2%", "#38bdf8", ""),
        ("High School — Class X",
         "Maharishi Vidya Mandir, Jabalpur",
         "", "CGPA 9.4", "#4ade80", ""),
    ]:
        title, inst, period, grade, gc, note = edu
        st.markdown(f"""
        <div class='card'>
            <div style='display:flex;justify-content:space-between;flex-wrap:wrap;gap:8px;'>
                <div>
                    <div style='font-size:1.05rem;font-weight:700;color:#e2e2f0;'>{title}</div>
                    <div style='font-family:Space Mono,monospace;font-size:0.8rem;color:#7b7bff;margin-top:5px;'>{inst}</div>
                    {"<div style='color:#555577;font-size:0.8rem;margin-top:4px;'>"+period+"</div>" if period else ""}
                </div>
                <div style='text-align:right;'>
                    <span style='font-family:Space Mono,monospace;font-size:1.2rem;font-weight:700;color:{gc};'>{grade}</span>
                </div>
            </div>
            {"<p style='color:#8888aa;font-size:0.88rem;line-height:1.7;margin-top:12px;margin-bottom:0;'>"+note+"</p>" if note else ""}
        </div>
        """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# 💼 EXPERIENCE
# ══════════════════════════════════════════════════════════════════════════════
elif page == "💼 Experience":
    st.markdown("<div class='sec-title'>💼 Experience & Internships</div>", unsafe_allow_html=True)

    # Timeline chart
    st.markdown("<div class='sub-label'>Career Timeline</div>", unsafe_allow_html=True)
    df_t = pd.DataFrame([
        dict(Task="DMRC – Data Science Intern",   Start="2022-07-01", Finish="2022-09-30", Type="Internship"),
        dict(Task="IBM SkillsBuild – ML Intern",  Start="2022-09-01", Finish="2022-11-30", Type="Internship"),
        dict(Task="TCS – AI/ML Engineer",         Start="2025-05-01", Finish="2026-03-01", Type="Full-Time"),
    ])
    fig_t = px.timeline(df_t, x_start="Start", x_end="Finish", y="Task", color="Type",
                        color_discrete_map={"Internship":"#a78bfa","Full-Time":"#7b7bff"})
    fig_t.update_yaxes(autorange="reversed")
    fig_t.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        font=dict(family='Space Mono,monospace', color='#aaaacc'),
        xaxis=dict(gridcolor='rgba(120,120,255,0.1)', color='#aaaacc'),
        yaxis=dict(color='#aaaacc'),
        legend=dict(bgcolor='rgba(0,0,0,0)'),
        height=200, margin=dict(l=10,r=10,t=10,b=10)
    )
    st.plotly_chart(fig_t, use_container_width=True)

    st.markdown("<div class='sub-label' style='margin:20px 0 12px;'>Full-Time</div>", unsafe_allow_html=True)

    with st.expander("🟣  AI/ML Engineer — Tata Consultancy Services (TCS)  |  May 2025 – Present  📍 Indore", expanded=True):
        st.markdown("""
        <div style='padding:4px 0;'>
        <div style='margin-bottom:12px;'>
        <span class='tag'>TensorFlow</span><span class='tag'>Docker</span><span class='tag'>AWS</span>
        <span class='tag'>CI/CD</span><span class='tag'>MLOps</span><span class='tag'>Model Monitoring</span>
        <span class='tag'>Python</span><span class='tag'>Drift Detection</span>
        </div>
        <div style='color:#aaaacc;line-height:1.85;font-size:0.93rem;'>
        <b style='color:#7b7bff;'>Responsibilities</b><br>
        ▸ Designed end-to-end ML workflows — preprocessing, feature engineering, training, deployment & monitoring.<br>
        ▸ Built scalable TensorFlow models improving classification accuracy and enabling automated decision workflows.<br>
        ▸ Developed intelligent automation systems reducing manual intervention through ML-driven decision engines.<br>
        ▸ Containerized ML services with Docker and implemented CI/CD pipelines for AWS deployments.<br>
        ▸ Monitored production models for data drift, performance degradation, and reliability.<br><br>
        <b style='color:#7b7bff;'>Impact</b><br>
        ▸ Reduced manual intervention significantly via automated ML decision engines.<br>
        ▸ Improved model reliability through proactive drift detection and monitoring pipelines.
        </div></div>
        """, unsafe_allow_html=True)

    st.markdown("<div class='sub-label' style='margin:20px 0 12px;'>Internships</div>", unsafe_allow_html=True)

    with st.expander("🔵  Machine Learning Intern — IBM SkillsBuild  |  Sep 2022 – Nov 2022  📍 Remote"):
        st.markdown("""
        <div style='padding:4px 0;'>
        <div style='margin-bottom:12px;'>
        <span class='tag'>Random Forest</span><span class='tag'>Scikit-learn</span>
        <span class='tag'>Feature Engineering</span><span class='tag'>Cross-Validation</span><span class='tag'>Python</span>
        </div>
        <div style='color:#aaaacc;line-height:1.85;font-size:0.93rem;'>
        <b style='color:#38bdf8;'>Work Done</b><br>
        ▸ Built supervised ML models including Random Forest for structured data classification.<br>
        ▸ Performed data preprocessing — missing value treatment, encoding, and scaling.<br>
        ▸ Applied feature engineering to improve model signal and reduce noise.<br>
        ▸ Used cross-validation and hyperparameter tuning to optimize model performance.<br><br>
        <b style='color:#38bdf8;'>Outcome</b><br>
        ▸ Delivered working ML model predicting patient mental health treatment requirements with strong accuracy.
        </div></div>
        """, unsafe_allow_html=True)

    with st.expander("🟡  Data Science Intern — Delhi Metro Rail Corporation (DMRC)  |  Jul 2022 – Sep 2022  📍 Delhi"):
        st.markdown("""
        <div style='padding:4px 0;'>
        <div style='margin-bottom:12px;'>
        <span class='tag'>Python</span><span class='tag'>Pandas</span><span class='tag'>Streamlit</span>
        <span class='tag'>Data Cleaning</span><span class='tag'>Outlier Detection</span><span class='tag'>Analytics</span>
        </div>
        <div style='color:#aaaacc;line-height:1.85;font-size:0.93rem;'>
        <b style='color:#a78bfa;'>Work Done</b><br>
        ▸ Performed comprehensive data cleaning — missing value handling and outlier detection for analytics pipelines.<br>
        ▸ Conducted EDA on large structured datasets to uncover operational patterns.<br>
        ▸ Developed a Streamlit-based application for structured data collection and interactive visualization.<br>
        ▸ Generated actionable insights to support infrastructure impact analysis.<br><br>
        <b style='color:#a78bfa;'>Outcome</b><br>
        ▸ Delivered live analytics dashboard used by the operations team for real-time data monitoring.
        </div></div>
        """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# 🚀 PROJECTS
# ══════════════════════════════════════════════════════════════════════════════
elif page == "🚀 Projects":
    st.markdown("<div class='sec-title'>🚀 Projects</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#8888aa;font-size:0.88rem;margin-bottom:20px;'>Tap any project to see full details, tech stack, and outcomes.</p>", unsafe_allow_html=True)

    projects = [
        ("🧠", "Enterprise Document Intelligence (RAG)", True,
         "LangChain + Vector Search RAG pipeline for automated enterprise knowledge retrieval",
         ["LangChain","RAG","Vector DB","LLM","Python","HuggingFace"], "#7b7bff",
         "▸ Built a Retrieval-Augmented Generation pipeline using LangChain for document ingestion and chunking.<br>"
         "▸ Implemented FAISS/Chroma vector similarity search to retrieve relevant passages as LLM context.<br>"
         "▸ Supports multiple document formats: PDF, DOCX, TXT.<br>"
         "▸ Automated knowledge retrieval workflow reducing manual document lookup time significantly.<br><br>"
         "<b>Outcome:</b> Working RAG system answering domain-specific questions from large document collections."),
        ("🫁", "Lung Disease Detection", False,
         "ResNet-based deep learning model for X-ray classification of lung diseases",
         ["TensorFlow","ResNet","Deep Learning","Image Classification","Keras"], "#38bdf8",
         "▸ Fine-tuned ResNet50 on chest X-ray datasets for multi-class disease classification.<br>"
         "▸ Applied image augmentation (rotation, flip, zoom) to improve generalization.<br>"
         "▸ Achieved high accuracy distinguishing Normal, Pneumonia, and COVID-19 cases.<br>"
         "▸ Optimized with batch normalization and dropout to reduce overfitting.<br><br>"
         "<b>Outcome:</b> Accurate diagnostic assistance model deployable in clinical settings."),
        ("📊", "Indian Crime Data Dashboard", False,
         "Interactive Streamlit dashboard visualizing India-w
