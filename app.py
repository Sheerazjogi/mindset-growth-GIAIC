#streamlit

import streamlit as st

st.set_page_config(page_title="growth mindset challenge",project_icon="✾")

st.title ("Growth Mindset Challenge")

st.header("Welcome to Growth Mindset Challenge 🌱")
st.write("Discover how adopting a growth mindset can transform your personal and academic life.")

#quote section

st.header("💡Today's Growth Mindset Challenge quote")
st.write("Success is not about being the best; it's about getting better every day. 🌱")

st.header("what is your Challenge Today?")
user_input =st.text_input("Describe a Challenge You are facing:")


#condition
if user_input:
    st.success(f"you are facing: {user_input}.Keep striving with determination—every step brings you closer to your goal!")
else:
  st.warning("Share your challenge and take the first step toward getting started.")

  #reflex
  st.header("Reflect on Your Learning")
  reflection = st.text_area("Write Your Outcome here:")

  if reflection:
    st.success(f"Excellent perspective! Your analysis is insightful: {reflection}")
  else:
    st.info("Reflecting on past experience help you grow! share your difficulties")
    
st.header("Celebrate your success! 🏆")
achievement = st.text_input("Share a recent achievement of yours.")

if achievement:
    st.success(f" 🎉Incredible! You have accomplished awesome!|Amazing! You achieved: {achievement}")
else:
    st.info("Every achievement matters, big or small! Share yours now! 🎉")
    
    #footer

    st.write("- - -")
    st.write("You are doing amazing—keep going! Every step forward is progress! ✨💪")
    st.write("** Created by Sheeraz Ali🔴🚫**")