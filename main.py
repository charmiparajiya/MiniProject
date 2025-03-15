import streamlit as st
from transformers import pipeline
import pyautogui
import time
import random

# Why Streamlit? It’s fast, simple, and great for beginners to build interactive apps like this playlist curator.
pyautogui.FAILSAFE = True
classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# Default background color
st.markdown(
    """
    <style>
    .stApp {
        background-color: #F8F1E9;  /* Warm off-white */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Elegant heading in a div with matching color
st.markdown(
    """
    <div style='text-align: center; background-color: #9E7B9B; 
                padding: 20px; border-radius: 15px; box-shadow: 2px 2px 8px #888888; margin-bottom: 20px;'>
        <h1 style='color: #FFFFFF; font-family: Arial; margin: 0;'>Mood-Based Playlist Weaver</h1>
    </div>
    """,
    unsafe_allow_html=True
)
st.write("**Welcome! Tell me how you feel, and I’ll suggest the perfect tunes to match your mood.**")
st.write("**How it works:** I use a smart model to guess if your mood is calm or energetic based on what you type.")

# Initialize session state
if "playlist" not in st.session_state:
    st.session_state.playlist = None
if "automation_run" not in st.session_state:
    st.session_state.automation_run = False

st.write("**Enter your mood below** (e.g., 'I’m tired' or 'I’m excited'):")
mood_input = st.text_input("How do you feel today?")

st.write("**Click to get your playlist** based on your mood:")
if st.button("Suggest Playlist"):
    if mood_input:
        result = classifier(mood_input)[0]
        mood = "Calm" if result["label"] == "NEGATIVE" else "Energetic"
        st.session_state.playlist = "Moonlight Sonata" if mood == "Calm" else "Sweet Caroline"
        st.session_state.automation_run = False
        # Cohesive background colors
        color = "#D8E2DC" if mood == "Calm" else "#FFE5D9"  # Soft gray-blue or peach blush
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-color: {color};
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
        # Random DJ persona
        # djs = ["DJ Chillax", "DJ PartyVibe", "DJ Soulful"]
        # messages = {
        #     "Calm": "Relax with this chill tune!",
        #     "Energetic": "Get pumped with this banger!"
        # }
        # dj = random.choice(djs)
        # message = messages[mood]
        # st.write(f"{dj} says: '{message}'")
        # Elegant Vibe Card
        vibe = "Quiet Night" if mood == "Calm" else "Party Time"
        st.markdown(
            f"""
            <div style='border: 2px solid #8A817C; border-radius: 10px; padding: 15px; 
                        background-color: #FFFFFF; box-shadow: 2px 2px 6px #888888; 
                        width: 350px; text-align: center; margin: 20px auto;'>
                <h3 style='color: #4A4A4A; margin: 0 0 10px 0;'>Your Vibe Card</h3>
                <p style='font-size: 16px; margin: 5px 0;'><b>Mood:</b> {mood}</p>
                <p style='font-size: 16px; margin: 5px 0;'><b>Playlist:</b> {st.session_state.playlist}</p>
                <p style='font-size: 16px; margin: 5px 0;'><b>Vibe:</b> {vibe}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.write("Please type how you feel first!")

st.write("**Click to play the playlist** (opens your music player):")
st.write("**Note:** This will take over your mouse/keyboard for a few seconds. Don’t move your mouse!")
if st.button("Play playlist") and not st.session_state.automation_run:
    if st.session_state.playlist:
        st.write("Opening music player and queuing your song...")
        pyautogui.hotkey("win", "r")
        time.sleep(2)
        pyautogui.typewrite("wmplayer", interval=0.2)
        pyautogui.press("enter")
        time.sleep(5)
        pyautogui.hotkey("alt", "space")
        time.sleep(0.5)
        pyautogui.press("x")
        time.sleep(1)
        pyautogui.click(x=1600, y=85)  # Your coordinates
        time.sleep(1)
        pyautogui.typewrite(st.session_state.playlist, interval=0.2)
        st.write(f"Song '{st.session_state.playlist}' queued in your music player!")
        st.session_state.automation_run = True
    else:
        st.write("Please curate a playlist first!")