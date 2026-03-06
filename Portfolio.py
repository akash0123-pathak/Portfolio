import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import time
import requests

# ─── CONFIG: Update your GitHub raw resume link here ──────────────────────────
# Upload your resume PDF to GitHub, then paste the raw URL below
GITHUB_RESUME_URL = "https://raw.githubusercontent.com/akash0123-pride/akash0123-pride/main/Akash_Pathak_Resume.pdf"
GITHUB_RESUME_VIEW = "https://github.com/akash0123-pride/akash0123-pride/blob/main/Akash_Pathak_Resume.pdf"

# ─── Page Config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Akash Pathak | AI/ML Engineer",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─── Global CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Syne:wght@400;600;700;800&display=swap');

/* Reset & base */
html, body, [class*="css"] {
    font-family: 'Syne', sans-serif;
    background-color: #050510;
    color: #e2e2f0;
}

/* Animated gradient background */
.stApp {
    background: linear-gradient(135deg, #050510 0%, #0a0a2e 50%, #050510 100%);
    background-size: 400% 400%;
    animation: gradientShift 12s ease infinite;
}

@keyframes gradientShift {
    0%   { background-position: 0% 50%; }
    50%  { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: rgba(10, 10, 40, 0.95) !important;
    border-right: 1px solid rgba(100, 100, 255, 0.2);
}
[data-testid="stSidebar"] * { color: #e2e2f0 !important; }

/* Navigation radio */
.stRadio label {
    font-family: 'Space Mono', monospace !important;
    font-size: 13px !important;
    color: #aaaacc !important;
    transition: color 0.2s;
}
.stRadio label:hover { color: #7b7bff !important; }

/* Section cards */
.card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(120,120,255,0.15);
    border-radius: 16px;
    padding: 28px 32px;
    margin-bottom: 24px;
    transition: border-color 0.3s, box-shadow 0.3s;
}
.card:hover {
    border-color: rgba(120,120,255,0.45);
    box-shadow: 0 0 30px rgba(100,100,255,0.08);
}

/* Glowing title */
.glow-title {
    font-family: 'Syne', sans-serif;
    font-size: 3.2rem;
    font-weight: 800;
    background: linear-gradient(90deg, #7b7bff, #a78bfa, #38bdf8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: shimmer 3s linear infinite;
    background-size: 200%;
}
@keyframes shimmer {
    0%   { background-position: 0%; }
    100% { background-position: 200%; }
}

/* Sub-heading */
.sub-heading {
    font-family: 'Space Mono', monospace;
    font-size: 1rem;
    color: #7b7bff;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 8px;
}

/* Section title */
.section-title {
    font-family: 'Syne', sans-serif;
    font-size: 2rem;
    font-weight: 800;
    color: #e2e2f0;
    margin-bottom: 24px;
    padding-bottom: 12px;
    border-bottom: 2px solid rgba(120,120,255,0.3);
}

/* Tag pills */
.tag {
    display: inline-block;
    background: rgba(120,120,255,0.12);
    border: 1px solid rgba(120,120,255,0.3);
    color: #a78bfa;
    border-radius: 20px;
    padding: 4px 14px;
    font-family: 'Space Mono', monospace;
    font-size: 11px;
    margin: 3px;
}

/* Stat boxes */
.stat-box {
    background: linear-gradient(135deg, rgba(120,120,255,0.1), rgba(56,189,248,0.05));
    border: 1px solid rgba(120,120,255,0.25);
    border-radius: 12px;
    padding: 20px;
    text-align: center;
}
.stat-number {
    font-family: 'Space Mono', monospace;
    font-size: 2rem;
    font-weight: 700;
    color: #7b7bff;
}
.stat-label {
    font-size: 0.75rem;
    color: #8888aa;
    text-transform: uppercase;
    letter-spacing: 2px;
    margin-top: 4px;
}

/* Timeline */
.timeline-item {
    border-left: 2px solid rgba(120,120,255,0.4);
    padding-left: 20px;
    margin-bottom: 28px;
    position: relative;
}
.timeline-item::before {
    content: '';
    width: 10px; height: 10px;
    background: #7b7bff;
    border-radius: 50%;
    position: absolute;
    left: -6px; top: 4px;
    box-shadow: 0 0 10px rgba(120,120,255,0.6);
}

/* Chatbot */
.chat-message-user {
    background: rgba(120,120,255,0.15);
    border: 1px solid rgba(120,120,255,0.3);
    border-radius: 12px 12px 2px 12px;
    padding: 12px 16px;
    margin: 8px 0;
    text-align: right;
    font-size: 0.9rem;
}
.chat-message-bot {
    background: rgba(56,189,248,0.08);
    border: 1px solid rgba(56,189,248,0.2);
    border-radius: 2px 12px 12px 12px;
    padding: 12px 16px;
    margin: 8px 0;
    font-size: 0.9rem;
    font-family: 'Space Mono', monospace;
}

/* Buttons */
.stButton>button {
    background: linear-gradient(135deg, #7b7bff, #a78bfa) !important;
    color: white !important;
    border: none !important;
    border-radius: 8px !important;
    font-family: 'Space Mono', monospace !important;
    font-size: 13px !important;
    padding: 10px 24px !important;
    transition: box-shadow 0.2s !important;
}
.stButton>button:hover {
    box-shadow: 0 0 20px rgba(120,120,255,0.4) !important;
}

/* Input fields */
.stTextInput>div>div>input, .stTextArea textarea {
    background: rgba(255,255,255,0.04) !important;
    border: 1px solid rgba(120,120,255,0.3) !important;
    border-radius: 8px !important;
    color: #e2e2f0 !important;
    font-family: 'Space Mono', monospace !important;
}

/* Hide default Streamlit elements */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 2rem !important; }

/* Expander styling */
[data-testid="stExpander"] {
    background: rgba(255,255,255,0.02) !important;
    border: 1px solid rgba(120,120,255,0.2) !important;
    border-radius: 12px !important;
    margin-bottom: 10px !important;
}
[data-testid="stExpander"]:hover {
    border-color: rgba(120,120,255,0.45) !important;
}
[data-testid="stExpander"] summary {
    font-family: 'Syne', sans-serif !important;
    font-size: 0.95rem !important;
    font-weight: 600 !important;
    color: #e2e2f0 !important;
    padding: 14px 18px !important;
}
[data-testid="stExpanderDetails"] {
    border-top: 1px solid rgba(120,120,255,0.15) !important;
    padding: 16px 18px !important;
}

/* Spinner */
.stSpinner > div { border-top-color: #7b7bff !important; }

/* Pulse animation for avatar */
@keyframes pulse {
    0%, 100% { box-shadow: 0 0 0 0 rgba(123,123,255,0.4); }
    50%       { box-shadow: 0 0 0 20px rgba(123,123,255,0); }
}
.avatar {
    animation: pulse 2.5s infinite;
    border-radius: 50%;
    border: 3px solid #7b7bff;
    padding: 3px;
}

/* Project card hover */
.project-card {
    background: rgba(255,255,255,0.02);
    border: 1px solid rgba(120,120,255,0.15);
    border-radius: 14px;
    padding: 22px 26px;
    margin-bottom: 16px;
    transition: all 0.3s;
}
.project-card:hover {
    background: rgba(120,120,255,0.07);
    border-color: rgba(120,120,255,0.4);
    transform: translateY(-2px);
}
</style>
""", unsafe_allow_html=True)


# ─── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style='text-align:center; padding: 20px 0 10px;'>
        <div style='width:80px; height:80px; border-radius:50%; background:linear-gradient(135deg,#7b7bff,#38bdf8);
             margin:0 auto; display:flex; align-items:center; justify-content:center;
             font-size:2rem; border: 3px solid rgba(120,120,255,0.5);
             box-shadow: 0 0 20px rgba(120,120,255,0.3);'>🤖</div>
        <div style='margin-top:12px; font-family:Syne,sans-serif; font-size:1.1rem; font-weight:700; color:#e2e2f0;'>Akash Pathak</div>
        <div style='font-family:Space Mono,monospace; font-size:0.7rem; color:#7b7bff; letter-spacing:2px; margin-top:4px;'>AI/ML ENGINEER</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<hr style='border-color:rgba(120,120,255,0.2); margin:10px 0 20px;'>", unsafe_allow_html=True)

    page = st.radio("", [
        "🏠 Home",
        "🎓 Education",
        "💼 Experience",
        "🚀 Projects",
        "📊 Skills",
        "📜 Certifications",
        "🤖 AI Chatbot",
        "📞 Contact"
    ], index=0)

    st.markdown("<hr style='border-color:rgba(120,120,255,0.2); margin:20px 0 10px;'>", unsafe_allow_html=True)
    st.markdown("""
    <div style='text-align:center; font-family:Space Mono,monospace; font-size:0.65rem; color:#555577;'>
        AVAILABLE FOR WORK<br>
        <span style='color:#4ade80; font-size:0.7rem;'>● Open to Opportunities</span>
    </div>
    """, unsafe_allow_html=True)


# ─── Home ──────────────────────────────────────────────────────────────────────
if page == "🏠 Home":
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("<div class='sub-heading'>AI / ML ENGINEER · DATA SCIENCE</div>", unsafe_allow_html=True)
        st.markdown("<div class='glow-title'>Akash Pathak</div>", unsafe_allow_html=True)
        st.markdown("""
        <p style='font-size:1.1rem; color:#aaaacc; max-width:600px; line-height:1.8; margin-top:16px;'>
        Building intelligent systems that learn, adapt, and solve real-world problems.
        From scalable ML pipelines to GenAI-powered applications — I bridge research and production.
        </p>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div style='display:flex; gap:12px; flex-wrap:wrap; margin-top:20px;'>
            <a href='https://www.linkedin.com/in/akash-pathak-44a082212' target='_blank'
               style='background:rgba(120,120,255,0.15); border:1px solid rgba(120,120,255,0.35);
               border-radius:8px; padding:10px 20px; color:#a78bfa; text-decoration:none;
               font-family:Space Mono,monospace; font-size:12px;'>🔗 LinkedIn</a>
            <a href='https://github.com/akash0123-pride' target='_blank'
               style='background:rgba(120,120,255,0.15); border:1px solid rgba(120,120,255,0.35);
               border-radius:8px; padding:10px 20px; color:#a78bfa; text-decoration:none;
               font-family:Space Mono,monospace; font-size:12px;'>🐙 GitHub</a>
            <a href='{GITHUB_RESUME_VIEW}' target='_blank'
               style='background:linear-gradient(135deg,#7b7bff,#a78bfa); border-radius:8px;
               padding:10px 20px; color:white; text-decoration:none;
               font-family:Space Mono,monospace; font-size:12px;'>📄 View Resume</a>
            <a href='{GITHUB_RESUME_URL}' download
               style='background:rgba(74,222,128,0.15); border:1px solid rgba(74,222,128,0.35);
               border-radius:8px; padding:10px 20px; color:#4ade80; text-decoration:none;
               font-family:Space Mono,monospace; font-size:12px;'>⬇️ Download</a>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style='background:linear-gradient(135deg,rgba(120,120,255,0.08),rgba(56,189,248,0.05));
             border:1px solid rgba(120,120,255,0.2); border-radius:16px; padding:24px; text-align:center;'>
            <div style='font-family:Space Mono,monospace; font-size:0.7rem; color:#555577;
                 text-transform:uppercase; letter-spacing:2px; margin-bottom:16px;'>QUICK STATS</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='height:32px;'></div>", unsafe_allow_html=True)

    # Stats row
    s1, s2, s3, s4 = st.columns(4)
    stats = [
        ("1+", "Year at TCS"),
        ("6+", "Projects Built"),
        ("3", "Certifications"),
        ("8.32", "CGPA"),
    ]
    for col, (num, label) in zip([s1, s2, s3, s4], stats):
        with col:
            st.markdown(f"""
            <div class='stat-box'>
                <div class='stat-number'>{num}</div>
                <div class='stat-label'>{label}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<div style='height:32px;'></div>", unsafe_allow_html=True)

    # Tech stack highlights
    st.markdown("<div class='sub-heading' style='margin-top:8px;'>CORE STACK</div>", unsafe_allow_html=True)
    tags = ["Python", "TensorFlow", "PyTorch", "LangChain", "LangGraph", "RAG", "Hugging Face",
            "Docker", "AWS", "Streamlit", "MLOps", "OpenAI APIs", "Scikit-learn", "SQL"]
    st.markdown("".join([f"<span class='tag'>{t}</span>" for t in tags]), unsafe_allow_html=True)

    st.markdown("<div style='height:32px;'></div>", unsafe_allow_html=True)

    # Radar chart – skill categories
    st.markdown("<div class='sub-heading'>CAPABILITY RADAR</div>", unsafe_allow_html=True)
    categories = ["ML/DL", "Generative AI", "MLOps", "Data Engineering", "Cloud/DevOps", "Programming"]
    values = [88, 85, 78, 82, 75, 90]
    fig_radar = go.Figure(go.Scatterpolar(
        r=values + [values[0]],
        theta=categories + [categories[0]],
        fill='toself',
        fillcolor='rgba(123,123,255,0.15)',
        line=dict(color='#7b7bff', width=2),
        marker=dict(color='#a78bfa', size=8)
    ))
    fig_radar.update_layout(
        polar=dict(
            bgcolor='rgba(0,0,0,0)',
            radialaxis=dict(visible=True, range=[0, 100], color='#555577', gridcolor='rgba(120,120,255,0.15)'),
            angularaxis=dict(color='#aaaacc', gridcolor='rgba(120,120,255,0.15)')
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(family='Space Mono, monospace', color='#aaaacc'),
        height=380,
        margin=dict(l=60, r=60, t=30, b=30)
    )
    st.plotly_chart(fig_radar, use_container_width=True)


# ─── Education ─────────────────────────────────────────────────────────────────
elif page == "🎓 Education":
    st.markdown("<div class='section-title'>🎓 Education</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class='card'>
        <div style='display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap;'>
            <div>
                <div style='font-size:1.2rem; font-weight:700; color:#e2e2f0;'>B.Tech — Computer Science Engineering (Data Science)</div>
                <div style='color:#7b7bff; font-family:Space Mono,monospace; font-size:0.85rem; margin-top:6px;'>Oriental Institute of Science & Technology, Bhopal</div>
            </div>
            <div style='text-align:right;'>
                <span class='tag'>2020 – 2024</span><br>
                <span style='font-family:Space Mono,monospace; font-size:1.1rem; color:#4ade80; font-weight:700;'>CGPA 8.32</span>
            </div>
        </div>
        <div style='margin-top:14px; color:#8888aa; font-size:0.9rem; line-height:1.7;'>
            Specialized in Data Science track covering Machine Learning, Deep Learning, Statistical Analysis, Big Data technologies, and AI system design.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='card'>
        <div style='display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap;'>
            <div>
                <div style='font-size:1.2rem; font-weight:700; color:#e2e2f0;'>Intermediate (Class XII)</div>
                <div style='color:#7b7bff; font-family:Space Mono,monospace; font-size:0.85rem; margin-top:6px;'>Maharishi Vidya Mandir, Jabalpur</div>
            </div>
            <div style='text-align:right;'>
                <span style='font-family:Space Mono,monospace; font-size:1.1rem; color:#38bdf8; font-weight:700;'>69.2%</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='card'>
        <div style='display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap;'>
            <div>
                <div style='font-size:1.2rem; font-weight:700; color:#e2e2f0;'>High School (Class X)</div>
                <div style='color:#7b7bff; font-family:Space Mono,monospace; font-size:0.85rem; margin-top:6px;'>Maharishi Vidya Mandir, Jabalpur</div>
            </div>
            <div style='text-align:right;'>
                <span style='font-family:Space Mono,monospace; font-size:1.1rem; color:#4ade80; font-weight:700;'>CGPA 9.4</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ─── Experience ────────────────────────────────────────────────────────────────
elif page == "💼 Experience":
    st.markdown("<div class='section-title'>💼 Work Experience & Internships</div>", unsafe_allow_html=True)

    # Career Timeline chart
    st.markdown("<div class='sub-heading'>CAREER TIMELINE</div>", unsafe_allow_html=True)
    timeline_data = pd.DataFrame([
        dict(Task="DMRC – Data Science Intern", Start="2022-07-01", Finish="2022-09-30", Resource="Internship"),
        dict(Task="IBM SkillsBuild – ML Intern", Start="2022-09-01", Finish="2022-11-30", Resource="Internship"),
        dict(Task="TCS – AI/ML Engineer", Start="2025-05-01", Finish="2026-03-06", Resource="Full-Time"),
    ])
    fig_timeline = px.timeline(
        timeline_data, x_start="Start", x_end="Finish", y="Task", color="Resource",
        color_discrete_map={"Internship": "#a78bfa", "Full-Time": "#7b7bff"}
    )
    fig_timeline.update_yaxes(autorange="reversed")
    fig_timeline.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        font=dict(family='Space Mono, monospace', color='#aaaacc'),
        xaxis=dict(gridcolor='rgba(120,120,255,0.1)', color='#aaaacc'),
        yaxis=dict(gridcolor='rgba(120,120,255,0.1)', color='#aaaacc'),
        legend=dict(bgcolor='rgba(0,0,0,0)', bordercolor='rgba(120,120,255,0.2)'),
        height=220, margin=dict(l=20, r=20, t=10, b=20)
    )
    st.plotly_chart(fig_timeline, use_container_width=True)

    st.markdown("<div class='sub-heading' style='margin:24px 0 16px;'>FULL-TIME ROLES</div>", unsafe_allow_html=True)

    # TCS
    with st.expander("🟣  AI/ML Engineer — Tata Consultancy Services (TCS)  |  May 2025 – Present  📍 Indore", expanded=True):
        st.markdown("""
        <div style='padding:8px 4px;'>
        <div style='display:flex; gap:8px; flex-wrap:wrap; margin-bottom:16px;'>
            <span class='tag'>TensorFlow</span><span class='tag'>Docker</span><span class='tag'>AWS</span>
            <span class='tag'>CI/CD</span><span class='tag'>MLOps</span><span class='tag'>Model Monitoring</span>
            <span class='tag'>Python</span><span class='tag'>Drift Detection</span>
        </div>
        <div style='color:#aaaacc; line-height:1.9; font-size:0.95rem;'>
        <b style='color:#7b7bff;'>Key Responsibilities:</b><br>
        ▸ Designed end-to-end ML workflows including preprocessing, feature engineering, model training, deployment, and monitoring.<br>
        ▸ Built scalable TensorFlow models improving classification accuracy and enabling automated decision workflows.<br>
        ▸ Developed intelligent automation systems reducing manual intervention through ML-driven decision engines.<br>
        ▸ Containerized ML services using Docker and implemented CI/CD pipelines for AWS deployments.<br>
        ▸ Monitored production models for data drift, performance degradation, and reliability.<br><br>
        <b style='color:#7b7bff;'>Impact:</b><br>
        ▸ Reduced manual intervention significantly through automated ML decision engines.<br>
        ▸ Improved model reliability via proactive drift detection and monitoring pipelines.
        </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div class='sub-heading' style='margin:24px 0 16px;'>INTERNSHIPS</div>", unsafe_allow_html=True)

    # IBM
    with st.expander("🔵  Machine Learning Intern — IBM SkillsBuild  |  Sep 2022 – Nov 2022  📍 Remote (Virtual)"):
        st.markdown("""
        <div style='padding:8px 4px;'>
        <div style='display:flex; gap:8px; flex-wrap:
