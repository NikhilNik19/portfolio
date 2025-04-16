import streamlit as st
from streamlit_lottie import st_lottie
import requests
import time
#Page configuration with improved metadata
st.set_page_config(
    page_title="Badavath Gayathri | Data Scientist Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load Lottie animations
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Preload animations
lottie_coding = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_tno6cg2w.json")
lottie_ai = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_gn0tojcq.json")
lottie_contact = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_u8jppxsl.json")

# Improved animated intro with progress bar
def show_intro():
    intro_html = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700&display=swap');
    
    .intro-container {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        z-index: 9999;
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        animation: fadeOut 1s ease-in-out 4s forwards;
    }
    
    .name-text {
        font-family: 'Orbitron', sans-serif;
        font-size: 4.5rem;
        color: #00ffff;
        margin-bottom: 2rem;
        text-shadow: 0 0 20px #0ff, 0 0 40px #0ff;
        animation: glowText 2s ease-in-out infinite alternate;
    }
    
    .title-text {
        font-family: 'Orbitron', sans-serif;
        font-size: 1.5rem;
        color: #ffffff;
        margin-bottom: 3rem;
        opacity: 0.8;
    }
    
    .progress-container {
        width: 300px;
        height: 8px;
        background: rgba(255, 255, 255, 0.2);
        border-radius: 10px;
        overflow: hidden;
    }
    
    .progress-bar {
        height: 100%;
        width: 0%;
        background: linear-gradient(90deg, #00ffff, #0080ff);
        border-radius: 10px;
        animation: progress 4s ease-in-out forwards;
    }
    
    @keyframes glowText {
        from { text-shadow: 0 0 10px #0ff; }
        to { text-shadow: 0 0 25px #0ff, 0 0 45px #0ff; }
    }
    
    @keyframes progress {
        0% { width: 0%; }
        100% { width: 100%; }
    }
    
    @keyframes fadeOut {
        0% { opacity: 1; }
        100% { opacity: 0; visibility: hidden; }
    }
    </style>
    
    <div class="intro-container">
        <div class="name-text">GAYATHRI BADAVATH</div>
        <div class="title-text">Data Scientist | ML Engineer | Developer</div>
        <div class="progress-container">
            <div class="progress-bar"></div>
        </div>
    </div>
    
    <script>
        // Force hide intro after animation completes
        setTimeout(function() {
            document.querySelector('.intro-container').style.display = 'none';
        }, 5000);
    </script>
    """
    st.markdown(intro_html, unsafe_allow_html=True)
    time.sleep(4.5)

show_intro()

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_tno6cg2w.json")

# Custom CSS with animated gradient background and floating panels
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Raleway:wght@400;700&display=swap');

        html, body, [class*="css"]  {
            font-family: 'Raleway', sans-serif;
            animation: gradientBG 15s ease infinite;
            background: linear-gradient(-45deg, #e0c3fc, #8ec5fc, #fbc2eb, #a6c1ee);
            background-size: 400% 400%;
            color: #212529;
        }

        @keyframes gradientBG {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        .title {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 40px;
            margin-top: 2rem;
        }

        .text-section {
            max-width: 600px;
        }

        .subtitle {
            font-size: 22px;
            color: #0d6efd;
            margin-bottom: 1rem;
        }

        .social-icons {
            display: flex;
            gap: 30px;
            font-size: 20px;
            margin-bottom: 20px;
        }

        .hero-button {
            margin-top: 10px;
        }

        .hero-button a {
            background: linear-gradient(to right, #6a11cb, #2575fc);
            color: white;
            padding: 0.8rem 1.5rem;
            border-radius: 10px;
            text-decoration: none;
            font-weight: bold;
        }

        .section-box {
            border-radius: 15px;
            padding: 2rem;
            margin-top: 2rem;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
            backdrop-filter: blur(10px);
            background-color: rgba(255, 255, 255, 0.6);
        }

        .highlight-boxes {
            display: flex;
            gap: 20px;
            margin-top: 1.5rem;
        }

        .highlight {
            flex: 1;
            padding: 1rem;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
            background: white;
        }

        .ds { background-color: #f3e8ff; }
        .dev { background-color: #e8f0ff; }
        .research { background-color: #ffe8e8; }

        /* Floating Colors for each section */
        #about { background-color: rgba(255, 253, 245, 0.85); }
        #education { background-color: rgba(240, 249, 255, 0.85); }
        #projects { background-color: rgba(255, 240, 245, 0.85); }
        #experience { background-color: rgba(245, 255, 248, 0.85); }
        #contact { background-color: rgba(240, 240, 255, 0.85); }

        #contact form input,
        #contact form textarea {
            width: 100%;
            margin-top: 10px;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }

        #contact form button {
            margin-top: 10px;
            padding: 10px 20px;
            background-color: #0d6efd;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
    </style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="title">
    <div class="text-section">
        <h1><strong>Badavath Gayathri</strong></h1>
        <div class="subtitle">Data Scientist | Machine Learning Engineer | Software Developer</div>
        <div class="social-icons">
            <a href="mailto:badavathgayathri02@gmail.com">📧 Email</a>
            <a href="https://www.linkedin.com/in/badavath-gayathri-74548a237/" target="_blank">🔗 LinkedIn</a>
            <a href="https://github.com/" target="_blank">💻 GitHub</a>
        </div>
        <div class="hero-button">
            <a href="#contact">Contact Me</a>
        </div>
    </div>
    <div>
""", unsafe_allow_html=True)

st_lottie(lottie_coding, height=300, key="hero")

st.markdown("""
    </div>
</div>
""", unsafe_allow_html=True)

# About Me Section
st.markdown("""
<div id="about" class="section-box">
    <h2>👋 About Me</h2>
    <p>I'm a passionate Data Scientist and Software Engineer with a strong foundation in machine learning algorithms, statistical modeling, and software development. Currently pursuing my BS in Data Science from IIT Madras, I thrive on transforming complex data into actionable insights and building intelligent systems that solve real-world problems.</p>
    <div class="highlight-boxes">
        <div class="highlight ds">
            <h4 style="color: #6610f2;">Data Science</h4>
            <p>Machine Learning, Deep Learning, Statistical Analysis</p>
        </div>
        <div class="highlight dev">
            <h4 style="color: #0d6efd;">Software Dev</h4>
            <p>Full-stack Development, Algorithms, System Design</p>
        </div>
        <div class="highlight research">
            <h4 style="color: #dc3545;">Research</h4>
            <p>Differential Privacy, AI Ethics, Innovative Solutions</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Education
st.markdown("""
<div id="education" class="section-box">
    <h2>🎓 Education</h2>
    <ul>
        <li><strong>B.Tech in Computer Science Engineering</strong>, NIT Andhra Pradesh (2020–2024) – CGPA: 7.97</li>
        <li><strong>Intermediate</strong>, Alphores Junior College (2018–2020) – 96.1%</li>
        <li><strong>SSC</strong>, Alphores High School (2017–2018) – CGPA: 9.8</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Projects
st.markdown("""
<div id="projects" class="section-box">
    <h2>💼 Projects</h2>
    <ul>
        <li><strong>PrivacyVerse:</strong> Implemented differential privacy in ML models (SGD, GAN, CGAN, PATE) with 20% improvement in privacy-preserving accuracy. <em>Tools: Python, TensorFlow, PyTorch</em></li>
        <li><strong>Sorting Visualizer:</strong> Interactive visualization of sorting algorithms using HTML, CSS, JavaScript.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Experience
st.markdown("""
<div id="experience" class="section-box">
    <h2>👩‍💻 Experience</h2>
    <p><strong>Machine Learning Intern</strong> @ NIT Warangal (Jun–Jul 2022)</p>
    <ul>
        <li>Developed image colorization algorithm using RGB to Lab conversion.</li>
        <li>Used Caffe for classification & segmentation, improving processing time by 13%.</li>
        <li>Extended to video colorization and optimized neural network performance by 20%.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Contact
st.markdown("""
<div id="contact" class="section-box">
    <h2>📬 Contact Me</h2>
    <form action="https://formspree.io/f/mwkgnldl" method="POST">
        <input type="text" name="name" placeholder="Your Name" required><br>
        <input type="email" name="email" placeholder="Your Email" required><br>
        <textarea name="message" rows="5" placeholder="Your Message" required></textarea><br>
        <button type="submit">Send</button>
    </form>
    <p style="margin-top: 10px;">Or reach out via Email / LinkedIn above!</p>
</div>
""", unsafe_allow_html=True)