import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Happy GF Day ❤️",
    page_icon="💖",
    layout="centered"
)

# Custom Aesthetic Styling (Pastel Soft Pink Theme)
st.markdown("""
    <style>
    .stApp { background-color: #FFF0F5; }
    h1, h2, h3 { color: #D87093 !important; text-align: center; }
    p, label { color: #4A4A4A; }
    div.stButton > button {
        background-color: #FFB6C1;
        color: #333333;
        border-radius: 20px;
        border: none;
        padding: 10px 24px;
        font-weight: bold;
        width: 100%;
    }
    div.stButton > button:hover {
        background-color: #FF69B4;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize Session State
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'choice' not in st.session_state:
    st.session_state.choice = None

# =========================================================
# SCREEN 1: PASSCODE LOCK
# =========================================================
if not st.session_state.authenticated:
    st.title("🔒 Top Secret Message")
    st.write("### Enter the passcode to unlock your surprise")
    
    passcode = st.text_input("Passcode (Hint: 0801)", type="password")
    
    if st.button("Unlock 💖"):
        if passcode == "0801":  # Change "0801" to your passcode
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("Incorrect passcode! Hint: 0801")

# =========================================================
# SCREEN 2: PLAYFUL QUESTION (YES / NO)
# =========================================================
elif st.session_state.choice is None:
    st.title("Hey Cutie! 🥰")
    st.write("### I made something special for you. Do you wanna see it?")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Yes! 😍"):
            st.session_state.choice = "yes"
            st.rerun()
    with col2:
        if st.button("No 😜"):
            st.session_state.choice = "no"
            st.rerun()

# =========================================================
# SCREEN 3A: IF SHE CLICKS "NO"
# =========================================================
elif st.session_state.choice == "no":
    st.title("SERIOUSLY?! 😤")
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcDdtNDNwZm9hOTJhcWJyeXhndjRzYXkxdmxicXZlYXc4NWNscDZ3dCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/L95W4wv8nnb9K/giphy.gif")
    st.write("### How dare you pick No! Try again...")
    if st.button("Go Back 🥺"):
        st.session_state.choice = None
        st.rerun()

# =========================================================
# SCREEN 3B: MAIN SCRAPBOOK HUB
# =========================================================
elif st.session_state.choice == "yes":
    st.balloons()
    st.title("Happy Girlfriend Day! 🎉❤️")
    st.write("---")

    tab1, tab2, tab3 = st.tabs(["✨ Cutest Face", "✉️ Love Letter", "🎵 Special Song"])

    # TAB 1: HER PHOTO
    with tab1:
        st.subheader("The Most Beautiful Face I've Ever Seen 😍")
        st.write("Look at you! Just perfection. ✨")
        
        # Paste your uploaded image URL inside the quotes below!
        st.image("https://i.postimg.cc/J4QxDxXY/IMG-20260728-194252-545.jpg", caption="My favorite view ❤️", use_container_width=True)

    # TAB 2: ENGLISH TRANSLATED LETTER
    with tab2:
        st.subheader("A Little Note For You 💌")
        st.info("""
        **To the cutest person ever,**

        Thank you for everything—for making my life so much better and for loving me so deeply. I like you so much that sometimes I can't even find the words to express it properly. 
        
        On top of all that, you're just so cute! Everything you talk about and all the little things you do are so incredibly adorable. Honestly, nobody else's opinions or actions matter to me anywhere near as much as yours do. 

        I know how hard it is to convince you when you get upset with me—you really hold your ground! But whenever we're finally face-to-face, I'm just going to steal a kiss to make it all up to you, haha 😝. 

        I love you so much 💘.

        **Happy Girlfriend Day! 😋🤎**
        """)

    # TAB 3: SONG (Baihja Mera Kol)
    with tab3:
        st.subheader("Baihja Mera Kol Tenu Takda Raha 🎧")
        st.write("Press play below 👇")
        # Direct video link for "Baihja Mera Kol"
        st.video("https://www.youtube.com/watch?v=A8f9u8p9gI4")
        st.success("You can count on me, today and always! ✨")
