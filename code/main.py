import streamlit as st
from PIL import Image

# Set page layout to wide for better appearance
st.set_page_config(layout="wide")

# Custom CSS for rounded corners and modern look
st.markdown("""
    <style>
    .stTextInput, .stButton, .stTextArea, .stFileUploader {
        border-radius: 20px;
    }
    
    .stTextInput > div > input {
        border-radius: 20px !important;
        padding: 10px !important;
    }

    .stButton > button {
        background-color: #444;
        border-radius: 20px;
        color: white;
        padding: 10px 20px;
        margin-left: 40px;  /* Adjust margin for spacing between buttons */
        margin-top: 30px;   /* Adjust margin for vertical spacing */
    }

    .stButton > button:hover {
        background-color: #555;
    }

    .stTextArea textarea {
        border-radius: 20px !important;
        padding: 10px !important;
    }

    /* Centering the text area and buttons */
    .block-container {
        display: flex;
        justify-content: center;
        padding-top: 30px;
        padding-left: 50px;
        padding-right: 50px;
        padding-bottom: 30px;
    }
    
    /* Optional: Center the title */
    .stMarkdown h1 {
        text-align: center;
    }

    /* Making buttons display inline */
    .stButton {
        display: inline-flex; 
        justify-content: flex-start; 
    }
    </style>
    """, unsafe_allow_html=True)

# Add a title with the new app name
st.title("Omni GPT")

# Create a layout for the text area and buttons
col1, col2 = st.columns([7, 1])  # Adjusted columns for a wider text area

with col1:
    # Text input section
    text_input = st.text_area("Enter your text here:", placeholder="Type your text here for query or image generation")

with col2:
    # Buttons in the same column
    col2_button1, col2_button2 = st.columns([1, 1])  # Create sub-columns for horizontal buttons
    with col2_button1:
        if st.button("Generate Answer"):
            pass
    
    with col2_button2:
        if st.button("Generate Image"):
            pass