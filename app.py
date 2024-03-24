import streamlit as st
from dotenv import load_dotenv, find_dotenv
from transformers import pipeline

load_dotenv(find_dotenv())

def img_to_text(url):
    image_to_text_pipeline = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")
    
    text = image_to_text_pipeline(url)[0]["generated_text"]
    
    return text
    
def build_streamlit_app():
    st.title("Image to Text")
    st.write("This app uses the Salesforce/blip-image-captioning-base model to convert images to text.")
    
    url = st.text_input("Enter the URL of the image:")
    
    if st.button("Convert"):
        text = img_to_text(url)
        st.write(text)
        

def main():
    build_streamlit_app()


if __name__=='__main__':
    main()