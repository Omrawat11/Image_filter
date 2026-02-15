
import streamlit as st
from PIL import Image, ImageFilter, ImageEnhance
import io

#-------------PAGE CONFIG-----------------
st.set_page_config(
    page_title="Advanced Image Filter App",
    page_icon="🖼️",
    layout = "wide"
)

st.title("🖼️Advance Image Filter Application")
st.write("Upload an imahe and apply different filters with adjustable control.")

#----------FILE UPLOADER--------------
file = st.file_uploader("Select an Image", type=["png","jpg","jpeg"])

if file:
    original_img = Image.open(file)

    #-----------SIDEBAR CONTROL-----------
    st.sidebar.header("🎛️ Filter Controls")

    filter_option = st.sidebar.selectbox(
        "Choose Filter",
        ["None", "GrayScale", "Blur", "Emboss", "Contour", "Sharpen", "Edge Enhance"]
    )
    brightness =  st.sidebar.slider("Brightness", 0.5, 2.0, 1.0)
    contast = st.sidebar.slider("Contrast", 0.5, 2.0, 1.0)

    #work on copy of original 
    img = original_img.copy()

    #--------------- APPLY FILTER-------------------
    with st.spinner("Applying filter...."):

        if filter_option == "GrayScale":
            img = img.convert("L")

        elif filter_option == "Blur":
            blur_intensity = st.sidebar.slider("Blur Intensity", 1,10,2)
            img = img.filter(ImageFilter.GaussianBlur(blur_intensity))

        elif filter_option == "Emboss":
            img = img.filter(ImageFilter.EMBOSS)

        elif filter_option == "Comtour":
            img = img.filter(ImageFilter.CONTOUR)

        elif filter_option == "Sharpen":
            img = img.filter(ImageFilter.SHARPEN)

        elif filter_option == "Edge Enhance":
            img = img.filter(ImageFilter.EDGE_ENHANCE)

        #Apply Brightness 
        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(brightness)

        #Apply Contrast
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(contast)

    #----------------DISPLAY NAME---------------
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Original Image")
        st.image(original_img, use_container_width=True)

    with col2:
        st.subheader("Filtered Image")
        st.image(img, use_container_width = True)

    #-----------------IMAGE DETAILS---------------
    st.markdown("## 📋 Image Details")
    st.write("Format:", original_img.format)
    st.write("Size:", original_img.size)
    st.write("Mode:", original_img.mode)

    #-----------------DOWNLOAD BUTTON-------------
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    st.download_button(
        "⬇️ Download Filtered Image",
        data=buffer,
        file_name = "filtered_image.png",
        mime="image/png"
    )
else:
    st.info("Please upload an image to begin.")
