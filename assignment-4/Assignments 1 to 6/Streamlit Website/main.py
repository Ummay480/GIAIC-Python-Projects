import streamlit as st

# Page configuration
st.set_page_config(page_title="Ummay Kulsoom | Portfolio", page_icon="💻", layout="centered")

# Title
st.title("👩‍💻 Ummay Kulsoom - Web Developer")
st.write("Welcome to my portfolio website built using Python and Streamlit!")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About Me", "Projects", "Contact"])

# Home Page
if page == "Home":
    st.header("🏠 Home")
    st.write("Hi there! I'm Ummay Kulsoom, a passionate web developer skilled in HTML, CSS, TypeScript, Next.js, Python, and Streamlit.")
    
    name = st.text_input("What's your name?")
    if name:
        st.success(f"Hello {name}! Glad you're here. Feel free to explore my portfolio.")

# About Me Page
elif page == "About Me":
    st.header("👩‍💼 About Me")
    st.write("""
    I'm a dedicated and creative web developer with experience in:
    
    - 🔹 Front-end development (HTML, CSS, TypeScript, Next.js, Python)
    - 🔹 Resume builder projects
    - 🔹 E-commerce marketplace projects            
    - 🔹 QCommerce restaurant project
    - 🔹 Furniture.io project
    - 🔹 Streamlit web apps
    - 🔹 WordPress and Webflow basics
    
    I enjoy solving problems, building beautiful UIs, and turning ideas into reality.
    """)
    st.write("📚 Currently studying Web 3.0, Metaverse, and Generative AI at GIAIC - Governor House Karachi")

# Projects Page
elif page == "Projects":
    st.header("💼 My Projects")

    st.subheader("🔧 Money-making-machine")
    st.write("A Python project that calculates earnings over time based on input data.")

    st.subheader("🧠 Mood Tracker")
    st.write("A web app using Streamlit that tracks and analyzes your mood over time.")

    st.subheader("🔐 Password Generator")
    st.write("A Python project to generate random passwords based on user-defined criteria.")

    st.subheader("🔒 Password Strength Checker")
    st.write("A Python tool that checks the strength of a password.")

    st.subheader("🔄 Unit Converter")
    st.write("A simple unit conversion app that allows users to convert units between various categories.")

    st.subheader("📚 Personal Library")
    st.write("A Python project to manage and track your personal library collection.")

    st.subheader("🔑 Chatbot Authentication")
    st.write("A chatbot that verifies user identity for secure access.")

    st.subheader("❓ QA Chatbot")
    st.write("A chatbot designed to answer common questions using a knowledge base.")

    st.subheader("🎮 Quiz App")
    st.write("An interactive quiz application using Streamlit and Python.")

    st.subheader("😂 Random Joke Generator")
    st.write("A fun app that generates random jokes using an API.")

    st.subheader("🤖 Simple Agent")
    st.write("A Python-based intelligent agent for solving problems.")

    st.subheader("🌐 Simple API")
    st.write("A simple Python-based API with endpoints to handle basic requests.")

    st.subheader("🧮 Simple Calculator")
    st.write("A basic Python calculator that performs arithmetic operations.")

    st.subheader("💡 Smart Calculator")
    st.write("An advanced calculator that provides additional features like square roots and exponents.")

    st.subheader("⚖️ BMI Calculator")
    st.write("A Python app to calculate your Body Mass Index (BMI) based on height and weight.")

    st.subheader("🎲 Even-Odd Checker")
    st.write("A Python app to check if a number is even or odd.")

    st.subheader("🔑 Password Generator")
    st.write("A password generator for creating secure passwords based on length and complexity.")

    st.subheader("🌍 Time Zone App")
    st.write("A Python app to find the current time in any given timezone.")

    st.subheader("🎲 Number Guessing Game")
    st.write("A fun number guessing game where the user has to guess a number within a range.")

    st.subheader("📈 Growth Mindset")
    st.write("A project designed to help users develop a growth mindset with positive affirmations.")

    st.subheader("📝 Mad Libs Game")
    st.write("A fun word game that generates silly stories by filling in blanks with user input.")

    st.subheader("🧠 Guess the Number Game (Computer)")
    st.write("A game where the computer randomly selects a number and the user has to guess it.")

    st.subheader("🧠 Guess the Number Game (User)")
    st.write("A game where the user selects a number and the computer tries to guess it.")

    st.subheader("✋ Rock, Paper, Scissors")
    st.write("A simple Python game of Rock, Paper, Scissors between user and computer.")

    st.subheader("⏳ Countdown Timer")
    st.write("A Python countdown timer that alerts the user when the timer reaches zero.")

    st.subheader("⚖️ BMI Calculator (again!)")
    st.write("A second version of the BMI calculator with additional features and improvements.")

    st.subheader("🌐 Streamlit Website")
    st.write("This portfolio website is built using Streamlit to showcase my projects and skills.")

# Contact Page
elif page == "Contact":
    st.header("📬 Contact Me")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    if st.button("Submit"):
        st.success("Thank you! Your message has been received. I'll get back to you soon.")

    st.write("📧 Email: kulsoom0324@gmail.com")
    st.write("📍 Location: Nishter Road, Garden, Karachi")
    st.write("🌐 GitHub: [@ummay480](https://github.com/ummay480)")
