import streamlit as st
from PIL import Image

# Custom CSS for the animation and button styles
st.markdown(
    """
    <style>
    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(-20px); }
        100% { opacity: 1; transform: translateY(0); }
    }

    .welcome-message {
        font-size: 48px; /* Adjust font size */
        text-align: center;
        color: white; /* Text color */
        animation: fadeIn 2.0s ease forwards; /* Apply animation */
        margin-top: 50px; /* Space above the message */
    }

    .stTextInput>div>input {
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
    </style>
    """,
    unsafe_allow_html=True
)

# Initialize session state for file upload tracking
if "uploaded_file" not in st.session_state:
    st.session_state["uploaded_file"] = None

# Function to handle file upload
def upload_file():
    # Automatically open the file explorer
    st.markdown("<script>document.querySelector('input[type=file]').click();</script>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Upload a Document for QA", type=["pdf", "txt", "jpg", "png", "jpeg"], label_visibility="hidden", help='Upload a document for question answering and Image for extraction.')

    # Save the uploaded file to session state
    if uploaded_file is not None:
        st.session_state["uploaded_file"] = uploaded_file

# Display the animated welcome message
st.markdown("<div class='welcome-message'>Welcome to Omni GPT!</div>", unsafe_allow_html=True)

main_placeholder = st.empty()

# Input text box
query = main_placeholder.text_input(
    "Question: ",
    placeholder="Type your question here for analyzing OR generating image",
    max_chars=1000
)

# Create columns for buttons
col1, col2, col3, col4 = st.columns([2.5, 2, 2.4, 3.7], vertical_alignment="center", gap="small")

with col2:
    st.button('Analyze Text', key='analyze_text', help='Click to analyze the text.')

with col3:
    st.button('Generate Image', key='generate_image', help='Click to generate an image.')



# Add a checkbox for toggling the sidebar
model_selected_qa=model_selected_text=model_selected_image=None
document=None
show_sidebar = st.checkbox("Show Sidebar")

if show_sidebar:
    # Sidebar content (will be hidden until the checkbox is checked)
    st.sidebar.title("Model for Text Analysis")
    model_selected_text = st.sidebar.selectbox("Select a text Model", ["Model 1", "Model 2"],label_visibility="hidden")

    st.sidebar.title("Model for QAs")
    model_selected_qa = st.sidebar.selectbox("Select a QA Model", ["Model 1", "Model 2"],label_visibility="hidden")

    st.sidebar.title("Model for Generating Image")
    model_selected_image = st.sidebar.selectbox("Select a Generating Image Model", ["Model 1", "Model 2"],label_visibility="hidden")

    st.sidebar.title("Upload a file")
    document = st.sidebar.file_uploader("Upload a PDF file", type=["pdf","txt","jpeg","png","jpg"], help="Upload a pdf or text file for analyzing and image for OCR", label_visibility="hidden")	