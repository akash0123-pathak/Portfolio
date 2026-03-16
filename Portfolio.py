import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import requests

# ─── UPDATE YOUR GITHUB RESUME LINKS HERE ─────────────────────────────────────
GITHUB_RESUME_VIEW = "https://drive.google.com/file/d/1Aq_yLZhdb9nkGAHU8-pnyemgZuGd9EAg/view?usp=drivesdk"
GITHUB_RESUME_URL  = "https://raw.githubusercontent.com/akash0123-pathak/akash0123-pathak/main/Akash_Pathak_Resume.pdf"

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


# ─── Navigation ────────────────────────────────────────────────────────────────
PAGES = ["🏠 Home","🎓 Education","💼 Experience","🚀 Projects",
         "📊 Skills","📜 Certifications","🤖 AI Chatbot","📞 Contact"]

if "page_idx" not in st.session_state:
    st.session_state.page_idx = 0

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
    sidebar_sel = st.radio("Navigate", PAGES,
                           index=st.session_state.page_idx,
                           label_visibility="collapsed")
    if PAGES.index(sidebar_sel) != st.session_state.page_idx:
        st.session_state.page_idx = PAGES.index(sidebar_sel)
        st.rerun()

page = PAGES[st.session_state.page_idx]


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
        <a class='link-btn' href='https://github.com/akash0123-pathak' target='_blank'>🐙 GitHub</a>
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

    st.markdown("<div class='sub-label'>Explore Portfolio</div>", unsafe_allow_html=True)
    r1, r2, r3 = st.columns(3)
    with r1:
        if st.button("💼 Experience", use_container_width=True):
            st.session_state.page_idx = 2
            st.rerun()
    with r2:
        if st.button("🚀 Projects", use_container_width=True):
            st.session_state.page_idx = 3
            st.rerun()
    with r3:
        if st.button("🤖 AI Chatbot", use_container_width=True):
            st.session_state.page_idx = 6
            st.rerun()


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
         "Interactive Streamlit dashboard visualizing India-wide crime trends with full EDA",
         ["Streamlit","Pandas","Plotly","EDA","Data Visualization","Python"], "#a78bfa",
         "▸ Collected and cleaned government crime datasets spanning 10+ years across all Indian states.<br>"
         "▸ Built interactive Streamlit dashboard with filters, maps, and animated trend charts.<br>"
         "▸ Performed EDA revealing state-wise, year-wise, and crime-type patterns.<br>"
         "▸ Generated actionable insights on crime hotspots and year-on-year change rates.<br><br>"
         "<b>Outcome:</b> Live dashboard enabling drill-down analysis used for data storytelling."),
        ("💡", "Smart Streetlight AI System", False,
         "Computer vision system for automated streetlight anomaly detection and monitoring",
         ["OpenCV","Computer Vision","Python","Anomaly Detection","ML"], "#f472b6",
         "▸ Built real-time monitoring pipeline using OpenCV to analyze streetlight status from camera feeds.<br>"
         "▸ Trained ML model to detect anomalies: flickering, outages, brightness deviations.<br>"
         "▸ Designed alert system to trigger notifications when anomalies are detected.<br>"
         "▸ Implemented real-time analytics dashboard for municipal infrastructure monitoring.<br><br>"
         "<b>Outcome:</b> Automated system reducing manual inspection time with real-time anomaly reporting."),
        ("🚗", "Driver Drowsiness Detection", False,
         "Real-time OpenCV system detecting driver fatigue and triggering safety alerts",
         ["OpenCV","dlib","Python","Real-Time","Computer Vision"], "#34d399",
         "▸ Used facial landmark detection (dlib) to track Eye Aspect Ratio (EAR) in real time.<br>"
         "▸ Triggers audio/visual alarm when eyes stay closed beyond drowsiness threshold.<br>"
         "▸ Achieves low-latency detection at 30fps on standard webcam input.<br>"
         "▸ Added head tilt and yawn detection as secondary fatigue indicators.<br><br>"
         "<b>Outcome:</b> Real-time safety system deployable in vehicles to prevent drowsy driving accidents."),
        ("💚", "Mental Health Tracker", False,
         "ML app analyzing user responses to track mental wellness patterns and give insights",
         ["Python","ML","Streamlit","NLP","Scikit-learn"], "#fbbf24",
         "▸ Designed questionnaire-based mental health screening app using validated psychological scales.<br>"
         "▸ Trained Random Forest classifier to predict mental health risk levels from user responses.<br>"
         "▸ Built clean Streamlit UI with personalized feedback and session trend tracking.<br>"
         "▸ Applied NLP sentiment analysis on open-text responses.<br><br>"
         "<b>Outcome:</b> Functional mental health tool providing instant risk screening and wellness recommendations."),
    ]

    for icon, name, featured, summary, tags, color, details in projects:
        badge = " 🌟 FEATURED" if featured else ""
        tag_html = " ".join([f"<span class='tag'>{t}</span>" for t in tags])
        with st.expander(f"{icon}  {name}{badge}  —  {summary}", expanded=featured):
            st.markdown(f"""
            <div style='padding:4px 0;'>
                <div style='margin-bottom:12px;'>{tag_html}</div>
                <div style='color:#aaaacc;line-height:1.85;font-size:0.93rem;'>
                    <b style='color:{color};'>Details</b><br>{details}
                </div>
                <div style='margin-top:14px;'>
                    <a class='link-btn' href='https://github.com/akash0123-pathak' target='_blank'>🐙 View on GitHub</a>
                </div>
            </div>
            """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# 📊 SKILLS
# ══════════════════════════════════════════════════════════════════════════════
elif page == "📊 Skills":
    st.markdown("<div class='sec-title'>📊 Skills & Proficiency</div>", unsafe_allow_html=True)

    skills = {
        "Python": 90, "SQL": 88, "TensorFlow / Keras": 85,
        "Scikit-learn": 85, "LangChain / LangGraph": 83,
        "PyTorch": 79, "Docker": 78, "Tableau": 80,
        "AWS": 75, "MLOps (Learning)": 65,
    }
    df_s = pd.DataFrame(list(skills.items()), columns=["Skill","Level"]).sort_values("Level")
    fig_b = px.bar(df_s, x="Level", y="Skill", orientation='h',
                   color="Level", color_continuous_scale=[[0,"#38bdf8"],[0.5,"#a78bfa"],[1,"#7b7bff"]],
                   range_color=[60,95], text="Level")
    fig_b.update_traces(texttemplate='%{text}%', textposition='outside', marker_line_width=0)
    fig_b.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        font=dict(family='Space Mono,monospace', color='#aaaacc', size=11),
        xaxis=dict(range=[0,108], gridcolor='rgba(120,120,255,0.1)', showticklabels=False),
        yaxis=dict(color='#e2e2f0'),
        coloraxis_showscale=False,
        height=380, margin=dict(l=10,r=55,t=10,b=10)
    )
    st.plotly_chart(fig_b, use_container_width=True)

    st.divider()
    st.markdown("<div class='sub-label'>Skill Categories</div>", unsafe_allow_html=True)

    skill_cats = {
        "🐍 Programming":       ["Python","SQL","OOP","DSA"],
        "🤖 ML / Deep Learning":["Scikit-learn","TensorFlow","Keras","PyTorch"],
        "✨ Generative AI":      ["LangChain","LangGraph","RAG","Prompt Eng","HuggingFace","OpenAI APIs"],
        "⚙️ ML Engineering":    ["ML Pipelines","Model Deployment","Drift Detection","Model Monitoring"],
        "☁️ DevOps / Cloud":    ["Docker","AWS","CI/CD","GitHub"],
        "📦 Data & ETL":        ["Preprocessing","Outlier Detection","ETL Pipelines","Tableau"],
    }
    for cat, items in skill_cats.items():
        tag_html = " ".join([f"<span class='tag'>{t}</span>" for t in items])
        st.markdown(f"""
        <div style='margin-bottom:14px;'>
            <div style='font-family:Space Mono,monospace;font-size:0.68rem;color:#7b7bff;
                 text-transform:uppercase;letter-spacing:2px;margin-bottom:7px;'>{cat}</div>
            {tag_html}
        </div>
        """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# 📜 CERTIFICATIONS
# ══════════════════════════════════════════════════════════════════════════════
elif page == "📜 Certifications":
    st.markdown("<div class='sec-title'>📜 Certifications</div>", unsafe_allow_html=True)

    certs = [
        ("🎓","Machine Learning with Python","FreeCodeCamp","#7b7bff",
         "Covers supervised & unsupervised learning, neural networks, and real-world ML projects using Python and Scikit-learn.",
         ["Python","Scikit-learn","Neural Networks","Classification","Clustering"]),
        ("🔵","Applied Data Science with Python","IBM SkillsBuild","#38bdf8",
         "IBM's applied data science program — Python, data analysis, visualization, ML workflows.",
         ["Python","Pandas","NumPy","Matplotlib","Scikit-learn","Data Analysis"]),
        ("🟣","Python for Data Science & Machine Learning","Udemy","#a78bfa",
         "Full bootcamp: NumPy, Pandas, Seaborn, Scikit-learn and ML algorithms for real-world data science.",
         ["Python","Pandas","Seaborn","Machine Learning","Feature Engineering"]),
        ("📊","Data Science A-Z","Udemy","#f472b6",
         "End-to-end data science — data cleaning, EDA, model building, validation, and communicating results.",
         ["Data Cleaning","EDA","Statistics","SQL","Tableau","Model Building"]),
        ("🔬","Data Analysis Using Python","IBM","#34d399",
         "IBM certification — data wrangling, exploratory analysis, correlation analysis, predictive pipelines.",
         ["Python","Pandas","Data Wrangling","Correlation Analysis","Predictive Modeling"]),
    ]

    for icon, name, issuer, color, desc, skills_list in certs:
        tag_html = " ".join([f"<span class='tag'>{t}</span>" for t in skills_list])
        with st.expander(f"{icon}  {name}  —  {issuer}"):
            st.markdown(f"""
            <div style='padding:4px 0;'>
                <div style='display:flex;align-items:center;gap:10px;margin-bottom:12px;'>
                    <span style='background:rgba(74,222,128,0.1);border:1px solid rgba(74,222,128,0.3);
                         color:#4ade80;border-radius:20px;padding:3px 12px;
                         font-family:Space Mono,monospace;font-size:11px;'>✓ Certified</span>
                    <span style='font-family:Space Mono,monospace;font-size:0.78rem;color:{color};'>{issuer}</span>
                </div>
                <p style='color:#aaaacc;line-height:1.75;font-size:0.92rem;margin-bottom:12px;'>{desc}</p>
                <div><b style='color:{color};font-family:Space Mono,monospace;font-size:0.68rem;'>SKILLS · </b>{tag_html}</div>
            </div>
            """, unsafe_allow_html=True)

    st.divider()
    st.markdown("<div class='sub-label'>My Resume</div>", unsafe_allow_html=True)
    st.markdown(f"""
    <div class='card' style='text-align:center;'>
        <div style='font-size:1.8rem;margin-bottom:10px;'>📋</div>
        <div style='font-weight:700;color:#e2e2f0;font-size:1.05rem;margin-bottom:6px;'>Akash Pathak — Full Resume</div>
        <div style='color:#8888aa;font-size:0.82rem;margin-bottom:18px;'>Hosted on GitHub · Always up to date</div>
        <a class='link-btn-primary' href='{GITHUB_RESUME_VIEW}' target='_blank'>👁️ View Resume</a>
        <a class='link-btn-green' href='{GITHUB_RESUME_URL}' download>⬇️ Download PDF</a>
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# 🤖 AI CHATBOT
# ══════════════════════════════════════════════════════════════════════════════
elif page == "🤖 AI Chatbot":
    st.markdown("<div class='sec-title'>🤖 Ask Akash's AI Assistant</div>", unsafe_allow_html=True)

    # ── Full profile injected directly — no retrieval needed ──────────────────
    AKASH_FULL_PROFILE = """
AKASH PATHAK — COMPLETE PROFILE

CURRENT ROLE: AI/ML Engineer at TCS (Tata Consultancy Services), Indore — May 2025 to present
- Designs end-to-end ML workflows: data preprocessing, feature engineering, model training, deployment, monitoring
- Builds scalable TensorFlow/PyTorch models for classification and intelligent automation
- Containerizes ML services with Docker, implements CI/CD pipelines on AWS
- Monitors production models for data drift and performance degradation

INTERNSHIPS:
1. IBM SkillsBuild — ML Intern (Sep–Nov 2022): Built Random Forest classifiers, feature engineering, cross-validation for mental health prediction
2. DMRC Delhi Metro — Data Science Intern (Jul–Sep 2022): Data cleaning, outlier detection, built Streamlit analytics dashboard

EDUCATION:
- B.Tech CS Engineering (Data Science), Oriental Institute of Science & Technology, Bhopal, 2020–2024, CGPA 8.32
- Class XII: Maharishi Vidya Mandir, Jabalpur — 69.2%
- Class X: Maharishi Vidya Mandir, Jabalpur — CGPA 9.4

PROJECTS (all 6):
1. Enterprise Document Intelligence (RAG) — LangChain, FAISS/Chroma, Python: RAG pipeline for automated knowledge retrieval from PDF/DOCX/TXT
2. Lung Disease Detection — ResNet50, TensorFlow, Keras: Chest X-ray classifier for Normal/Pneumonia/COVID-19
3. Indian Crime Dashboard — Streamlit, Plotly, Pandas: 10+ years India crime data visualization with EDA
4. Smart Streetlight AI — OpenCV, ML, Python: Real-time anomaly detection for streetlight outages and flickering
5. Driver Drowsiness Detection — dlib, OpenCV, EAR algorithm: 30fps fatigue detection with audio/visual alarm
6. Mental Health Tracker — Random Forest, NLP, Scikit-learn: Questionnaire-based wellness risk assessment

SKILLS:
- Programming: Python, SQL, OOP, DSA
- ML/DL: Scikit-learn, TensorFlow, Keras, PyTorch
- GenAI/LLM: LangChain, LangGraph, RAG, Prompt Engineering, HuggingFace, OpenAI APIs
- MLOps: ML Pipelines, Model Deployment, Model Monitoring, Drift Detection
- DevOps/Cloud: Docker, AWS, CI/CD, GitHub
- Data/Visualization: Pandas, NumPy, Tableau, Streamlit, ETL Pipelines

CERTIFICATIONS:
1. Machine Learning with Python — FreeCodeCamp
2. Applied Data Science with Python — IBM SkillsBuild
3. Python for Data Science and Machine Learning — Udemy
4. Data Science A-Z — Udemy
5. Data Analysis Using Python — IBM

CONTACT:
- Email: akash.pathak0123@gmail.com
- Phone: +91 7024426415
- LinkedIn: linkedin.com/in/akash-pathak-44a082212
- GitHub: github.com/akash0123-pathak
- Location: Indore, India (originally from Chhatapur)
- Open to: Generative AI, MLOps, LLM Engineering, AI Products — remote or hybrid
"""

    BASE_SYSTEM = """You are a friendly AI assistant on Akash Pathak's portfolio website.

RULES:
- For greetings (hi, hello, hey): respond warmly e.g. "Hi! I'm Akash's AI assistant. Ask me about his skills, experience, projects, or education!"
- For questions: answer DIRECTLY and COMPLETELY using only the profile facts
- NEVER cut off mid-word or mid-sentence — always finish completely
- NEVER generate follow-up questions
- NEVER say "If you have any specific questions..."
- For personal/unrelated questions: "I only cover Akash's professional profile — skills, experience, projects, education, and contact info."
- Keep answers concise but complete — finish every sentence fully"""

    def build_prompt(query):
        """Inject full profile into system prompt for accurate answers."""
        return f"{BASE_SYSTEM}\n\nAKASH'S COMPLETE PROFILE:\n{AKASH_FULL_PROFILE}"

    # ── Layer 1: Groq (Llama 3, free, fast) ───────────────────────────────────
    def ask_groq(query, history):
        try:
            try:
                api_key = st.secrets["GROQ_API_KEY"]
            except Exception:
                api_key = ""
            if not api_key:
                return None, "no_key"
            resp = requests.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
                json={
                    "model": "llama-3.1-8b-instant",
                    "messages": [{"role": "system", "content": build_prompt(query)}] + history,
                    "max_tokens": 600,
                    "temperature": 0.5,
                },
                timeout=20
            )
            data = resp.json()
            if "choices" in data:
                return data["choices"][0]["message"]["content"].strip(), "groq"
            # Return actual error so we can see it
            err = data.get("error", {}).get("message", str(data))
            return err, "groq_error"
        except Exception as e:
            return str(e), "groq_fail"

    # ── Router ─────────────────────────────────────────────────────────────────
    def get_answer(query, history):
        reply, source = ask_groq(query, history)
        if source == "groq":
            return reply, "⚡ Llama 3"
        # Show actual error for debugging
        return f"❌ Groq error: {reply}", source

    # ── Chat UI ────────────────────────────────────────────────────────────────
    # Show key status
    try:
        _k = st.secrets["GROQ_API_KEY"]
        _key_ok = bool(_k and len(_k) > 10)
    except Exception:
        _key_ok = False

    if not _key_ok:
        st.error("⚠️ GROQ_API_KEY not found. Add it in Streamlit → Settings → Secrets → GROQ_API_KEY = \"gsk_...\"")



    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "last_source" not in st.session_state:
        st.session_state.last_source = ""

    if not st.session_state.chat_history:
        st.markdown(
            "<div class='chat-bot'>👋 Hi! I'm Akash's AI assistant. "
            "Ask me anything about his experience, skills, projects, or contact info!</div>",
            unsafe_allow_html=True
        )

    for msg in st.session_state.chat_history:
        css = "chat-user" if msg["role"] == "user" else "chat-bot"
        prefix = "🧑" if msg["role"] == "user" else "🤖"
        st.markdown(f"<div class='{css}'>{prefix} {msg['content']}</div>", unsafe_allow_html=True)

    # Show which model answered last
    if st.session_state.last_source:
        st.markdown(
            f"<div style='font-family:Space Mono,monospace;font-size:0.65rem;"
            f"color:#555577;margin:4px 0 12px;'>answered by {st.session_state.last_source}</div>",
            unsafe_allow_html=True
        )

    with st.form("chat_form", clear_on_submit=True):
        c_in, c_btn = st.columns([5, 1])
        with c_in:
            typed = st.text_input("Message", placeholder="Ask anything about Akash...", label_visibility="collapsed")
        with c_btn:
            sent = st.form_submit_button("Send")

    if sent and typed.strip():
        # Append user message FIRST so history is always up to date
        st.session_state.chat_history.append({"role": "user", "content": typed.strip()})
        # Build history for API: last 6 messages (already includes the new user msg)
        hist = st.session_state.chat_history[-6:]
        with st.spinner("⚡ Thinking..."):
            reply, source = get_answer(typed.strip(), hist)
        st.session_state.chat_history.append({"role": "assistant", "content": reply})
        st.session_state.last_source = source
        st.rerun()

    if st.session_state.chat_history:
        if st.button("🗑️ Clear Chat"):
            st.session_state.chat_history = []
            st.session_state.last_source = ""
            st.rerun()




# ══════════════════════════════════════════════════════════════════════════════
# 📞 CONTACT
# ══════════════════════════════════════════════════════════════════════════════
elif page == "📞 Contact":
    st.markdown("<div class='sec-title'>📞 Contact</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class='card'>
        <div class='sub-label'>Get In Touch</div>
        <div style='margin-top:14px;line-height:2.2;font-size:0.95rem;'>
            <span style='color:#555577;font-family:Space Mono,monospace;font-size:0.75rem;'>EMAIL</span><br>
            <a href='mailto:akash.pathak0123@gmail.com' style='color:#e2e2f0;text-decoration:none;'>
                akash.pathak0123@gmail.com
            </a><br><br>
            <span style='color:#555577;font-family:Space Mono,monospace;font-size:0.75rem;'>PHONE</span><br>
            <span style='color:#e2e2f0;'>+91 7024426415</span><br><br>
            <span style='color:#555577;font-family:Space Mono,monospace;font-size:0.75rem;'>LOCATION</span><br>
            <span style='color:#e2e2f0;'>📍 Indore / Chhatapur, India</span>
        </div>
        <div style='margin-top:20px;'>
            <a class='link-btn' href='https://www.linkedin.com/in/akash-pathak-44a082212' target='_blank'>🔗 LinkedIn</a>
            <a class='link-btn' href='https://github.com/akash0123-pathak' target='_blank'>🐙 GitHub</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='card'>
        <div class='sub-label'>Availability</div>
        <div style='margin-top:14px;'>
            <span style='color:#4ade80;font-size:1.1rem;'>●</span>
            <span style='color:#e2e2f0;margin-left:8px;'>Open to new opportunities</span>
        </div>
        <p style='color:#8888aa;font-size:0.9rem;line-height:1.75;margin-top:12px;'>
        Currently at TCS as AI/ML Engineer and exploring roles in
        <b style='color:#a78bfa;'>Generative AI</b>, <b style='color:#38bdf8;'>MLOps</b>,
        and <b style='color:#7b7bff;'>LLM Engineering</b>.
        </p>
        <div style='margin-top:14px;'>
            <span class='tag'>GenAI Applications</span>
            <span class='tag'>MLOps</span>
            <span class='tag'>LLM Engineering</span>
            <span class='tag'>AI Products</span>
            <span class='tag'>Remote / Hybrid</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
