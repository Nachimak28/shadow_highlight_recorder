import os
from PIL import Image
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from utils import shadow_highlight_correction

img_path = 'C:/Users/HP/Desktop/data_cleanup_DR/all_crop_images_v1_perfect_consensus_annotation_tool/4/dj_711.jpeg'
image = np.array(Image.open(img_path))


def control_ui():
    st.sidebar.markdown('Controls')

    shadow_amount = st.sidebar.slider("Shadow amount", 0.0, 1.0, 0.5, step=0.05)
    shadow_tone = st.sidebar.slider("Shadow Tone", 0.0, 1.0, 0.0, step=0.05)

    highlight_amount = st.sidebar.slider("Highlight amount", 0.0, 1.0, 0.5, step=0.05)
    highlight_tone = st.sidebar.slider("Highlight Tone", 0.0, 1.0, 0.0, step=0.05)

    return shadow_amount, shadow_tone, highlight_amount, highlight_tone


def display_image(image, shadow_amount, shadow_tone, highlight_amount, highlight_tone):
        modified_image = shadow_highlight_correction(img=image, 
                                                    shadow_amount_percent=shadow_amount,
                                                    shadow_tone_percent=shadow_tone,
                                                    shadow_radius=100,
                                                    highlight_amount_percent=highlight_amount,
                                                    highlight_tone_percent=highlight_tone,
                                                    highlight_radius=100,
                                                    color_percent=1
                                                    )
        
        col1, col2 = st.columns(2)
        with col1:
            st.write('Original Image')
            st.image(image, clamp=True, use_column_width=True)
        with col2:
            st.write('Modified Image')
            st.image(modified_image, clamp=True, use_column_width=True)


def show():

    shadow_amount, shadow_tone, highlight_amount, highlight_tone = control_ui()

    display_image(image=image, shadow_amount=shadow_amount, shadow_tone=shadow_tone, highlight_amount=highlight_amount, highlight_tone=highlight_tone)

    
if __name__ == "__main__":
    show()