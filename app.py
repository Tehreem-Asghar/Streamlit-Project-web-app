import streamlit as st
import random

# Page Configuration
st.set_page_config(
    page_title="🌱 Growth Mindset Challenge",
    page_icon="🌱",
    layout="centered",
)


# Custom CSS for Styling
st.markdown(
    """
    <style>
    /* General Styling */
    body {
        background: linear-gradient(135deg, #1e3c72, #2a5298);
        font-family: 'Arial', sans-serif;
        color: white;
    }
    .main {
        background: rgba(255, 255, 255, 0.1);
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        backdrop-filter: blur(10px);
    }
    h1 {
        color: #ffffff;
        text-align: center;
        font-family: 'Georgia', serif;
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }
    @media (max-width: 600px) {
        h1 {
            font-size: 2rem; /* Smaller title for mobile screens */
        }
    }
    h2 {
        color: #ffffff;
        font-family: 'Georgia', serif;
        font-size: 2rem;
        margin-top: 1.5rem;
    }
    .stButton button {
        background: linear-gradient(135deg, #2e86c1, #148f77);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 10px 20px;
        font-size: 1rem;
        font-weight: bold;
        transition: transform 0.2s, box-shadow 0.2s;
    }
    .stButton button:hover {
        transform: scale(1.05);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        color : #ffffff
    }
    .stTextInput input, .stTextArea textarea {
        border-radius: 10px;
        border: 1px solid #ccc;
        padding: 10px;
        font-size: 1rem;
        background: rgba(255, 255, 255, 0.8);
    }
    .stSuccess {
        color: #28a745;
        font-weight: bold;
    }
    .stInfo {
        color: #17a2b8;
        font-weight: bold;
    }
    .stError {
        color: #dc3545;
        font-weight: bold;
    }
    .quote-box {
        background: rgba(255, 255, 255, 0.2);
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .footer {
        text-align: center;
        margin-top: 2rem;
        color: #000000;
        font-size: 0.9rem;
    }
    .card {
        background: rgba(255, 255, 255, 0.2);
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin-bottom: 1.5rem;
    }
    .progress-bar {
        background: linear-gradient(135deg, #2e86c1, #148f77);
        border-radius: 10px;
        height: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# App Title and Introduction
st.header(""" 

🌱 Growth Mindset Challenge 

""")
st.markdown(
    """
    <div class="card">
        Welcome to the **Growth Mindset Challenge**! 🌟  
        A growth mindset is the belief that you can develop your abilities through effort, learning, and persistence.  
        Let’s explore how you can embrace challenges, learn from mistakes, and achieve your full potential!
    </div>
    """,
    unsafe_allow_html=True,
)

# Section 1: What is a Growth Mindset?
st.header("What is a Growth Mindset?")
st.markdown(
    """
    <div class="card">
        A **growth mindset** is the understanding that your talents and abilities can be developed through dedication and hard work. Unlike a fixed mindset, which assumes that skills are innate and unchangeable, a growth mindset empowers you to:
        - **Embrace Challenges**: See obstacles as opportunities to grow.
        - **Learn from Mistakes**: Use failures as stepping stones to success.
        - **Persist Through Setbacks**: Stay motivated even when things get tough.
        - **Celebrate Effort**: Focus on the process, not just the outcome.
        - **Stay Curious**: Always seek to learn and improve.
    </div>
    """,
    unsafe_allow_html=True,
)

# Section 2: Growth Mindset Tips
st.header("Tips to Develop a Growth Mindset")
if st.button("Show Tips"):
    st.balloons()  # Balloons animation on button click
    st.markdown(
        """
        <div class="card">
            Here are some actionable tips to cultivate a growth mindset:
            - **Set Learning Goals**: Focus on improving skills rather than achieving perfection.
            - **Embrace Challenges**: Step out of your comfort zone and take on new tasks.
            - **Learn from Feedback**: Use constructive criticism to grow.
            - **Practice Resilience**: Bounce back from setbacks with a positive attitude.
            - **Celebrate Progress**: Acknowledge and reward your efforts, no matter how small.
        </div>
        """,
        unsafe_allow_html=True,
    )

# Section 3: User Feedback
st.header("Share Your Thoughts")
user_input = st.text_input("How has a growth mindset helped you in your journey?")
if user_input:
    st.success(f"Thank you for sharing! 🌟 Your feedback: **{user_input}**")

# Section 4: Growth Mindset Quiz
st.header("Test Your Mindset")
st.write("Let’s see how well you understand the growth mindset!")

question = st.radio(
    "What would you do if you faced a difficult problem?",
    ("I’ll try to solve it and learn from the process", "I’ll ask for help and observe how others solve it", "I’ll avoid it because it’s too hard")
)

progress = 0  # For progress bar

if question == "I’ll try to solve it and learn from the process":
    st.success("✅ That’s the spirit! A growth mindset is all about learning through effort.")
    progress += 50
elif question == "I’ll ask for help and observe how others solve it":
    st.info("🤔 Collaboration is great, but don’t forget to challenge yourself too!")
    progress += 30
else:
    st.error("❌ Avoidance limits growth. Embrace challenges to unlock your potential!")

# Progress Bar
st.write("### Your Growth Mindset Progress:")
st.markdown(
    f"""
    <div class="progress-bar" style="width: {progress}%;"></div>
    """,
    unsafe_allow_html=True,
)

# Section 5: Motivational Quotes
st.header("Need a Boost?")
st.markdown("Here’s a motivational quote to keep you inspired:")

# List of Motivational Quotes
quotes = [
    "🌟 Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill",
    "🚀 Your only limit is your mind. – Unknown",
    "💡 Difficulties in life are intended to make us better, not bitter. – Unknown",
    "🔥 Believe in yourself and you’re halfway there. – Theodore Roosevelt",
    "🌱 The journey of a thousand miles begins with a single step. – Lao Tzu",
]

# Display a Random Quote
if st.button("Get Motivated"):
    st.balloons()  # Balloons animation on button click
    random_quote = random.choice(quotes)
    st.markdown(
        f"""
        <div class="quote-box">
            <p>💬 <strong>{random_quote}</strong></p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Footer
st.markdown("---")
st.markdown(
    """
    <div class="footer">
        🚀 Keep going! Adopt a growth mindset, embrace challenges, and never stop learning. 🌱
    </div>
    """,
    unsafe_allow_html=True,
)