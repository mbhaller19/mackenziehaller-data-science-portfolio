import streamlit as st
import streamlit.components.v1 as components
import base64

st.set_page_config(page_title="Mackenzie Haller | Data Science Portfolio", layout="wide")

# ------------------------------
# Encode profile photo for hero embed
with open("self_pic.png", "rb") as f:
    img_b64 = base64.b64encode(f.read()).decode()

# ------------------------------
# CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', 'Segoe UI', sans-serif;
    }

    .block-container {
        padding-top: 1rem;
        padding-bottom: 4rem;
        max-width: 1100px;
    }

    /* ── Hero ── */
    .hero {
        background: linear-gradient(135deg, #0f172a 0%, #1e3a5f 60%, #0ea5e9 100%);
        border-radius: 20px;
        padding: 3rem 3.5rem;
        display: flex;
        align-items: center;
        gap: 2.5rem;
        margin-bottom: 2rem;
    }
    .hero-photo {
        width: 150px;
        height: 150px;
        border-radius: 50%;
        background-size: 155%;
        background-position: center 15%;
        background-repeat: no-repeat;
        border: 4px solid rgba(255,255,255,0.25);
        flex-shrink: 0;
    }
    .hero-name {
        font-size: 3.8rem !important;
        font-weight: 800 !important;
        color: #ffffff !important;
        margin: 0 0 0.2rem 0;
        line-height: 1.05;
        letter-spacing: -0.01em;
    }
    .hero-title {
        font-size: 1.05rem;
        color: rgba(255,255,255,0.7);
        margin-bottom: 0.9rem;
        font-weight: 400;
    }
    .hero-bio {
        font-size: 0.95rem;
        color: rgba(255,255,255,0.8);
        line-height: 1.75;
        max-width: 640px;
        margin-bottom: 1.2rem;
    }
    .hero-btn {
        display: inline-block;
        padding: 0.45rem 1.1rem;
        border-radius: 8px;
        font-size: 0.86rem;
        font-weight: 600;
        text-decoration: none !important;
        margin-right: 0.5rem;
    }
    .hero-btn-dark  { background: #ffffff; color: #0f172a; border: 1px solid #ffffff; }
    .hero-btn-blue  { background: #ffffff; color: #0f172a; border: 1px solid #ffffff; }
    .hero-btn-ghost { background: #ffffff; color: #0f172a; border: 1px solid #ffffff; }

    /* ── Divider ── */
    .divider { border: none; border-top: 1px solid #e2e8f0; margin: 2rem 0; }

    /* ── Section heading ── */
    .section-heading {
        font-size: 0.72rem;
        font-weight: 700;
        color: #94a3b8;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        margin-bottom: 1.3rem;
    }

    /* ── Stat boxes ── */
    .stat-box {
        text-align: center;
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 14px;
        padding: 1.4rem 1rem;
    }
    .stat-number { font-size: 1.9rem; font-weight: 700; color: #0f172a; display: block; }
    .stat-label  { font-size: 0.8rem; color: #64748b; margin-top: 0.3rem; display: block; line-height: 1.4; }

    /* ── What I Can Do cards ── */
    .service-card {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 14px;
        padding: 1.4rem 1.3rem;
        height: 100%;
    }
    .service-icon  { font-size: 1.6rem; margin-bottom: 0.6rem; display: block; }
    .service-title { font-size: 1rem; font-weight: 600; color: #0f172a; margin-bottom: 0.4rem; }
    .service-desc  { font-size: 0.87rem; color: #64748b; line-height: 1.65; }

    /* ── Skill tags ── */
    .skill-tag {
        display: inline-block;
        background: #f1f5f9;
        color: #334155;
        border-radius: 6px;
        padding: 0.28rem 0.8rem;
        font-size: 0.83rem;
        font-weight: 500;
        margin: 0.2rem 0.15rem;
        border: 1px solid #e2e8f0;
    }
    .skill-tag-match {
        display: inline-block;
        background: #dbeafe;
        color: #1d4ed8;
        border-radius: 6px;
        padding: 0.28rem 0.8rem;
        font-size: 0.83rem;
        font-weight: 600;
        margin: 0.2rem 0.15rem;
        border: 1px solid #bfdbfe;
    }
    .skill-category {
        font-size: 0.72rem;
        font-weight: 700;
        color: #94a3b8;
        text-transform: uppercase;
        letter-spacing: 0.09em;
        margin-bottom: 0.4rem;
        margin-top: 1rem;
        display: block;
    }

    /* ── Project cards ── */
    .project-title { font-size: 1.1rem; font-weight: 600; color: #0f172a; margin-bottom: 0.3rem; }
    .project-tools { font-size: 0.8rem; color: #94a3b8; margin-bottom: 0.7rem; font-weight: 500; }
    .project-desc  { font-size: 0.93rem; color: #475569; line-height: 1.7; margin-bottom: 0.8rem; }
    .project-link a { color: #0ea5e9; font-size: 0.9rem; text-decoration: none; font-weight: 500; }
    .project-link a:hover { text-decoration: underline; }

    /* ── Status badges ── */
    .badge {
        display: inline-block;
        font-size: 0.72rem;
        font-weight: 600;
        padding: 0.18rem 0.6rem;
        border-radius: 5px;
        margin-left: 0.4rem;
        vertical-align: middle;
    }
    .badge-inprogress { background: #fef3c7; color: #92400e; border: 1px solid #fde68a; }
    .badge-inpublication { background: #ede9fe; color: #5b21b6; border: 1px solid #ddd6fe; }

    /* ── Contact row ── */
    .contact-row { font-size: 0.85rem; color: #94a3b8; text-align: center; }
    .contact-row a { color: #64748b; text-decoration: none; font-weight: 500; }
    .contact-row a:hover { color: #0f172a; }

    /* Sidebar buttons */
    [data-testid="stSidebar"] .stButton > button {
        background: transparent !important;
        border: 1px solid #1e293b !important;
        color: #94a3b8 !important;
        text-align: left !important;
        font-size: 0.9rem !important;
        padding: 0.3rem 0.5rem !important;
        width: 100% !important;
    }
    [data-testid="stSidebar"] .stButton > button:hover {
        border-color: #475569 !important;
        color: #ffffff !important;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background: #0f172a;
        border-right: 1px solid #1e293b;
    }
    [data-testid="stSidebar"] * {
        color: #cbd5e1 !important;
    }
    [data-testid="stSidebar"] h3 {
        color: #ffffff !important;
        font-size: 1rem !important;
        font-weight: 700 !important;
        letter-spacing: 0.02em;
    }
    [data-testid="stSidebar"] a {
        color: #94a3b8 !important;
        text-decoration: none !important;
        font-size: 0.9rem;
        line-height: 2;
    }
    [data-testid="stSidebar"] a:hover {
        color: #ffffff !important;
    }
    [data-testid="stSidebar"] hr {
        border-color: #1e293b !important;
        margin: 0.8rem 0;
    }
    [data-testid="stSidebar"] strong {
        color: #ffffff !important;
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 0.1em;
    }
</style>
""", unsafe_allow_html=True)

# ------------------------------
# Sidebar Navigation
if "active_tab" not in st.session_state:
    st.session_state["active_tab"] = "Projects"
if "scroll_top" not in st.session_state:
    st.session_state["scroll_top"] = False
if "scroll_to_tab" not in st.session_state:
    st.session_state["scroll_to_tab"] = False
if "scroll_nonce" not in st.session_state:
    st.session_state["scroll_nonce"] = 0

# Sync URL query param → active tab on page load / direct link
_tab_param = st.query_params.get("tab", "")
if _tab_param in ("Projects", "Resume"):
    st.session_state["active_tab"] = _tab_param

with st.sidebar:
    st.markdown("### Mackenzie Haller")
    st.markdown("---")
    st.markdown("""
- [About](#about)
- [What I Can Do](#what-i-can-do-for-you)
- [Skills](#skills)
""")
    if st.button("Projects", use_container_width=True, key="sb_projects"):
        st.session_state["active_tab"] = "Projects"
        st.session_state["scroll_to_tab"] = True
        st.session_state["scroll_nonce"] += 1
        st.query_params["tab"] = "Projects"
        st.rerun()
    if st.button("Resume", use_container_width=True, key="sb_resume"):
        st.session_state["active_tab"] = "Resume"
        st.session_state["scroll_to_tab"] = True
        st.session_state["scroll_nonce"] += 1
        st.query_params["tab"] = "Resume"
        st.rerun()
    st.markdown("---")
    st.markdown("---")
    st.markdown("**Contact**")
    st.markdown("haller.mackenzie@outlook.com")
    st.markdown("[GitHub](https://github.com/mackenziehaller)  ·  [LinkedIn](https://www.linkedin.com/in/mackenzie-haller-18aa88bb/)")

# Scroll to top when switching tabs
if st.session_state["scroll_top"]:
    st.session_state["scroll_top"] = False
    components.html(
        "<script>window.parent.document.querySelector('section.main').scrollTo({top: 0, behavior: 'instant'});</script>",
        height=0,
    )

# Scroll to the projects/resume section when clicking sidebar nav
if st.session_state["scroll_to_tab"]:
    st.session_state["scroll_to_tab"] = False
    _nonce = st.session_state["scroll_nonce"]
    components.html(
        f"<script>setTimeout(function(){{ var el = window.parent.document.getElementById('projects'); if(el){{ el.scrollIntoView({{behavior: 'smooth'}}); }} }}, 200); /* n={_nonce} */</script>",
        height=0,
    )

# ------------------------------
# Hero Banner
st.markdown(f"""
<div id="about" class="hero">
    <div class="hero-photo" style="background-image: url('data:image/png;base64,{img_b64}');"></div>
    <div>
        <h1 class="hero-name">Mackenzie Haller</h1>
        <p class="hero-title">Data Scientist &amp; Analytics Professional &nbsp;·&nbsp; SQL &nbsp;·&nbsp; Python &nbsp;·&nbsp; Power BI &nbsp;·&nbsp; Machine Learning &amp; AI</p>
        <p class="hero-bio">
            Data scientist and analytics professional with 6+ years of experience across public health, tech, and utilities.
            I build end-to-end analytics — automated data pipelines, predictive models, and production dashboards — that turn
            complex, real-world data into decisions. Comfortable owning a project from raw data to a stakeholder-ready result.
        </p>
        <a href="https://github.com/mackenziehaller" target="_blank" class="hero-btn hero-btn-dark">GitHub</a>
        <a href="https://www.linkedin.com/in/mackenzie-haller-18aa88bb/" target="_blank" class="hero-btn hero-btn-blue">LinkedIn</a>
        <a href="mailto:haller.mackenzie@outlook.com" class="hero-btn hero-btn-ghost">Email</a>
        <a href="?tab=Resume" class="hero-btn hero-btn-ghost">Resume</a>
    </div>
</div>
""", unsafe_allow_html=True)

# ------------------------------
# Stats
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<div class="stat-box"><span class="stat-number">6+</span><span class="stat-label">Years of Experience</span></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="stat-box"><span class="stat-number">M.S.</span><span class="stat-label">Master of Data Science (Honors) · UNSW</span></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="stat-box"><span class="stat-number">3</span><span class="stat-label">Industries: Public Health · Tech · Utilities</span></div>', unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ------------------------------
# What I Can Do For You
st.markdown('<div id="what-i-can-do-for-you"></div>', unsafe_allow_html=True)
st.markdown('<p class="section-heading">What I Can Do For You</p>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("""
    <div class="service-card">
        <span class="service-icon">📊</span>
        <div class="service-title">Data Analytics & Insights</div>
        <div class="service-desc">Turn complex, messy datasets into clear, actionable insights for teams, executives, and stakeholders across any domain.</div>
    </div>
    """, unsafe_allow_html=True)
with c2:
    st.markdown("""
    <div class="service-card">
        <span class="service-icon">📈</span>
        <div class="service-title">Dashboard & BI Development</div>
        <div class="service-desc">Build interactive, production-ready dashboards in Power BI, Streamlit, or R Shiny that automate reporting and reduce ad-hoc requests.</div>
    </div>
    """, unsafe_allow_html=True)
with c3:
    st.markdown("""
    <div class="service-card">
        <span class="service-icon">🔁</span>
        <div class="service-title">Data Pipeline Engineering</div>
        <div class="service-desc">Design and maintain reliable ETL pipelines, SQL Server databases, and Azure-based workflows for automated, scalable data delivery.</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
c4, c5, c6 = st.columns(3)
with c4:
    st.markdown("""
    <div class="service-card">
        <span class="service-icon">🤖</span>
        <div class="service-title">ML & Predictive Modeling</div>
        <div class="service-desc">Build supervised models for classification, regression, and survival analysis to support evidence-based, data-driven decisions.</div>
    </div>
    """, unsafe_allow_html=True)
with c5:
    st.markdown("""
    <div class="service-card">
        <span class="service-icon">✨</span>
        <div class="service-title">AI & LLM Integration</div>
        <div class="service-desc">Integrate LLMs into data workflows via RAG pipelines, LoRA fine-tuning, and AI-assisted data collection and automation.</div>
    </div>
    """, unsafe_allow_html=True)
with c6:
    st.markdown("""
    <div class="service-card">
        <span class="service-icon">📄</span>
        <div class="service-title">Reproducible Research & Reporting</div>
        <div class="service-desc">Deliver publication-quality, reproducible analytics using R (Quarto), Python, and GIS tools for technical reports and research outputs.</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
c7, c8, c9 = st.columns(3)
with c7:
    st.markdown("""
    <div class="service-card">
        <span class="service-icon">⚙️</span>
        <div class="service-title">Workflow Automation</div>
        <div class="service-desc">Automate repetitive reporting, data collection, and operational processes using Python, GitHub Actions, and AI-assisted pipelines.</div>
    </div>
    """, unsafe_allow_html=True)
with c8:
    st.markdown("""
    <div class="service-card">
        <span class="service-icon">🎓</span>
        <div class="service-title">Data Upskilling & Training</div>
        <div class="service-desc">Upskill teams in SQL, R, Python, and BI tools through hands-on training, documentation, and tool adoption support.</div>
    </div>
    """, unsafe_allow_html=True)
with c9:
    st.markdown("""
    <div class="service-card">
        <span class="service-icon">📈</span>
        <div class="service-title">Data Strategy & Analytics Consulting</div>
        <div class="service-desc">Translate business goals into a clear data strategy, from KPI definition to reporting architecture and tool selection.</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ------------------------------
# Skills with Search
st.markdown('<div id="skills"></div>', unsafe_allow_html=True)
st.markdown('<p class="section-heading">Skills</p>', unsafe_allow_html=True)

ALL_SKILLS = {
    "Programming & Analytics": ["SQL", "Python", "R", "SAS", "Java", "Excel (VBA)", "Quarto", "dplyr", "tidyverse"],
    "Data Visualization & BI": ["Power BI (DAX)", "Streamlit", "R Shiny", "Plotly", "ggplot2", "matplotlib", "seaborn", "Spotfire", "leaflet"],
    "Analytics & Reporting": ["KPI Reporting", "Data Quality Assurance", "Reproducible Reporting", "Applied Research", "Study Design", "A/B Testing", "Statistical Analysis"],
    "ML, AI & Statistics": ["Regression", "Classification", "Survival Analysis", "Tree-Based Models", "LLMs", "RAG Pipelines", "LoRA Fine-Tuning", "AI Workflow Automation", "NLP", "Predictive Modeling", "Feature Engineering"],
    "Infrastructure & Cloud": ["SQL Server", "Azure", "ETL Pipelines", "Docker", "Git / GitHub", "GitHub Actions", "Kafka", "Schema Design"],
    "GIS & Spatial": ["GIS Analysis", "Spatial Analytics", "R (sf, leaflet, ggmap)", "Mapping"],
    "Soft Skills": ["Data Storytelling", "Stakeholder Reporting", "Research Communication", "Process Improvement", "Workflow Automation", "Cross-functional Collaboration"],
}

search = st.text_input("🔍 Search skills...", placeholder="e.g. Python, LLM, Power BI...")

for category, skills in ALL_SKILLS.items():
    if search:
        matched   = [s for s in skills if search.lower() in s.lower()]
        unmatched = [s for s in skills if search.lower() not in s.lower()]
        if not matched and not unmatched:
            continue
        html = f'<span class="skill-category">{category}</span>'
        for s in matched:
            html += f'<span class="skill-tag-match">{s}</span>'
        for s in unmatched:
            html += f'<span class="skill-tag">{s}</span>'
        st.markdown(html, unsafe_allow_html=True)
    else:
        html = f'<span class="skill-category">{category}</span>'
        for s in skills:
            html += f'<span class="skill-tag">{s}</span>'
        st.markdown(html, unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ------------------------------
# Beyond the Data
st.markdown('<p class="section-heading">Beyond the Data</p>', unsafe_allow_html=True)
st.markdown("""
<span class="skill-category">Interests</span>
<span class="skill-tag">Applied Statistics</span>
<span class="skill-tag">Data Storytelling</span>
<span class="skill-tag">Open-Source Tooling</span>
<span class="skill-tag">Evidence-Based Decision Making</span>
<span class="skill-category">Other</span>
<span class="skill-tag">CorePower Yoga Instructor · 2021 to Present</span>
""", unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ------------------------------
# Projects / Resume switcher
st.markdown('<div id="projects"></div>', unsafe_allow_html=True)

# Tab-style toggle buttons
col_t1, col_t2, _ = st.columns([1, 1, 6])
with col_t1:
    if st.button("Projects", key="main_projects",
                 type="primary" if st.session_state["active_tab"] == "Projects" else "secondary"):
        st.session_state["active_tab"] = "Projects"
        st.query_params["tab"] = "Projects"
        st.rerun()
with col_t2:
    if st.button("Resume", key="main_resume",
                 type="primary" if st.session_state["active_tab"] == "Resume" else "secondary"):
        st.session_state["active_tab"] = "Resume"
        st.query_params["tab"] = "Resume"
        st.rerun()

st.markdown('<hr class="divider">', unsafe_allow_html=True)

if st.session_state["active_tab"] == "Projects":
    st.markdown('<p class="section-heading">Selected Projects</p>', unsafe_allow_html=True)

    # Project 1
    st.markdown("""
    <p class="project-title">Summer Drowning Toll Dashboard</p>
    <p class="project-tools">Python &nbsp;·&nbsp; Streamlit &nbsp;·&nbsp; Azure &nbsp;·&nbsp; SQL Server &nbsp;·&nbsp; GitHub Actions</p>
    <p class="project-desc">End-to-end operational dashboard with a fully automated production pipeline: scheduled ETL jobs,
    a SQL Server backend, and daily-refreshed visualizations deployed via GitHub Actions to a public Streamlit app.</p>
    <p class="project-link"><a href="https://www.royallifesaving.com.au/research-and-policy/drowning-research/summer-drowning-toll" target="_blank">View live dashboard →</a></p>
    """, unsafe_allow_html=True)
    selection = st.selectbox("Preview visualization", ["Bar Chart", "Line Chart", "Map"])
    image_map = {"Bar Chart": "sdt_bar.png", "Line Chart": "sdt_line.png", "Map": "sdt_map.png"}
    st.image(image_map[selection], use_container_width=True)

    st.markdown('<hr class="divider">', unsafe_allow_html=True)

    # Project 2
    st.markdown("""
    <p class="project-title">Annual National Drowning Report</p>
    <p class="project-tools">R &nbsp;·&nbsp; SQL</p>
    <p class="project-desc">Reproducible R/Quarto analytics pipeline — from raw data ingestion through statistical
    trend analysis to publication-ready report — supporting a national annual publication.</p>
    <p class="project-link"><a href="https://www.royallifesaving.com.au/__data/assets/pdf_file/0004/118273/National-Drowning-Report-2025-V2.pdf" target="_blank">View report →</a></p>
    """, unsafe_allow_html=True)
    st.image("drowning.png", use_container_width=True)

    st.markdown('<hr class="divider">', unsafe_allow_html=True)

    # Project 3 — Thesis
    st.markdown("""
    <p class="project-title">ML Classification of Vulnerable Communities <span class="badge badge-inpublication">In Publication</span></p>
    <p class="project-tools">Python &nbsp;·&nbsp; Scikit-learn &nbsp;·&nbsp; Pandas</p>
    <p class="project-desc">Master's thesis building and evaluating supervised classification models (logistic regression,
    random forest, gradient boosting) on a 50k+ record national dataset to identify at-risk populations,
    including feature engineering, model selection, and performance evaluation across candidate algorithms.
    Paper currently in publication — link will be added upon release.</p>
    """, unsafe_allow_html=True)

    st.markdown('<hr class="divider">', unsafe_allow_html=True)

    # Project 4 — EHR
    st.markdown("""
    <p class="project-title">Real-Time Streaming Data Pipeline <span class="badge badge-inprogress">In Progress</span></p>
    <p class="project-tools">Python &nbsp;·&nbsp; Pandas &nbsp;·&nbsp; Seaborn &nbsp;·&nbsp; Kafka &nbsp;·&nbsp; MIMIC Dataset</p>
    <p class="project-desc">Built a Kafka-based streaming pipeline for real-time ingestion and processing of a large
    time-series dataset (MIMIC), with downstream exploratory analysis and trend visualization across cohorts.</p>
    <p class="project-link"><span style="color:#94a3b8; font-size:0.9rem;">Code available upon request</span></p>
    """, unsafe_allow_html=True)

elif st.session_state["active_tab"] == "Resume":
    st.markdown('<div id="resume"></div>', unsafe_allow_html=True)
    col_dl, _ = st.columns([1, 3])
    with col_dl:
        with open("resume.pdf", "rb") as f:
            st.download_button("Download Resume (PDF)", f, file_name="Mackenzie_Haller_Resume.pdf", mime="application/pdf")

    st.markdown("---")
    st.markdown("### Profile")
    st.markdown("Data scientist and analytics professional with experience across strategy, analytics, and technology spanning public health, semiconductor manufacturing, and utilities. Proven ability to turn complex, real-world data into actionable insights that inform research, strategy, and operational decisions. Experienced in end-to-end analytics including study design, statistical analysis, predictive modeling, and visualization. Skilled in framing ambiguous business questions, defining hypotheses, and developing reproducible analytical pipelines. Passionate about driving decisions through data and close collaboration with cross-functional teams.")

    st.markdown("---")
    st.markdown("### Experience")

    st.markdown("**Data Science Officer** · Royal Life Saving Society · *Sep 2024 – Present*")
    st.markdown("""
- Lead end-to-end analytics across multiple projects, translating complex, large-scale datasets into actionable insights for strategy and decision-making.
- Design and implement automated data workflows, improving reporting efficiency by 30% and ensuring reproducibility.
- Build and maintain SQL databases and Azure data pipelines, improving data reliability and accessibility across teams.
- Develop machine learning-driven data collection processes, increasing data accuracy by 20% and eliminating manual collection efforts.
- Create dashboards and reporting tools (Power BI, R Shiny, Python) to support internal decision-making and external stakeholder communication.
- Conduct data cleaning, validation, and integration across large, multi-source datasets to ensure analytical quality.
- Partner with research and policy teams to define study hypotheses, design analysis, and interpret results.
- Communicate findings to executives, media, and public stakeholders, influencing public health initiatives.
- Train team members in SQL and R, improving data literacy and analytical capabilities across the organization.
""")

    st.markdown("**Data / Business Analyst** · ASML · *Nov 2022 – Jan 2024*")
    st.markdown("""
- Translated demand, cost, and forecast data into actionable insights to guide strategic planning and operational decisions.
- Developed interactive dashboards (Power BI, Spotfire) integrating complex datasets to monitor performance and resource utilization.
- Delivered recurring executive reports, presenting analysis in clear, decision-ready formats.
- Identified cost-saving opportunities and improved operational efficiency through data-driven recommendations.
""")

    st.markdown("**Engineering / Data Analyst** · San Diego Gas & Electric (SDG&E) · *Mar 2020 – Nov 2022*")
    st.markdown("""
- Analyzed large-scale operational datasets to support regulatory reporting and internal quality standards.
- Authored daily operational reports, ensuring timely and accurate communication of findings.
""")

    st.markdown("**Data Engineer / QA** *(Part-time)* · GoodMonth Labs · *Jan 2022 – Jun 2022*")
    st.markdown("""
- Developed an NLP-based machine learning model for consumer messaging data, supporting product insights and automation.
""")

    st.markdown("**Quality Assurance Analyst** · Arrowhead General Insurance · *Aug 2019 – Mar 2020*")
    st.markdown("""
- Designed and executed QA strategies for enterprise applications, improving release quality.
""")

    st.markdown("---")
    st.markdown("### Education")
    st.markdown("""
**Master of Data Science (Honors)** · University of New South Wales (UNSW) · *Graduated Sep 2025*
Focus: Statistical modeling, machine learning, and applied predictive analytics on large, real-world datasets

**B.S. Applied Mathematics, Minor Economics** · California Polytechnic State University, San Luis Obispo · *Graduated Jun 2019*
""")

    st.markdown("---")
    st.markdown("### Technical Skills")
    st.markdown("""
| Area | Skills |
|---|---|
| Programming & Data Analysis | SQL, Python, R, SAS, Excel; healthcare analytics; EHR and ICD-coded data |
| Data Visualization | Power BI (DAX), Tableau, Spotfire, R Shiny, Plotly, Streamlit |
| Analytics & Modeling | Machine learning, regression/classification, clustering, predictive modeling, KPI development, cost analysis |
| Data Engineering & Automation | ETL pipelines, database design, Azure workflows, Git, workflow automation, AI-assisted analytics |
| Communication | Executive reporting, stakeholder engagement, translating data into actionable insights, cross-functional collaboration |
""")

    st.markdown("---")
    st.markdown("### Projects")
    st.markdown("""
**Thesis: A Machine Learning Approach to Classifying Vulnerable Communities** *(Jan 2025 – Sep 2025, in publication)*
- Built and evaluated predictive classification models on a national dataset (50k+ records) to identify high-risk populations.
- Developed reproducible analytics pipelines and dashboards to support decision-making and resource allocation.

**Resident Scheduling Program** · R Shiny · *Jan 2025 – Mar 2025*
- Developed an R Shiny application to optimize scheduling across 15 staff, reducing manual effort by 50% and ensuring compliance with operational constraints.

**UNSW Data Science Datathon** · *Dec 2024*
- Collaborated with a 4-person team to analyze real-time event data under competition time constraints.

**Streaming Data Pipeline** · Kafka, MIMIC Dataset *(in progress)*
- Time-series pattern analysis with a Kafka streaming pipeline for real-time data ingestion and processing.
""")

# ------------------------------
# Footer
st.markdown('<hr class="divider">', unsafe_allow_html=True)
st.markdown("""
<p class="contact-row">
    haller.mackenzie@outlook.com &nbsp;·&nbsp;
    <a href="https://github.com/mackenziehaller" target="_blank">GitHub</a> &nbsp;·&nbsp;
    <a href="https://www.linkedin.com/in/mackenzie-haller-18aa88bb/" target="_blank">LinkedIn</a>
</p>
""", unsafe_allow_html=True)
