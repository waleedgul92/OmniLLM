import requests
import streamlit as st
from dotenv import load_dotenv
import os

# Function to generate and display image
def generate__image_flux(query="Astronaut riding a horse", save_option=False):
    # Load API key from environment file
    load_dotenv("./keys.env")
    hugging_face_key = os.getenv('hugging_face_key')
    
    # API details
    API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev"
    headers = {"Authorization": f"Bearer {hugging_face_key}"}
    
    # Make the API request
    response = requests.post(API_URL, headers=headers, json={"inputs": query})
    return response