import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold
from dotenv import load_dotenv
import os

def google_genai_image(img_path,prompt:str="give me letters in image?"):
    ## Load the google api key
    env_keys=load_dotenv("./keys.env")
    google_env_key=os.getenv('GOOGLE_API_KEY')
        ## Configure the generation config
    generation_config = genai.GenerationConfig(
            max_output_tokens=1000, temperature=0.1
    )
        ## Configure the safety settings
    safety_settings={
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE
    }
    ## Configure the google api
    genai.configure(api_key=google_env_key)

    uploaded_image = genai.upload_file(img_path)
    ## Load the model
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    ## Generate the content
    response=model.generate_content([uploaded_image,"\n\n",prompt],generation_config=generation_config,safety_settings=safety_settings)    
    return response.text

