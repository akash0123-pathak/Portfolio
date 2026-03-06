import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import time
import requests

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

        st.markdown("""
        <div style='display:flex; gap:12px; flex-wrap:wrap; margin-top:20px;'>
            <a href='https://www.linkedin.com/in/akash-pathak-44a082212' target='_blank'
               style='background:rgba(120,120,255,0.15); border:1px solid rgba(120,120,255,0.35);
               border-radius:8px; padding:10px 20px; color:#a78bfa; text-decoration:none;
               font-family:Space Mono,monospace; font-size:12px;'>🔗 LinkedIn</a>
            <a href='https://github.com/akash0123-pride' target='_blank'
               style='background:rgba(120,120,255,0.15); border:1px solid rgba(120,120,255,0.35);
               border-radius:8px; padding:10px 20px; color:#a78bfa; text-decoration:none;
               font-family:Space Mono,monospace; font-size:12px;'>🐙 GitHub</a>
            <a href='https://drive.google.com/file/d/1zfMTKiAvqE5uA0tvJwtWZOinsdrkwSAw/view' target='_blank'
               style='background:linear-gradient(135deg,#7b7bff,#a78bfa); border-radius:8px;
               padding:10px 20px; color:white; text-decoration:none;
               font-family:Space Mono,monospace; font-size:12px;'>📄 Resume</a>
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
    st.markdown("<div class='section-title'>💼 Work Experience</div>", unsafe_allow_html=True)

    experiences = [
        {
            "role": "AI/ML Engineer",
            "company": "Tata Consultancy Services (TCS)",
            "period": "May 2025 – Present",
            "location": "Indore",
            "color": "#7b7bff",
            "points": [
                "Designed end-to-end ML workflows including preprocessing, feature engineering, model training, deployment, and monitoring.",
                "Built scalable TensorFlow models improving classification accuracy and enabling automated decision workflows.",
                "Developed intelligent automation systems reducing manual intervention through ML-driven decision engines.",
                "Containerized ML services using Docker and implemented CI/CD pipelines for AWS deployments.",
                "Monitored production models for data drift, performance degradation, and reliability."
            ],
            "tags": ["TensorFlow", "Docker", "AWS", "CI/CD", "MLOps", "Model Monitoring"]
        },
        {
            "role": "Machine Learning Intern",
            "company": "IBM SkillsBuild (Virtual)",
            "period": "Sep 2022 – Nov 2022",
            "location": "Remote",
            "color": "#38bdf8",
            "points": [
                "Built supervised ML models including Random Forest for structured data classification.",
                "Performed preprocessing, feature engineering, cross-validation, and performance optimization."
            ],
            "tags": ["Random Forest", "Scikit-learn", "Feature Engineering", "Cross-Validation"]
        },
        {
            "role": "Data Science Intern",
            "company": "Delhi Metro Rail Corporation Limited (DMRC)",
            "period": "Jul 2022 – Sep 2022",
            "location": "Delhi",
            "color": "#a78bfa",
            "points": [
                "Performed data cleaning, missing value handling, and outlier detection for analytics pipelines.",
                "Developed a Streamlit-based application for structured data collection and visualization."
            ],
            "tags": ["Python", "Pandas", "Streamlit", "Data Cleaning", "Analytics"]
        },
    ]

    for exp in experiences:
        bullet_html = "".join([f"<li style='margin-bottom:8px; color:#aaaacc;'>{p}</li>" for p in exp['points']])
        tag_html = "".join([f"<span class='tag'>{t}</span>" for t in exp['tags']])
        st.markdown(f"""
        <div class='card'>
            <div style='display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; margin-bottom:12px;'>
                <div>
                    <div style='font-size:1.2rem; font-weight:700; color:#e2e2f0;'>{exp['role']}</div>
                    <div style='color:{exp['color']}; font-family:Space Mono,monospace; font-size:0.85rem; margin-top:4px;'>{exp['company']}</div>
                </div>
                <div style='text-align:right;'>
                    <span class='tag'>{exp['period']}</span><br>
                    <span style='font-size:0.8rem; color:#555577;'>📍 {exp['location']}</span>
                </div>
            </div>
            <ul style='padding-left:20px; margin:12px 0;'>{bullet_html}</ul>
            <div style='margin-top:14px;'>{tag_html}</div>
        </div>
        """, unsafe_allow_html=True)

    # Timeline chart
    st.markdown("<div class='sub-heading' style='margin-top:8px;'>CAREER TIMELINE</div>", unsafe_allow_html=True)
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


# ─── Projects ──────────────────────────────────────────────────────────────────
elif page == "🚀 Projects":
    st.markdown("<div class='section-title'>🚀 Projects</div>", unsafe_allow_html=True)

    projects = [
        {
            "name": "Enterprise Document Intelligence System (RAG)",
            "icon": "🧠",
            "desc": "Built a Retrieval-Augmented Generation system using LangChain and vector similarity search for automated knowledge retrieval from enterprise documents.",
            "tags": ["LangChain", "RAG", "Vector DB", "LLM", "Python"],
            "highlight": True
        },
        {
            "name": "Lung Disease Detection",
            "icon": "🫁",
            "desc": "Developed a ResNet-based TensorFlow model for classifying lung diseases from chest X-ray images with high accuracy and performance optimization techniques.",
            "tags": ["TensorFlow", "ResNet", "Deep Learning", "Image Classification"],
            "highlight": False
        },
        {
            "name": "Indian Crime Dashboard",
            "icon": "📊",
            "desc": "Built an interactive analytics dashboard using Python, Pandas, and Streamlit to visualize crime trends across India, with EDA and actionable insights.",
            "tags": ["Streamlit", "Pandas", "Plotly", "EDA", "Data Visualization"],
            "highlight": False
        },
        {
            "name": "Smart Streetlight AI System",
            "icon": "💡",
            "desc": "Computer vision-based monitoring system using Python and ML for automated anomaly detection and real-time analytics on streetlight infrastructure.",
            "tags": ["OpenCV", "Computer Vision", "Python", "Anomaly Detection"],
            "highlight": False
        },
        {
            "name": "Driver Drowsiness Detection",
            "icon": "🚗",
            "desc": "Real-time system using OpenCV and ML to detect driver drowsiness and trigger alerts, improving road safety.",
            "tags": ["OpenCV", "ML", "Python", "Real-Time"],
            "highlight": False
        },
        {
            "name": "Mental Health Tracker",
            "icon": "💚",
            "desc": "Application that analyzes user responses to track and provide insights about mental wellness patterns using ML.",
            "tags": ["Python", "ML", "Streamlit", "NLP"],
            "highlight": False
        },
    ]

    col_a, col_b = st.columns(2)
    for i, proj in enumerate(projects):
        col = col_a if i % 2 == 0 else col_b
        tag_html = "".join([f"<span class='tag'>{t}</span>" for t in proj['tags']])
        border = "rgba(120,120,255,0.4)" if proj['highlight'] else "rgba(120,120,255,0.15)"
        bg = "rgba(120,120,255,0.06)" if proj['highlight'] else "rgba(255,255,255,0.02)"
        badge = "<span style='background:#7b7bff; color:white; border-radius:4px; padding:2px 8px; font-size:0.65rem; font-family:Space Mono,monospace; margin-left:8px;'>FEATURED</span>" if proj['highlight'] else ""
        with col:
            st.markdown(f"""
            <div style='background:{bg}; border:1px solid {border}; border-radius:14px; padding:22px 26px; margin-bottom:16px;'>
                <div style='font-size:1.1rem; font-weight:700; color:#e2e2f0; margin-bottom:8px;'>
                    {proj['icon']} {proj['name']}{badge}
                </div>
                <p style='color:#8888aa; font-size:0.88rem; line-height:1.7; margin-bottom:14px;'>{proj['desc']}</p>
                <div>{tag_html}</div>
            </div>
            """, unsafe_allow_html=True)


# ─── Skills ────────────────────────────────────────────────────────────────────
elif page == "📊 Skills":
    st.markdown("<div class='section-title'>📊 Skills & Proficiency</div>", unsafe_allow_html=True)

    col1, col2 = st.columns([3, 2])

    with col1:
        skills = {
            "Python": 90,
            "SQL": 88,
            "TensorFlow / Keras": 85,
            "Scikit-learn": 85,
            "LangChain / LangGraph": 82,
            "PyTorch": 78,
            "Docker": 78,
            "Tableau": 80,
            "AWS": 75,
            "MLOps (Learning)": 65,
        }
        df_skills = pd.DataFrame(list(skills.items()), columns=["Skill", "Level"])
        df_skills = df_skills.sort_values("Level", ascending=True)

        fig_bar = px.bar(
            df_skills, x="Level", y="Skill", orientation='h',
            color="Level", color_continuous_scale=[[0, "#38bdf8"], [0.5, "#a78bfa"], [1, "#7b7bff"]],
            range_color=[60, 95], text="Level"
        )
        fig_bar.update_traces(texttemplate='%{text}%', textposition='outside', marker_line_width=0)
        fig_bar.update_layout(
            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
            font=dict(family='Space Mono, monospace', color='#aaaacc', size=12),
            xaxis=dict(range=[0, 105], gridcolor='rgba(120,120,255,0.1)', color='#aaaacc', showticklabels=False),
            yaxis=dict(gridcolor='rgba(0,0,0,0)', color='#e2e2f0'),
            coloraxis_showscale=False,
            height=400, margin=dict(l=20, r=60, t=10, b=20)
        )
        st.plotly_chart(fig_bar, use_container_width=True)

    with col2:
        skill_categories = {
            "Programming": ["Python", "SQL", "OOP", "DSA"],
            "ML / DL": ["Scikit-learn", "TensorFlow", "Keras", "PyTorch"],
            "Generative AI": ["LangChain", "LangGraph", "RAG", "Prompt Eng", "Hugging Face", "OpenAI APIs"],
            "ML Engineering": ["ML Pipelines", "Model Deployment", "Drift Detection", "Model Monitoring"],
            "DevOps / Cloud": ["Docker", "AWS", "CI/CD", "GitHub"],
            "Data & ETL": ["Preprocessing", "Outlier Detection", "ETL Pipelines", "Tableau"],
        }
        for cat, items in skill_categories.items():
            tag_html = "".join([f"<span class='tag'>{t}</span>" for t in items])
            st.markdown(f"""
            <div style='margin-bottom:16px;'>
                <div style='font-family:Space Mono,monospace; font-size:0.7rem; color:#7b7bff;
                     text-transform:uppercase; letter-spacing:2px; margin-bottom:8px;'>{cat}</div>
                <div>{tag_html}</div>
            </div>
            """, unsafe_allow_html=True)


# ─── Certifications ────────────────────────────────────────────────────────────
elif page == "📜 Certifications":
    st.markdown("<div class='section-title'>📜 Certifications</div>", unsafe_allow_html=True)

    certs = [
        {"name": "Machine Learning with Python", "issuer": "FreeCodeCamp", "icon": "🎓", "color": "#7b7bff"},
        {"name": "Applied Data Science with Python", "issuer": "IBM SkillsBuild", "icon": "🔵", "color": "#38bdf8"},
        {"name": "Python for Data Science and Machine Learning", "issuer": "Udemy", "icon": "🟣", "color": "#a78bfa"},
        {"name": "Data Science A-Z", "issuer": "Udemy", "icon": "📊", "color": "#f472b6"},
        {"name": "Data Analysis Using Python", "issuer": "IBM", "icon": "🔬", "color": "#34d399"},
    ]

    col1, col2 = st.columns(2)
    for i, cert in enumerate(certs):
        col = col1 if i % 2 == 0 else col2
        with col:
            st.markdown(f"""
            <div class='card' style='border-left:3px solid {cert['color']};'>
                <div style='font-size:1.5rem; margin-bottom:8px;'>{cert['icon']}</div>
                <div style='font-weight:700; color:#e2e2f0; font-size:1rem;'>{cert['name']}</div>
                <div style='font-family:Space Mono,monospace; font-size:0.8rem; color:{cert['color']}; margin-top:6px;'>
                    {cert['issuer']}
                </div>
                <div style='margin-top:10px;'>
                    <span style='background:rgba(74,222,128,0.1); border:1px solid rgba(74,222,128,0.3);
                         color:#4ade80; border-radius:20px; padding:3px 12px;
                         font-family:Space Mono,monospace; font-size:11px;'>✓ Certified</span>
                </div>
            </div>
            """, unsafe_allow_html=True)


# ─── AI Chatbot ────────────────────────────────────────────────────────────────
elif page == "🤖 AI Chatbot":
    st.markdown("<div class='section-title'>🤖 Ask Akash's AI Assistant</div>", unsafe_allow_html=True)
    st.markdown("""
    <p style='color:#8888aa; font-size:0.9rem; margin-bottom:24px;'>
    This AI assistant knows everything about Akash's background, skills, and experience.
    Ask anything — <em>powered by a language model loaded from GitHub</em>.
    </p>
    """, unsafe_allow_html=True)

    # System prompt with Akash's full context
    SYSTEM_PROMPT = """You are Akash Pathak's personal AI assistant embedded in his portfolio website.
You have full knowledge of his background and should answer questions about him confidently and professionally.

AKASH'S PROFILE:
- Full Name: Akash Pathak
- Role: AI/ML Engineer at Tata Consultancy Services (TCS), Indore (May 2025 – Present)
- Education: B.Tech Computer Science Engineering (Data Science), Oriental Institute of Science & Technology, Bhopal, 2020–2024, CGPA 8.32
- Email: akash.pathak0123@gmail.com | Phone: +91 7024426415
- LinkedIn: https://www.linkedin.com/in/akash-pathak-44a082212
- GitHub: https://github.com/akash0123-pride
- Location: Originally from Chhatapur, India

WORK EXPERIENCE:
1. TCS – AI/ML Engineer (May 2025–Present): End-to-end ML workflows, TensorFlow models, intelligent automation, Docker, CI/CD, AWS, model monitoring and drift detection.
2. IBM SkillsBuild – ML Intern (Sep–Nov 2022): Random Forest models, feature engineering, cross-validation.
3. DMRC – Data Science Intern (Jul–Sep 2022): Data cleaning, outlier detection, Streamlit analytics app.

PROJECTS:
- Enterprise Document Intelligence (RAG): LangChain, vector search, automated knowledge retrieval
- Lung Disease Detection: ResNet + TensorFlow for X-ray classification
- Indian Crime Dashboard: Streamlit + Plotly analytics dashboard
- Smart Streetlight AI: Computer vision anomaly detection
- Driver Drowsiness Detection: OpenCV real-time alerting system
- Mental Health Tracker: ML-based wellness insights app

SKILLS: Python, SQL, TensorFlow, PyTorch, Keras, Scikit-learn, LangChain, LangGraph, RAG, Hugging Face, OpenAI APIs, Docker, AWS, CI/CD, MLOps (learning), Tableau, Prompt Engineering

CERTIFICATIONS: ML with Python (FreeCodeCamp), Applied Data Science with Python (IBM), Python for DS & ML (Udemy)

PERSONALITY: Professional, passionate about AI/ML, eager to solve real-world problems, open to new opportunities.

Answer concisely and helpfully. If asked about something unrelated to Akash, politely redirect to his professional profile. Always be friendly and professional."""

    # Initialize chat history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Display conversation
    chat_container = st.container()
    with chat_container:
        if not st.session_state.chat_history:
            st.markdown("""
            <div class='chat-message-bot'>
                👋 Hi! I'm Akash's AI assistant. Ask me anything about his experience, skills, projects, or how to get in touch!
            </div>
            """, unsafe_allow_html=True)
        for msg in st.session_state.chat_history:
            if msg["role"] == "user":
                st.markdown(f"<div class='chat-message-user'>🧑 {msg['content']}</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div class='chat-message-bot'>🤖 {msg['content']}</div>", unsafe_allow_html=True)

    # Quick questions
    st.markdown("<div style='margin:16px 0 8px; font-family:Space Mono,monospace; font-size:0.7rem; color:#555577; text-transform:uppercase; letter-spacing:2px;'>QUICK QUESTIONS</div>", unsafe_allow_html=True)
    quick_cols = st.columns(3)
    quick_questions = [
        "What does Akash do at TCS?",
        "What are his top skills?",
        "Tell me about his RAG project",
        "What's his educational background?",
        "Is he open to new opportunities?",
        "How can I contact Akash?",
    ]
    for i, q in enumerate(quick_questions):
        with quick_cols[i % 3]:
            if st.button(q, key=f"quick_{i}"):
                st.session_state.pending_question = q
                st.rerun()

    # Handle pending quick question
    if "pending_question" in st.session_state:
        user_input = st.session_state.pending_question
        del st.session_state.pending_question
    else:
        user_input = None

    # Chat input
    with st.form("chat_form", clear_on_submit=True):
        col_input, col_btn = st.columns([5, 1])
        with col_input:
            text_input = st.text_input("", placeholder="Ask about Akash's experience, skills, projects...", label_visibility="collapsed")
        with col_btn:
            submitted = st.form_submit_button("Send")

    if submitted and text_input:
        user_input = text_input

    if user_input:
        st.session_state.chat_history.append({"role": "user", "content": user_input})

        # Build messages for API
        messages = [{"role": m["role"], "content": m["content"]} for m in st.session_state.chat_history]

        with st.spinner("Thinking..."):
            try:
                response = requests.post(
                    "https://api.anthropic.com/v1/messages",
                    headers={"Content-Type": "application/json"},
                    json={
                        "model": "claude-haiku-4-5-20251001",
                        "max_tokens": 600,
                        "system": SYSTEM_PROMPT,
                        "messages": messages
                    },
                    timeout=30
                )
                data = response.json()
                if "content" in data and data["content"]:
                    reply = data["content"][0]["text"]
                else:
                    reply = "Sorry, I couldn't get a response. Please try again."
            except Exception as e:
                reply = f"⚠️ Connection error. Please check your API key or try again later."

        st.session_state.chat_history.append({"role": "assistant", "content": reply})
        st.rerun()

    if st.session_state.chat_history:
        if st.button("🗑️ Clear Chat"):
            st.session_state.chat_history = []
            st.rerun()

    # API key notice
    st.markdown("""
    <div style='margin-top:24px; padding:14px 18px; background:rgba(251,191,36,0.07);
         border:1px solid rgba(251,191,36,0.25); border-radius:10px;
         font-family:Space Mono,monospace; font-size:0.75rem; color:#fbbf24;'>
        ⚙️ <strong>Setup:</strong> Add your Anthropic API key in Streamlit secrets as <code>ANTHROPIC_API_KEY</code>
        or set <code>st.secrets["ANTHROPIC_API_KEY"]</code> in your deployment settings.
    </div>
    """, unsafe_allow_html=True)


# ─── Contact ───────────────────────────────────────────────────────────────────
elif page == "📞 Contact":
    st.markdown("<div class='section-title'>📞 Contact</div>", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("""
        <div class='card'>
            <div style='font-family:Space Mono,monospace; font-size:0.7rem; color:#7b7bff;
                 text-transform:uppercase; letter-spacing:2px; margin-bottom:20px;'>GET IN TOUCH</div>
            <div style='margin-bottom:16px;'>
                <span style='color:#555577; font-size:0.8rem; font-family:Space Mono,monospace;'>EMAIL</span><br>
                <a href='mailto:akash.pathak0123@gmail.com' style='color:#e2e2f0; text-decoration:none; font-size:1rem;'>
                    akash.pathak0123@gmail.com
                </a>
            </div>
            <div style='margin-bottom:16px;'>
                <span style='color:#555577; font-size:0.8rem; font-family:Space Mono,monospace;'>PHONE</span><br>
                <span style='color:#e2e2f0; font-size:1rem;'>+91 7024426415</span>
            </div>
            <div style='margin-bottom:16px;'>
                <span style='color:#555577; font-size:0.8rem; font-family:Space Mono,monospace;'>LOCATION</span><br>
                <span style='color:#e2e2f0; font-size:1rem;'>📍 Indore / Chhatapur, India</span>
            </div>
            <div style='margin-top:24px; display:flex; gap:10px; flex-wrap:wrap;'>
                <a href='https://www.linkedin.com/in/akash-pathak-44a082212' target='_blank'
                   style='background:rgba(120,120,255,0.15); border:1px solid rgba(120,120,255,0.35);
                   border-radius:8px; padding:10px 18px; color:#a78bfa; text-decoration:none;
                   font-family:Space Mono,monospace; font-size:12px;'>🔗 LinkedIn</a>
                <a href='https://github.com/akash0123-pride' target='_blank'
                   style='background:rgba(120,120,255,0.15); border:1px solid rgba(120,120,255,0.35);
                   border-radius:8px; padding:10px 18px; color:#a78bfa; text-decoration:none;
                   font-family:Space Mono,monospace; font-size:12px;'>🐙 GitHub</a>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='card'>
            <div style='font-family:Space Mono,monospace; font-size:0.7rem; color:#7b7bff;
                 text-transform:uppercase; letter-spacing:2px; margin-bottom:20px;'>AVAILABILITY</div>
            <div style='display:flex; align-items:center; gap:10px; margin-bottom:16px;'>
                <span style='color:#4ade80; font-size:1.2rem;'>●</span>
                <span style='color:#e2e2f0;'>Open to new opportunities</span>
            </div>
            <p style='color:#8888aa; font-size:0.9rem; line-height:1.7;'>
            Currently working at TCS as an AI/ML Engineer and exploring opportunities in
            <strong style='color:#a78bfa;'>Generative AI</strong>,
            <strong style='color:#38bdf8;'>MLOps</strong>, and
            <strong style='color:#7b7bff;'>AI Product Engineering</strong>.
            </p>
            <div style='margin-top:20px;'>
                <div class='sub-heading' style='margin-bottom:12px;'>INTERESTED IN</div>
                <div>
                    <span class='tag'>GenAI Applications</span>
                    <span class='tag'>MLOps</span>
                    <span class='tag'>LLM Engineering</span>
                    <span class='tag'>AI Products</span>
                    <span class='tag'>Remote Work</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
