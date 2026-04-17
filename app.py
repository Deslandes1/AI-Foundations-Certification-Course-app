import streamlit as st
import asyncio
import tempfile
import base64
import os
import subprocess

st.set_page_config(page_title="AI Foundations & Certification Course", layout="wide")

def set_tech_style():
    st.markdown("""
        <style>
        .stApp { background: linear-gradient(135deg, #0a0f1f, #0e1a2a, #0a0f1f); }
        .main-header { background: linear-gradient(135deg, #00d4ff, #0077ff, #0033aa); padding: 1.5rem; border-radius: 20px; text-align: center; margin-bottom: 1rem; }
        .main-header h1 { color: white; text-shadow: 2px 2px 4px #000000; font-size: 2.5rem; margin: 0; }
        .main-header p { color: #fff5cc; font-size: 1.2rem; margin: 0; }
        html, body, .stApp, .stMarkdown, .stText, .stRadio label, .stSelectbox label, .stTextInput label, .stButton button, .stTitle, .stSubheader, .stHeader, .stCaption, .stAlert, .stException, .stCodeBlock, .stDataFrame, .stTable, .stTabs [role="tab"], .stTabs [role="tablist"] button, .stExpander, .stProgress > div, .stMetric label, .stMetric value, div, p, span, pre, code, .element-container, .stTextArea label, .stText p, .stText div, .stText span, .stText code { color: #ffffff !important; }
        .stText { color: #ffffff !important; font-size: 1rem; background: transparent !important; }
        .stTabs [role="tab"] { color: #ffffff !important; background: rgba(0,212,255,0.2); border-radius: 10px; margin: 0 2px; }
        .stTabs [role="tab"][aria-selected="true"] { background: #0077ff; color: white !important; }
        .stRadio [role="radiogroup"] label { background: rgba(255,255,255,0.1); border-radius: 10px; padding: 0.3rem; margin: 0.2rem 0; color: white !important; }
        .stButton button { background-color: #0077ff; color: white !important; border-radius: 30px; font-weight: bold; }
        .stButton button:hover { background-color: #00d4ff; color: black !important; }
        section[data-testid="stSidebar"] { background: linear-gradient(135deg, #0a0f1f, #0e1a2a); }
        section[data-testid="stSidebar"] .stMarkdown, section[data-testid="stSidebar"] .stText, section[data-testid="stSidebar"] label { color: white !important; }
        section[data-testid="stSidebar"] .stSelectbox label { color: white !important; }
        section[data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] { background-color: #1e2a3a; border: 1px solid #0077ff; border-radius: 10px; }
        div[data-baseweb="popover"] ul { background-color: #1e2a3a; border: 1px solid #0077ff; }
        div[data-baseweb="popover"] li { color: white !important; background-color: #1e2a3a; }
        div[data-baseweb="popover"] li:hover { background-color: #0077ff; }
        .certificate { background: linear-gradient(135deg, #ffd700, #ffaa00); padding: 1rem; border-radius: 20px; text-align: center; color: #000 !important; }
        .certificate h3, .certificate p { color: #000 !important; }
        </style>
    """, unsafe_allow_html=True)

def show_logo():
    st.markdown("""
        <div style="display: flex; justify-content: center; margin-bottom: 1rem;">
            <svg width="100" height="100" viewBox="0 0 100 100">
                <circle cx="50" cy="50" r="45" fill="url(#gradLogo)" stroke="#00d4ff" stroke-width="3"/>
                <defs><linearGradient id="gradLogo" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" stop-color="#00d4ff"/>
                    <stop offset="50%" stop-color="#0077ff"/>
                    <stop offset="100%" stop-color="#0033aa"/>
                </linearGradient></defs>
                <text x="50" y="65" font-size="40" text-anchor="middle" fill="white" font-weight="bold">🤖</text>
            </svg>
        </div>
    """, unsafe_allow_html=True)

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    set_tech_style()
    st.title("🔐 Access Required")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        show_logo()
        st.markdown("<h2 style='text-align: center;'>AI Foundations & Certification Course</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #00d4ff;'>28 days to AI mastery – from beginner to certified expert</p>", unsafe_allow_html=True)
        password_input = st.text_input("Enter password to access", type="password")
        if st.button("Login"):
            if password_input == "20082010":
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("Incorrect password. Access denied.")
    st.stop()

set_tech_style()
st.markdown("""
<div class="main-header">
    <h1>🤖 AI Foundations & Certification Course</h1>
    <p>28 days | 4 weeks | Hands‑on projects | Official certificate</p>
</div>
""", unsafe_allow_html=True)

with st.sidebar:
    show_logo()
    st.markdown("## 🎯 Select a day")
    day_number = st.selectbox("Day", list(range(1, 29)), index=0)
    st.markdown("---")
    st.markdown("### 📚 Your progress")
    st.progress(day_number / 28)
    st.markdown(f"✅ Day {day_number} of 28 completed")
    st.markdown("---")
    st.markdown("**Founder & Developer:**")
    st.markdown("Gesner Deslandes")
    st.markdown("📞 WhatsApp: (509) 4738-5663")
    st.markdown("📧 Email: deslandes78@gmail.com")
    st.markdown("🌐 [Main website](https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/)")
    st.markdown("---")
    st.markdown("### 💰 Price")
    st.markdown("**$299 USD** (full course – all 28 days, source code, certificate)")
    st.markdown("---")
    st.markdown("### © 2025 GlobalInternet.py")
    st.markdown("All rights reserved")
    st.markdown("---")
    if st.button("🚪 Logout", use_container_width=True):
        st.session_state.authenticated = False
        st.rerun()

# ---------- Course data ----------
weeks = {
    1: {"title": "Week 1 - AI Foundations & Your Personal Mentor", "days": 7},
    2: {"title": "Week 2 - Creativity & Quiet Skill-Building", "days": 7},
    3: {"title": "Week 3 - Building AI Bots & Smart Automation", "days": 7},
    4: {"title": "Week 4 - Certification & Career Application", "days": 7}
}

lessons = {
    1: {"title": "Meet your AI Mentor - Setting up ChatGPT & Gemini", "duration": "15 min", "content": "Learn how to create accounts, navigate the interfaces, and understand the core capabilities of ChatGPT and Google Gemini. These will be your primary AI assistants throughout the course."},
    2: {"title": "The 'Overthinker's Guide' to Prompting - Get exact answers", "duration": "14 min", "content": "Master the art of crafting precise prompts. Discover how to structure questions, use context, and avoid common pitfalls to get exactly the answers you need."},
    3: {"title": "Claude - Brainstorming & organizing messy thoughts", "duration": "16 min", "content": "Explore Claude's strength in handling long context windows. Use it to brainstorm ideas, summarize documents, and organize scattered notes into clear action plans."},
    4: {"title": "Perplexity - Smart, stress-free internet research", "duration": "12 min", "content": "Use Perplexity AI to conduct research with citations. Learn to ask follow-up questions and get accurate, up‑to‑date information without endless searching."},
    5: {"title": "AI for daily productivity & saving 2 hours a day", "duration": "15 min", "content": "Practical ways to integrate AI into your daily routine: email drafting, task prioritization, meeting summaries, and quick data analysis."},
    6: {"title": "Crafting your first custom AI assistant persona", "duration": "18 min", "content": "Create a personalized AI persona tailored to your role or interests. Define its tone, expertise, and typical responses to act as your dedicated assistant."},
    7: {"title": "Milestone - Build your personalized daily AI workflow", "duration": "20 min", "content": "Combine everything from week 1 into a seamless daily routine. Map out when and how you will use each AI tool to maximize efficiency."},
    8: {"title": "MidJourney - Turning simple text into stunning visuals", "duration": "14 min", "content": "Introduction to MidJourney. Learn basic commands, parameters, and how to generate high‑quality images from text prompts."},
    9: {"title": "MidJourney - Creating professional brand graphics", "duration": "16 min", "content": "Advanced techniques: logos, social media banners, presentation backgrounds. Learn to iterate and refine outputs for a consistent brand style."},
    10: {"title": "Canva + AI - Design basics with zero artistic skills", "duration": "15 min", "content": "Use Canva's AI features (Magic Write, Text to Image) to create professional designs quickly. No design experience required."},
    11: {"title": "Runway - Turning static images into engaging video", "duration": "17 min", "content": "Animate static images, add motion, and create short video clips using Runway's Gen‑2 and other tools."},
    12: {"title": "ElevenLabs - Pro voiceovers without recording yourself", "duration": "14 min", "content": "Generate natural‑sounding voiceovers from text. Adjust tone, speed, and emotion to match your project."},
    13: {"title": "Assembling your first AI-generated portfolio piece", "duration": "18 min", "content": "Combine visuals, voiceover, and video into a cohesive portfolio piece. Plan the narrative and structure."},
    14: {"title": "Milestone - Complete your 'Faceless' AI Video Project", "duration": "20 min", "content": "Produce a complete video (e.g., educational short, product promo) using only AI‑generated assets. No on‑camera presence needed."},
    15: {"title": "Basics - Visual automation without a single line of code", "duration": "16 min", "content": "Introduction to automation platforms (Zapier, Make). Understand triggers, actions, and how to connect apps visually."},
    16: {"title": "Connecting AI to your favorite everyday apps", "duration": "18 min", "content": "Integrate AI with Google Sheets, Gmail, Slack, and other common tools to automate repetitive tasks."},
    17: {"title": "Make.com - Building an automated researcher bot", "duration": "15 min", "content": "Step‑by‑step creation of a bot that fetches news, summarizes articles, and sends reports to you on a schedule."},
    18: {"title": "How to present AI wins to your manager", "duration": "18 min", "content": "Frameworks and templates for showcasing your automation successes. Learn to measure ROI and communicate value effectively."},
    19: {"title": "Creating a 24/7 AI Customer Support Agent", "duration": "20 min", "content": "Build a chatbot that answers common customer questions using OpenAI's API or a no‑code platform like Landbot."},
    20: {"title": "Testing & refining your new AI bot", "duration": "15 min", "content": "Methods for testing your bot, collecting feedback, and iterating to improve accuracy and user satisfaction."},
    21: {"title": "Milestone - Deploy your first working AI Automation", "duration": "20 min", "content": "Launch your automation in a real environment (e.g., for your own business or a test project). Document the process and results."},
    22: {"title": "Preparing for your JobEscape AI Certification", "duration": "14 min", "content": "Overview of the certification exam, key topics, and study strategies. Review the official guide."},
    23: {"title": "Packaging your AI skills for your current role", "duration": "16 min", "content": "How to add AI skills to your resume, LinkedIn, and performance reviews. Practical tips for immediate application."},
    24: {"title": "How to present AI wins to your manager (repeat)", "duration": "18 min", "content": "Refine your presentation skills with more examples and role‑play scenarios. Learn to handle questions and objections."},
    25: {"title": "Building your personal AI workflow from scratch", "duration": "15 min", "content": "Design a custom workflow that integrates the tools you've learned. Focus on your unique needs and goals."},
    26: {"title": "The Final AI Knowledge Check & Review", "duration": "20 min", "content": "Comprehensive review of all concepts covered in the course. Practice quiz to test your understanding."},
    27: {"title": "Claim your Official AI Expert Certificate", "duration": "10 min", "content": "Download your personalized certificate after completing the course requirements. Instructions for verification."},
    28: {"title": "Apply what you learned – your first real AI project at work", "duration": "15 min", "content": "Guidance on identifying a real project in your workplace, planning the implementation, and measuring success. Next steps for continued learning."}
}

# Determine which week
week_num = (day_number - 1) // 7 + 1
week_title = weeks[week_num]["title"]
day_title = lessons[day_number]["title"]
duration = lessons[day_number]["duration"]
content = lessons[day_number]["content"]

st.markdown(f"## 📅 {week_title}")
st.markdown(f"### Day {day_number}: {day_title}")
st.markdown(f"⏱️ **Duration:** {duration}")
st.markdown("---")
st.markdown(content)

# Audio for the lesson content
def generate_audio(text, output_path):
    cmd = ["edge-tts", "--voice", "en-US-GuyNeural", "--text", text, "--write-media", output_path]
    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True, timeout=30)
    except Exception as e:
        st.error(f"Audio error: {e}")

def play_audio(text, key):
    if st.button(f"🔊 Listen to lesson", key=key):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
            generate_audio(text, tmp.name)
            with open(tmp.name, "rb") as f:
                audio_bytes = f.read()
                b64 = base64.b64encode(audio_bytes).decode()
                st.markdown(f'<audio controls src="data:audio/mp3;base64,{b64}" autoplay style="width: 100%;"></audio>', unsafe_allow_html=True)
            os.unlink(tmp.name)

play_audio(f"Day {day_number}: {day_title}. {content}", f"audio_{day_number}")

# Milestone indicator
if day_number in [7, 14, 21, 28]:
    st.markdown("---")
    st.success("🎯 **Milestone achieved!** Great progress – keep going!")

# Certificate claim on day 27-28
if day_number >= 27:
    st.markdown("---")
    st.markdown('<div class="certificate"><h3>🏅 Official AI Expert Certificate</h3><p>Congratulations! You have completed the AI Foundations & Certification Course.</p><p>Click the button below to download your certificate.</p></div>', unsafe_allow_html=True)
    if st.button("📜 Download Certificate", use_container_width=True):
        # Create a simple text certificate (you can replace with PDF generation)
        cert_text = f"AI Expert Certificate\n\nThis certifies that User has successfully completed the 28‑day AI Foundations & Certification Course.\n\nDate: {datetime.now().strftime('%Y-%m-%d')}\n\nGesner Deslandes\nFounder, GlobalInternet.py"
        st.download_button("⬇️ Download Certificate (TXT)", cert_text, file_name="ai_certificate.txt", mime="text/plain")

if day_number == 28:
    st.markdown("---")
    st.markdown("## 🎓 Congratulations! You are now an AI Certified Expert.")
    st.markdown("""
    ### 📞 To continue with advanced courses or get support:
    - **Gesner Deslandes** – Founder
    - 📱 WhatsApp: (509) 4738-5663
    - 📧 Email: deslandes78@gmail.com
    - 🌐 [GlobalInternet.py](https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/)
    
    Keep practicing and applying your skills. You are ready for real‑world AI projects!
    """)

st.markdown("---")
st.caption("🤖 AI Foundations & Certification Course – 28 days to AI mastery.")
