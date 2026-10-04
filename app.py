import streamlit as st
import streamlit.components.v1 as components
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-3.5-flash-lite")

st.set_page_config(page_title="Gist — AI Text Summarizer", page_icon="📝", layout="wide")


st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&family=Space+Grotesk:wght@600;700&display=swap');

.stApp {
    background: linear-gradient(270deg, #d5dde6 0%, #d5e0eb 50%, #cfd9e3 100%);
    font-family: 'Poppins', sans-serif;
}

.twinkle-layer {
    position: fixed;
    top: 0; left: 0;
    width: 100%; height: 100%;
    pointer-events: none;
    z-index: 0;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='300'%3E%3Cpath d='M20 5 L23 17 L35 20 L23 23 L20 35 L17 23 L5 20 L17 17 Z' fill='%2391c7db'/%3E%3Cpath d='M180 90 L183 102 L195 105 L183 108 L180 120 L177 108 L165 105 L177 102 Z' fill='%2391c7db'/%3E%3Cpath d='M90 200 L93 212 L105 215 L93 218 L90 230 L87 218 L75 215 L87 212 Z' fill='%2391c7db'/%3E%3Cpath d='M250 230 L253 242 L265 245 L253 248 L250 260 L247 248 L235 245 L247 242 Z' fill='%2391c7db'/%3E%3C/svg%3E");
    background-repeat: repeat;
    background-size: 300px 300px;
    animation: twinkle 5s ease-in-out infinite;
}

@keyframes twinkle {
    0%, 100% { opacity: 0.3; }
    50% { opacity: 0.9; }
}

h1 {
    font-family: 'Space Grotesk', sans-serif;
    color: #0b3747;
    text-shadow: 
        1px 1px 0px rgba(255,255,255,1.6),
        3px 3px 6px rgba(13,59,76,1.25);
    letter-spacing: 0.5px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #0c506e;
    font-weight: 500;
    line-height: 1.7;
    width: 100%;
    display: block;
    margin-bottom: 25px;
}

h3 {
    color: #0c506e !important;
    font-weight: 700 !important;
}

div[data-testid="stFileUploader"] label p {
    color: #0c506e !important;
    font-weight: 700 !important;
    font-size: 16px !important;
}

.word-count-text {
    color: #3d788f !important;
    font-size: 13px !important;
}

div[data-testid="stTextArea"] textarea {
    background-color: #FFFFFF !important;
    border: 2px solid #0c506e !important;
    border-radius: 9px !important;
    box-shadow: 3px 3px 8px rgba(13,59,76,0.2) !important;
    color: #385661 !important;
    font-size: 15px !important;
    transition: 0.2s !important;
}

div[data-testid="stTextArea"] textarea:focus {
    border: 2px solid #C1554A !important;
    box-shadow: 4px 4px 10px rgba(193,85,74,0.3) !important;
    outline: none !important;
}

div[data-testid="stTextArea"] textarea:disabled {
    background-color: #EAF4F7 !important;
    border: 2px solid #C1554A !important;
    color: #0c506e !important;
    box-shadow: 3px 3px 8px rgba(13,59,76,0.2) !important;
    -webkit-text-fill-color: #0c506e !important;
    opacity: 1 !important;
}

div[data-testid="stTextArea"] textarea::placeholder {
    color: #8AA5AD !important;
    font-style: italic !important;
}

.st-key-short_btn_box button {
    background-color: #0c506e !important;
    color: white !important;
    border: 2px solid #0c506e !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
    width: 100% !important;
    box-shadow: 3px 3px 8px rgba(13,59,76,0.3) !important;
    transition: 0.2s !important;
}
.st-key-short_btn_box button:hover {
    background-color: #C1554A !important;
    color: white !important;
    border: 2px solid #C1554A !important;
    font-weight: 700 !important;
    transform: scale(1.03);
    box-shadow: 4px 4px 12px rgba(13,59,76,0.4) !important;
}

.st-key-detailed_btn_box button {
    background-color: #0c506e !important;
    color: white !important;
    border: 2px solid #0c506e !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
    width: 100% !important;
    box-shadow: 3px 3px 8px rgba(13,59,76,0.3) !important;
    transition: 0.2s !important;
}
.st-key-detailed_btn_box button:hover {
    background-color: #C1554A !important;
    color: white !important;
    border: 2px solid #C1554A !important;
    font-weight: 700 !important;
    transform: scale(1.03);
    box-shadow: 4px 4px 12px rgba(13,59,76,0.4) !important;
}

.st-key-clear_btn_box button {
    background-color: rgba(12, 80, 110, 0.1) !important;
    color: #0c506e !important;
    border: 2px solid #0c506e !important;
    border-radius: 8px !important;
    width: 50px !important;
    height: 50px !important;
    padding: 0 !important;
    font-size: 30px !important;
    transition: 0.2s !important;
}
.st-key-clear_btn_box button:hover {
    background-color: rgba(193, 85, 74, 0.15) !important;
    color: #C1554A !important;
    border: 2px solid #C1554A !important;
    transform: scale(1.05);
}

div[data-testid="stFileUploader"] section {
    background-color: rgba(12, 80, 110, 0.06) !important;
    border: 2px dashed #0c506e !important;
    border-radius: 12px !important;
}

div[data-testid="stFileUploader"] section > div > span {
    color: #0c506e !important;
    font-weight: 600 !important;
}

div[data-testid="stFileUploaderDropzoneInstructions"] div span {
    color: #C1554A !important;
}

div[data-testid="stFileUploader"] section button {
    background-color: #0c506e !important;
    color: white !important;
    border: 2px solid #0c506e !important;
    border-radius: 8px !important;
    font-weight: 600 !important;
    transition: 0.2s !important;
}

div[data-testid="stFileUploader"] section button:hover {
    background-color: #C1554A !important;
    border: 2px solid #C1554A !important;
    color: white !important;
}

</style>

<div class="twinkle-layer"></div>
""", unsafe_allow_html=True)


# ---------- Session state ----------
if "input_text" not in st.session_state:
    st.session_state.input_text = ""
if "clear_trigger" not in st.session_state:
    st.session_state.clear_trigger = False
if "summary_output" not in st.session_state:
    st.session_state.summary_output = ""
if "last_uploaded_name" not in st.session_state:
    st.session_state.last_uploaded_name = None

if st.session_state.clear_trigger:
    st.session_state.input_text = ""
    st.session_state.summary_output = ""
    st.session_state.clear_trigger = False
    st.session_state.last_uploaded_name = None

# ---------- Main heading ----------
st.markdown("<h1 style='text-align:center;'>Gist — AI Text Summarizer</h1>", unsafe_allow_html=True)

# ---------- Description ----------
st.markdown("<p class='subtitle'>Gist reads your text and gives you back exactly what matters. Paste an article, a report, or your notes, and choose a quick overview or a fuller, more detailed breakdown — all in seconds, powered by AI.</p>", unsafe_allow_html=True)
# ---------- Two columns ----------
col1, col2 = st.columns(2)

with col1:
    uploaded_file = st.file_uploader("Upload your file here, or paste your text below.", type=["txt"])
    if uploaded_file is not None and uploaded_file.name != st.session_state.last_uploaded_name:
        st.session_state.input_text = uploaded_file.read().decode("utf-8")
        st.session_state.last_uploaded_name = uploaded_file.name
        st.rerun()

    user_text = st.text_area(
        "input",
        height=320,
        placeholder="Paste or type your text here... (or press Ctrl+V to paste)",
        label_visibility="collapsed",
        key="input_text"
    )
    word_count_input = len(user_text.split()) if user_text else 0
    st.markdown(f"<p class='word-count-text'>Word count: {word_count_input}</p>", unsafe_allow_html=True)

    btn_col1, btn_col2, btn_col3 = st.columns([1, 1, 0.4])
    with btn_col1:
        with st.container(key="short_btn_box"):
            short_btn = st.button("Short Summary", use_container_width=True)
    with btn_col2:
        with st.container(key="detailed_btn_box"):
            detailed_btn = st.button("Detailed Summary", use_container_width=True)
    with btn_col3:
        with st.container(key="clear_btn_box"):
            clear_btn = st.button("🗑️", use_container_width=True, help="Clear text")

with col2:
    st.markdown("<div style='height: 52px;'></div>", unsafe_allow_html=True)
    st.subheader("Summary")
    if st.session_state.summary_output:
        st.text_area(
            "output",
            value=st.session_state.summary_output,
            height=320,
            label_visibility="collapsed",
            disabled=True
        )
    else:
        st.text_area(
            "output",
            value="",
            height=320,
            placeholder="Your summary will appear here...",
            label_visibility="collapsed",
            disabled=True
        )

    output_word_count = len(st.session_state.summary_output.split()) if st.session_state.summary_output else 0

    wc_col, copy_col = st.columns([3, 1])
    with wc_col:
        st.markdown(f"<p class='word-count-text'>Word count: {output_word_count}</p>", unsafe_allow_html=True)
    with copy_col:
        if st.session_state.summary_output:
            copy_text = st.session_state.summary_output.replace("`", "'").replace("\n", "\\n")
            components.html(f"""
                <div style="display:flex; justify-content:flex-end;">
                    <button onclick="navigator.clipboard.writeText(`{copy_text}`)"
                        onmouseover="this.style.borderColor='#C1554A'; this.style.color='#C1554A'; this.style.boxShadow='3px 3px 8px rgba(193,85,74,0.3)';"
                        onmouseout="this.style.borderColor='#0c506e'; this.style.color='#0c506e'; this.style.boxShadow='3px 3px 8px rgba(13,59,76,0.2)';"
                        style="padding:6px 16px; border-radius:8px; border:2px solid #0c506e; color:#0c506e; background:white; cursor:pointer; font-weight:600; font-size:13px; box-shadow:3px 3px 8px rgba(13,59,76,0.2); transition:0.2s;">
                        📋 Copy
                    </button>
                </div>
            """, height=40)

# ---------- Button logic ----------
if clear_btn:
    st.session_state.clear_trigger = True
    st.rerun()

if short_btn or detailed_btn:
    if user_text.strip() == "":
        st.session_state.summary_output = "⚠️ Please paste some text first."
    else:
        input_word_count = len(user_text.split())

        if short_btn:
            target_words = max(10, round(input_word_count * 0.35))
            instruction = f"Write a CONDENSED summary of approximately {target_words} words. Keep only the most essential points, significantly shorter than the original."
        else:
            target_words = round(input_word_count * 1.3)
            instruction = f"Write a DETAILED, EXPANDED summary of approximately {target_words} words. Add context, explanation, and elaboration on the key ideas — this should be longer and more thorough than the original text, not just a restatement."

        prompt = f"{instruction}\n\nText to summarize:\n{user_text}"

        with st.spinner("Summarizing..."):
            try:
                response = model.generate_content(prompt)
                st.session_state.summary_output = response.text
            except Exception:
                st.session_state.summary_output = "Something went wrong. Please try again."
    st.rerun()

# ---------- Footer ----------
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'><span style='color:#C1554A;'>© 2026 Gist</span> <span style='color:#0c506e;'>— Built with Python, Streamlit & Google Gemini API</span></p>", unsafe_allow_html=True)

