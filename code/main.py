import streamlit as st
from PIL import Image
from dotenv import load_dotenv
from text_models import google_genai_text, gpt2_text
from image_models import google_genai_image
from image_generation_models import generate__image_flux
from tmp_folder import use_tmp_folder
import tempfile
import os
import io
from PIL import Image, ImageDraw, ImageFont

# Configure the Streamlit page
st.set_page_config("Omni LLM", initial_sidebar_state="collapsed")

# Custom CSS for animations and styling
st.markdown(
    """
    <style>
    @keyframes fadeIn {
        0% { opacity: 0; transform: translateX(-20px); }
        100% { opacity: 1; transform: translateX(0); }
    }

    .welcome-message {
        font-size: 48px; /* Adjust font size */
        text-align: center;
        color: white; /* Text color */
        animation: fadeIn 2.0s ease forwards; /* Apply animation */
        margin-top: 50px; /* Space above the message */
    }

    .stTextInput > div > input {
        height: 100%;  /* Adjust height */
        width: 100%;   /* Adjust width */
        font-size: 14px;  /* Adjust font size */
    }

    div[data-testid="column"] {
        width: fit-content !important;
        flex: unset;
        padding-left: 20px;  /* Left padding */
    }

    div[data-testid="column"] * {
        width: fit-content !important;
        vertical-align: left;  /* Align items to the left */
    }

    /* Styling the file uploader to match button styles */
    .stFileUploader {
        width: 100%;  /* Make the file uploader full width */
        border-radius: 5px;  /* Rounded corners */
        text-align: center;  /* Center text */
    }

    [data-testid='stFileUploader'] section {
        padding: 0;
        float: left;
    }

    [data-testid='stFileUploader'] section > input + div {
        display: none;  /* Hide the default uploader text */
    }

    /* Animation for sidebar items */
    .sidebar .stSelectbox, 
    .sidebar .stButton, 
    .sidebar .stFileUploader {
        animation: fadeIn 1s ease forwards; /* Apply animation to sidebar elements */
    }

    .sidebar {
        animation: fadeIn 1s ease forwards; /* Apply animation to sidebar itself */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display the animated welcome message
st.markdown("<div class='welcome-message'>Welcome to Omni GPT!</div>", unsafe_allow_html=True)

# Custom CSS for spinner
st.markdown("""
  <style>
  div.stSpinner {
    text-align:center;
    align-items: center;
    justify-content: center;
  }
  </style>""", unsafe_allow_html=True)

# Placeholder for main content
main_placeholder = st.empty()

# Input text box for user query with selected model display
col_input, col_model = st.columns([3, 1])

with col_input:
    user_query = main_placeholder.text_input(
        "Question: ",
        placeholder="Type your question here for analyzing OR generating image",
        max_chars=1000, label_visibility="hidden"
    )

# Create columns for action buttons
col1, col2, col3, col4 = st.columns([2.5, 2, 2.4, 3.7], vertical_alignment="center", gap="small")

with col2:
    analyze_button = st.button('Analyze Text', key='analyze_text', help='Click to analyze the text.')

with col3:
    generate_image_button=st.button('Generate Image', key='generate_image', help='Click to generate an image.')

# Sidebar elements with titles and selectboxes
st.sidebar.title("Model for Text Analysis")
selected_text_model = st.sidebar.selectbox("Select a Text Model", ["Gemini-1.5", "Gpt-2"], label_visibility="hidden")

st.sidebar.title("Model for QAs")
selected_qa_model = st.sidebar.selectbox("Select a QA Model", ["Model 1", "Model 2"], label_visibility="hidden")

st.sidebar.title("Model for Generating Image")
selected_image_model = st.sidebar.selectbox("Select an Image Generation Model", ["FLUX.1", "Model 2"], 
                                                label_visibility="hidden")

st.sidebar.title("Upload a File")
uploaded_document = st.sidebar.file_uploader("Upload a Pdf or Text file", type=["pdf", "txt"],
                                                  help="Upload a PDF or text file for analysis ", label_visibility="hidden" )

st.sidebar.title("Upload an image")
uploaded_image = st.sidebar.file_uploader("Upload an Image File", type=["jpg", "jpeg", "png"],
                                                  help="Upload an image for analysis ", label_visibility="hidden")


with col_model:
    st.markdown(f"<div style='color:gray; font-size:14px text-align: right;'  > Text Model: {selected_text_model}</div>", unsafe_allow_html=True)
st.markdown("""
  <style>
    .css-13sdm1b.e16nr0p33 {
      margin-top: -75px;
    }
  </style>
""", unsafe_allow_html=True)


# Generate and display image if button is clicked
if user_query and generate_image_button:
    with col_model:
        st.markdown(f"<div style='color:gray; font-size:14px text-align: right;'  > Image Model: {selected_image_model}</div>", unsafe_allow_html=True)
        st.markdown("""
        <style>
            .css-13sdm1b.e16nr0p33 {
            margin-top: -75px;
            }
        </style>
    """, unsafe_allow_html=True)
    if selected_image_model == "FLUX.1":
        with st.spinner("Generating Image..."):
            response = generate__image_flux(user_query)

        if response.status_code == 200:
            image_bytes = response.content
            stream = io.BytesIO(image_bytes)
            img = Image.open(stream)
            
            # Add optional text to the image
            draw = ImageDraw.Draw(img)
            font = ImageFont.load_default()
            draw.text((7, 7), "Generated Image", (255, 255, 255), font=font)
            
            # Display the image in Streamlit
            st.image(img, caption="Generated Image", use_column_width=True)

            # Option to save image after generation
        else:
            st.error(f"Error: {response.status_code}")

# Analyze text button logic (if needed)
if user_query and analyze_button:
    if selected_text_model == "Gemini-1.5":
        with st.spinner("Generating Response..."):
            response = google_genai_text(user_query)
        st.write(response)
    elif selected_text_model == "Gpt-2":
        with st.spinner("Generating Response..."):
            response = google_genai_text(user_query)
        st.write(response)
