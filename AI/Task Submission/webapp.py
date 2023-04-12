import streamlit as st
import numpy as np
from PIL import Image
import cv2
import tempfile
import os

# Define the app layout
st.title("Image and Video Captioning App")
menu = ["Image", "Video"]
choice = st.sidebar.selectbox("Select an option", menu)

# Define the capture mode
mode = st.sidebar.radio("Select capture mode", ["Local file", "Camera"])

tfile = None  # initialize tfile variable to None

# Define the file upload option
if mode == "Local file":
    file = st.file_uploader("Upload file", type=[choice.lower(), "mp4", "avi"])
    if file is not None:
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(file.read())

# Define the camera capture option
else:
    cap = cv2.VideoCapture(0)
    if st.button("Capture"):
        # Capture the frame
        ret, img = cap.read()
        # Save the frame to a temporary file
        tfile = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")
        cv2.imwrite(tfile.name, cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    cap.release()

# Define the caption input
caption = st.text_input("Enter a caption")

# Display the image/video with caption
if tfile is not None:
    st.write(f"**{caption}**")
    if choice == "Image":
        img = Image.open(tfile.name)
        st.image(img)
    else:
        st.video(tfile.name)


st.title("Image Upload")

# Display file upload widget
uploaded_file = st.file_uploader("Choose an image...", type="jpg")

# Display caption input box
caption = st.text_input('Enter a caption for the image (optional):')

# If a file was uploaded
if uploaded_file is not None:
    # Read the file contents
    image = Image.open(uploaded_file)
    st.image(image, caption=caption, use_column_width=True)
    img_array = np.array(image)
    
    # Write the file to a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as tfile:
        tfile.write(img_array)
        st.write('Image saved to:', tfile.name)
    
    # Close the file and delete 
    os.unlink(tfile.name)
 
