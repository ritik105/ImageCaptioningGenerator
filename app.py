import streamlit as st
from PIL import Image
import requests
import io

# Define API URL and headers
API_URL = "https://api-inference.huggingface.co/models/moranyanuka/blip-image-captioning-large-mocha"
API_TOKEN = "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"  # Replace with your actual Hugging Face API token
headers = {"Authorization": f"Bearer {API_TOKEN}"}

# Function to query the model API with an image file
def query(uploaded_file):
    try:
        with io.BytesIO(uploaded_file.read()) as f:
            data = f.read()
        response = requests.post(API_URL, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for non-2xx status codes
        return response.json()
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return []

# Streamlit app
st.title("Image Captioning with Hugging Face Model")
st.markdown("Upload an image, and this app will generate captions for it using the Hugging Face image captioning model.")

# Upload image
uploaded_image = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

# Process uploaded image and generate captions
if uploaded_image is not None:
    st.subheader("Uploaded Image")
    st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)

    # Generate captions
    with st.spinner("Generating captions..."):
        captions = query(uploaded_image)

    st.subheader("Generated Captions:")
    if captions:
        for i, caption in enumerate(captions):
            st.write(f"Caption {i+1}: {caption}")
    else:
        st.warning("No captions generated.")
