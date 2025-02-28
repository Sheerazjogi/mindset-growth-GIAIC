import streamlit as st

st.set_page_config(page_title="Growth Mindset Challenge", page_icon="✾")

st.title("Growth Mindset Challenge")

st.header("Welcome to Growth Mindset Challenge 🌱")
st.write("Discover how adopting a growth mindset can transform your personal and academic life.")

# Quote section
st.header("💡 Today's Growth Mindset Challenge Quote")
st.write("Success is not about being the best; it's about getting better every day. 🌱")

st.header("What is your Challenge Today?")
user_input = st.text_input("Describe a challenge you are facing:")

# Condition
if user_input:
    st.success(f"You are facing: {user_input}. Keep striving with determination—every step brings you closer to your goal!")
else:
    st.warning("Share your challenge and take the first step toward getting started.")

# Reflection
st.header("Reflect on Your Learning")
reflection = st.text_area("Write your outcome here:")

if reflection:
    st.success(f"Excellent perspective! Your analysis is insightful: {reflection}")
else:
    st.info("Reflecting on past experiences helps you grow! Share your difficulties.")

st.header("Celebrate Your Success! 🏆")
achievement = st.text_input("Share a recent achievement of yours.")

if achievement:
    st.success(f"🎉 Incredible! You have accomplished something awesome! You achieved: {achievement}")
else:
    st.info("Every achievement matters, big or small! Share yours now! 🎉")

# Footer
st.write("- - -")
st.write("You are doing amazing—keep going! Every step forward is progress! ✨💪")
st.write("*Created by Sheeraz Ali🔴🚫*")



