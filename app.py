import streamlit as st
import random

# Web App Title
st.title("🌱 Growth Mindset Challenge")

# Introduction
st.write("""
### What is a Growth Mindset?
A growth mindset means that we can improve our skills and abilities through hard work, dedication, and learning.
""")

# Button for Tips
if st.button("See Growth Mindset Tips"):
    st.write("""
    ✅ Accept challenges  
    ✅ Learn from mistakes  
    ✅ Keep a positive mindset  
    ✅ Set learning goals  
    """)

# User Feedback
user_input = st.text_input("Share your thoughts: How does a growth mindset help you?")
if user_input:
    st.write("Your feedback:", user_input)

# Growth Mindset Quiz
st.write("## Growth Mindset Quiz")
question = st.radio(
    "If you face a difficult problem, what will you do?",
    ("I will try and learn", "I will see how others solve it", "I will give up, this is not for me")
)

progress = 0  # For progress bar

if question == "I will try and learn":
    st.success("✅ Absolutely right! This is the essence of a growth mindset.")
    progress += 50
elif question == "I will see how others solve it":
    st.info("🤔 Good approach, but trying yourself is also important.")
    progress += 30
else:
    st.error("❌ This is a fixed mindset. Always try to learn!")

# Progress Bar
st.write("### Your Growth Mindset Progress:")
st.progress(progress)

# Motivational Quotes Section
quotes = [
    "🌟 Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "🚀 Your only limit is your mind.",
    "💡 Difficulties in life are intended to make us better, not bitter.",
    "🔥 Believe in yourself and you’re halfway there."
]

if st.button("Need Motivation?"):
    st.write(random.choice(quotes))

# Final Message
st.write("### 🏆 Keep Going! Adopt a growth mindset and always strive to learn. 🚀")


























# import streamlit as st
# import random

# # Web App Title
# st.title("🌱 Growth Mindset Challenge")

# # Introduction
# st.write("""
# ### Growth Mindset Kya Hai?
# Growth mindset ka matlab hai ke hum apni skills aur abilities improve kar sakte hain 
# mehnat, lagan aur seekhnay se.
# """)

# # Button for Tips
# if st.button("Growth Mindset Tips Dekho"):
#     st.write("""
#     ✅ Challenges ko accept karo  
#     ✅ Ghaltiyon se seekho  
#     ✅ Positive mindset rakho  
#     ✅ Learning goals set karo  
#     """)

# # User Feedback
# user_input = st.text_input("Apni soch share karein: Growth mindset kaise help karta hai?")
# if user_input:
#     st.write("Aapka feedback:", user_input)

# # Growth Mindset Quiz
# st.write("## Growth Mindset Quiz")
# question = st.radio(
#     "Agar tum ek mushkil problem face kar rahi ho, tum kya karogi?",
#     ("Try karungi aur seekhungi", "Dekhungi ke koi aur kaise solve karta hai", "Chor dungi, yeh mere bas ka nahi")
# )

# progress = 0  # Progress bar ke liye

# if question == "Try karungi aur seekhungi":
#     st.success("✅ Bilkul sahi! Growth mindset ka yahi concept hai.")
#     progress += 50
# elif question == "Dekhungi ke koi aur kaise solve karta hai":
#     st.info("🤔 Achha approach hai, magar khud bhi try karna zaroori hai.")
#     progress += 30
# else:
#     st.error("❌ Yeh fixed mindset hai, hamesha seekhne ki koshish karo!")

# # Progress Bar
# st.write("### Tumhari Growth Mindset Progress:")
# st.progress(progress)

# # Motivational Quotes Section
# quotes = [
#     "🌟 Success is not final, failure is not fatal: It is the courage to continue that counts.",
#     "🚀 Your only limit is your mind.",
#     "💡 Difficulties in life are intended to make us better, not bitter.",
#     "🔥 Believe in yourself and you’re halfway there."
# ]

# if st.button("Motivation Chahiye?"):
#     st.write(random.choice(quotes))

# # Final Message
# st.write("### 🏆 Keep Going! Growth mindset adopt karo aur hamesha seekhne ki koshish karo. 🚀")
