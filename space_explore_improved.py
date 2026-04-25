
import streamlit as st
import pandas as pd
import random

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Space Explorer 🚀", layout="wide")

# ---------------- CSS (BLACK THEME + FIX DROPDOWN) ----------------
st.markdown("""
    <style>
        /* Main background */
        .stApp {
            background-color: #000000;
        }

        /* Sidebar */
        section[data-testid="stSidebar"] {
            background-color: #000000;
        }

        /* Text */
        h1, h2, h3, h4, h5, h6, p, div, span, label {
            color: white !important;
        }

        /* Buttons */
        .stButton>button {
            background-color: #111111;
            color: white;
            border-radius: 10px;
            border: 1px solid #333;
        }

        /* INPUT FIELDS FIX */
        input, textarea {
            background-color: #222222 !important;
            color: white !important;
        }

        /* Date & Time input fix */
        .stDateInput input, .stTimeInput input {
            background-color: #222222 !important;
            color: white !important;
        }

        /* Selectbox (closed view) */
        div[data-baseweb="select"] {
            background-color: #222222 !important;
            color: white !important;
        }

        div[data-baseweb="select"] span {
            color: white !important;
        }

        /* Dropdown list (opened) */
        ul[role="listbox"] li {
            background-color: #222222 !important;
            color: white !important;
        }

        ul[role="listbox"] li:hover {
            background-color: #444444 !important;
        }

        /* Radio */
        .stRadio > div {
            color: white;
        }

        /* Tables */
        .stDataFrame, .stTable {
            background-color: #111111;
        }
    </style>
""", unsafe_allow_html=True)
# ---------------- TITLE ----------------
st.title("🚀 Space Explorer Adventure")

# Sidebar navigation
st.sidebar.title("Navigation")
choice = st.sidebar.radio("Navigate to:", ["Home","Space Quiz","Mission Planner"])

# ---------------- SPACE FACTS ----------------
space_facts = [
    "Jupiter is so big that all the other planets could fit inside it.",
    "A day on Venus is longer than a year on Venus.",
    "Neutron stars can spin 600 times per second.",
    "There are more stars in the universe than grains of sand on Earth.",
    "Saturn could float in water because it is mostly gas.",
    "The footprints on the Moon will stay there for millions of years.",
    "Mars has the tallest volcano in the solar system.",
    "One million Earths could fit inside the Sun."
]

# ---------------- HOME ----------------
if choice == "Home":
    st.header("🌌 Welcome to Space Explorer Adventure!")

    col1, col2 = st.columns(2)

    with col1:
        st.write("""
            Embark on an interstellar journey!  
            - Take a fun Space Quiz  
            - Plan your Space Mission  
            - Learn amazing space facts  
        """)

        st.subheader("🌠 Discover a Space Fact")

        if st.button("Show Me a Space Fact"):
            fact = random.choice(space_facts)
            st.info(f"💡 {fact}")

    with col2:
        st.image("https://images.unsplash.com/photo-1446776811953-b23d57bd21aa", use_container_width=True)

# ---------------- QUIZ ----------------
elif choice == "Space Quiz":
    st.header("👨🏻‍🚀 Test Your Space Knowledge")

    st.image("https://images.unsplash.com/photo-1462331940025-496dfbfc7564", use_container_width=True)

    st.progress(0.66)

    st.subheader("Answer the following questions")

    q1 = st.radio("🌍 Q1: Largest planet?", ["Earth", "Jupiter", "Mars"])
    q2 = st.radio("🚀 Q2: First human in space?", ["Neil Armstrong", "Buzz Aldrin", "Yuri Gagarin"])
    q3 = st.radio("🌌 Q3: Our galaxy?", ["Milky Way Galaxy","Andromeda Galaxy", "Whirlpool Galaxy"])

    if st.button("🚀 Submit Quiz"):
        score = 0

        score += 1 if q1 == "Jupiter" else 0
        score += 1 if q2 == "Yuri Gagarin" else 0
        score += 1 if q3 == "Milky Way Galaxy" else 0

        if score == 3:
            st.balloons()
            st.success("🌟 Perfect Score! You're a Space Master! 🚀")
        elif score == 2:
            st.info("👏 Great job! Just one step away from perfection.")
        elif score == 1:
            st.warning("👍 Not bad! Keep learning about space.")
        else:
            st.error("😅 Oops! Try again and explore more.")

        st.subheader(f"📊 Your Score: {score}/3")

        results = pd.DataFrame({
            "Question": ["Q1", "Q2", "Q3"],
            "Your Answer": [q1, q2, q3],
            "Correct Answer": ["Jupiter", "Yuri Gagarin", "Milky Way Galaxy"]
        })

        st.dataframe(results, use_container_width=True)

# ---------------- MISSION ----------------
elif choice == "Mission Planner":
    st.header("🛰️ Plan Your Space Mission")

    st.image("https://images.unsplash.com/photo-1451187580459-43490279c0fa", use_container_width=True)

    spacecraft = st.text_input("🚀 Spacecraft Name", "Star Explorer")
    launch_date = st.date_input("📅 Launch Date")
    launch_time = st.time_input("⏰ Launch Time")

    spaceship_type = st.selectbox("🛸 Spaceship Type", ["Rocket", "Shuttle", "Space Station"])

    category = st.selectbox("🌟 Quote Category", ["Exploration","Discovery","Adventure"])
    quotes = {
        "Exploration": "To explore the universe is to explore ourselves.",
        "Discovery": "Discovery is seeing what everybody else has seen, and thinking what nobody else has thought.",
        "Adventure": "Space is an adventure worth taking."
    }

    st.info(f"💡 {quotes[category]}")

    if st.button("💾 Save Mission"):
        st.success(f"""
        🚀 Mission '{spacecraft}' is scheduled!  
        📅 {launch_date}  
        ⏰ {launch_time}  
        🛸 Type: {spaceship_type}
        """)
