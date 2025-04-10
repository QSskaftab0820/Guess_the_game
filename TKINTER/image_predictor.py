import streamlit as st
import random

st.title("🧠 Image Prediction Demo")
st.write("Choose an image and see if it's the correct one!")

# Sample images (replace these with your own URLs or paths)
images = {
    "Cat": "https://placekitten.com/200/200",
    "Dog": "https://placedog.net/200/200?id=1",
    "Parrot": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/Ara_ararauna_Luc_Viatour.jpg/200px-Ara_ararauna_Luc_Viatour.jpg",
    "Horse": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/Horse_in_Love_Valley%2C_Turkey.jpg/200px-Horse_in_Love_Valley%2C_Turkey.jpg"
}

# Randomly choose the correct answer
if 'correct_choice' not in st.session_state:
    st.session_state.correct_choice = random.choice(list(images.keys()))

# Show images with radio buttons
user_choice = st.radio("Which one do you think is the correct image?", list(images.keys()), index=0)

st.image(images[user_choice], caption=user_choice, use_column_width=True)

# Submit button
if st.button("Predict"):
    if user_choice == st.session_state.correct_choice:
        st.success(f"🎉 Correct! {user_choice} is the right image.")
    else:
        st.error(f"❌ Nope! The correct answer was {st.session_state.correct_choice}.")
        st.image(images[st.session_state.correct_choice], caption="Correct Image", use_column_width=True)

# Option to play again
if st.button("Try Another Round"):
    st.session_state.correct_choice = random.choice(list(images.keys()))
    st.experimental_rerun()
