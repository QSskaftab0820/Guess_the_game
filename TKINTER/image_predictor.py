import streamlit as st
import random

# Word-to-image mapping (you can customize or expand this)
image_dict = {
    "Dog": "https://th.bing.com/th/id/OIP.sweV5y8OvabQrCD2IMdYJgHaFj?rs=1&pid=ImgDetMain",
    "Cat": "https://th.bing.com/th/id/OIP.TzP2op3lkhlTh6oOHamacAHaHa?w=249&h=249&c=8&rs=1&qlt=90&o=6&dpr=1.3&pid=3.1&rm=2",
    "Parrot": "https://img.freepik.com/premium-photo/colorful-parrot-sitting-branch-forest_871710-24980.jpg",
    "Horse": "https://th.bing.com/th/id/OIP.Xw9TPYUwQnVXJEfK4CVm4AHaJQ?w=1384&h=1730&rs=1&pid=ImgDetMain"
}

st.title("🧠 Word-to-Image Prediction Game")
st.write("Match the word with the correct image!")

# Pick a random word as the question
if 'correct_word' not in st.session_state:
    st.session_state.correct_word = random.choice(list(image_dict.keys()))

# Show the word to the user
#st.subheader(f"🔤 Match the word: **{st.session_state.correct_word}**")

# Show all images with radio buttons
choices = list(image_dict.keys())
user_choice = st.radio("Which image matches the word?", choices, index=0)

st.image(image_dict[user_choice], caption=user_choice, use_container_width =True)

# Check answer
if st.button("Submit Guess"):
    if user_choice == st.session_state.correct_word:
        st.success("🎉 Correct! Well done.")
    else:
        st.error(f"❌ Nope! The correct answer was {st.session_state.correct_word}")
        st.image(image_dict[st.session_state.correct_word], caption="Correct Image", use_container_width =True)

# Play again
if st.button("Play Again"):
    for key in list(st.session_state.keys()):
        del st.session_state[key]  # Clear session state
    st.rerun()  # Force rerun



