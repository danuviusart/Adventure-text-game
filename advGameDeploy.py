import streamlit as st

# Initialize session state
if "step" not in st.session_state:
    st.session_state.step = "intro"
if "choice1" not in st.session_state:
    st.session_state.choice1 = ""
if "game_over" not in st.session_state:
    st.session_state.game_over = False

def reset_game():
    st.session_state.step = "intro"
    st.session_state.choice1 = ""
    st.session_state.game_over = False

# Intro
if st.session_state.step == "intro":
    st.write("""
    You are Alex, a famous tour guide in the ancient city of Solaria.  
    One day, a mysterious map is left at your desk, promising a hidden treasure in the old ruins.  
    Curiosity piqued, you decide to follow it.
    """)
    st.session_state.step = "main_choice"

# Main choices
if st.session_state.step == "main_choice" and not st.session_state.game_over:
    choice = st.radio(
        "Your choices:",
        ["Take the map and head straight to the ruins.",
         "Ask a colleague for advice about the map first.",
         "Ignore the map and continue your regular tour."]
    )
    if st.button("Submit Choice"):
        if choice.startswith("Take the map"):
            st.session_state.choice1 = "1"
            st.session_state.step = "ruins"
        elif choice.startswith("Ask a colleague"):
            st.session_state.choice1 = "2"
            st.session_state.step = "colleague"
        else:
            st.session_state.choice1 = "3"
            st.session_state.step = "routine"

# Ruins
if st.session_state.step == "ruins" and not st.session_state.game_over:
    st.write("""
    You arrive at the ruins and see two paths inside the main chamber:
    1. A narrow dark tunnel.
    2. A stone staircase leading up.
    """)
    choice = st.radio("Choose a path:", ["Narrow dark tunnel", "Stone staircase"])
    if st.button("Go"):
        if choice.startswith("Narrow"):
            st.write("Tunnel leads to a small treasure chest, but a trap triggers! You barely escape with a small gem.")
            st.session_state.game_over = True
        else:
            st.write("You climb to a golden chamber full of coins and artifacts!")
            st.session_state.game_over = True

# Colleague
if st.session_state.step == "colleague" and not st.session_state.game_over:
    st.write("""
    Your colleague warns it might be a trap. You now have two options:
    1. Follow the map carefully but slowly.
    2. Go back home and research the ruins before trying.
    """)
    choice = st.radio("What do you do?", ["Follow carefully", "Go back home"])
    if st.button("Proceed"):
        if choice.startswith("Follow"):
            st.write("You avoid traps but only find some old scrolls.")
            st.session_state.game_over = True
        else:
            st.write("You discover the treasure’s location precisely, ready for next day. Push Proceed")
            st.session_state.step = "ruins"

# Routine
if st.session_state.step == "routine" and not st.session_state.game_over:
    st.write("""
    You continue your normal tour. Afterward, a local asks if you heard about the “hidden treasure.”  
    1. Decide to chase the treasure now.
    2. Politely refuse and stick to your routine.
    """)
    choice = st.radio("What do you do?", ["Chase the treasure", "Stick to routine"])
    if st.button("Proceed"):
        if choice.startswith("Chase"):
            st.write("Ruins are more dangerous at night. Push Proceed")
            st.session_state.step = "ruins"
        else:
            st.write("Life goes on as usual, treasure missed.")
            st.session_state.game_over = True

# Replay button
if st.session_state.game_over:
    if st.button("Play Again"):
        reset_game()
