import streamlit as st
from PIL import Image
from dotenv import load_dotenv
from text_models import google_genai_text
from image_models import google_genai_image

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
## Custom CSS for spinner
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

# Input text box for user query
user_query = main_placeholder.text_input(
    "Question: ",
    placeholder="Type your question here for analyzing OR generating image",
    max_chars=1000, label_visibility="hidden"
)

# Create columns for action buttons
col1, col2, col3, col4 = st.columns([2.5, 2, 2.4, 3.7], vertical_alignment="center", gap="small")

with col2:
    analyze_button=st.button('Analyze Text', key='analyze_text', help='Click to analyze the text.')

with col3:
    st.button('Generate Image', key='generate_image', help='Click to generate an image.')

# Sidebar elements with titles and selectboxes
st.sidebar.title("Model for Text Analysis")
selected_text_model = st.sidebar.selectbox("Select a Text Model", ["Gemini-1.5-Flash", "Model 2"], 
                                               label_visibility="hidden")

st.sidebar.title("Model for QAs")
selected_qa_model = st.sidebar.selectbox("Select a QA Model", ["Gemini-1.5-Flash", "Model 2"], 
                                             label_visibility="hidden")

st.sidebar.title("Model for Generating Image")
selected_image_model = st.sidebar.selectbox("Select an Image Generation Model", ["Model 1", "Model 2"], 
                                                label_visibility="hidden")

st.sidebar.title("Upload a File")
uploaded_document = st.sidebar.file_uploader("Upload a PDF or Image File", type=["pdf", "txt", "jpeg", "png", "jpg"],
                                                  help="Upload a PDF or text file for analysis and an image for OCR.", label_visibility="hidden")


## Check if the user has clicked the analyze button and generate text bases on 
if user_query and analyze_button:
    if selected_text_model=="Gemini-1.5-Flash":
        loading_placeholder = st.empty()
        with st.spinner("Generating Response"):
            response=google_genai_text(user_query)
        # Display the response
            st.write("\n"*3)
            st.write(response)
    if selected_text_model=="Model 2":
        pass

if user_query and uploaded_document:
    if selected_qa_model=="Gemini-1.5-Flash":
        loading_placeholder = st.empty()
        with st.spinner("Generating Response"):
            response=google_genai_image(user_query)
        # Display the response
            st.write("\n"*3)
            st.write(response)
    if selected_qa_model=="Model 2":
        pass