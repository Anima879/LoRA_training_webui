import streamlit as st
from components import DirPath
import tkinter as tk


def render_config(tk_root: tk.Tk):
    base_model_path = DirPath("base model", tk_root)
    image_dir_path = DirPath("image dir", tk_root)
    output_dir_path = DirPath("output dir", tk_root)

    base_model_path.render()
    image_dir_path.render()
    output_dir_path.render()

    output_name = st.checkbox("Do you want to change the name of output checkpoints?")
    tags = st.checkbox("Do you want to save a txt file that contains a list\nof all tags that you have used in "
                       "your training data?")
    v2 = st.checkbox("Are you training on a SD2.x base model?")
    if v2:
        st.checkbox("Are you training on a model based on the 768x version of SD2?")
    realistic_model = st.checkbox("Are you training on a realistic model?")
    reg_img_folder = st.checkbox("Do you want to use regularization images?")
    st.selectbox(
        "Optimizer",
        ["AdamW", "AdamW8bit", "Lion", "SGDNesterov", "SGDNesterov8bit", "DAdaptation", "AdaFactor"],
        index=1
    )

    st.number_input("Dim size", min_value=1, value=32, step=1)
    st.slider("Alpha", min_value=0.0, max_value=1.0, value=0.5, step=0.01)

    model_type = st.selectbox("Type of model", ['LoRA', 'LoCon', 'LoHa'])

    scheduler = st.selectbox(
        "Scheduler",
        ["cosine_with_restarts", "cosine", "polynomial", "constant", "constant_with_warmup", "linear"]
    )

    st.number_input("Width resolution", min_value=1, value=256, step=1)
    st.number_input("Height resolution", min_value=1, value=256, step=1)
    st.number_input("Batch size", min_value=1, value=32, step=1)

    save_epochs = st.checkbox("Save epochs as it trains")
    if save_epochs:
        st.number_input("Save every", min_value=1, value=1, step=1)

    st.selectbox("Which way do you want to manage steps?", ["Epochs", "Steps"])

    warmup_ratio = st.checkbox("Warmup ratio")
    if warmup_ratio:
        st.number_input("Warmup ratio", min_value=0.0, max_value=1.0, value=0.01, step=0.01)

    st.checkbox("Shuffle captions")
    keep_tokens = st.checkbox("Keep som tokens at the front of the caption")
    if keep_tokens:
        number_tokens = st.number_input("Keep tokens", min_value=0, value=1, step=1)

    st.selectbox("Elements to train", ["both", "unet_only", "text_only"])

    st.checkbox("Flip images (reduce biases)")
    st.text_input("Comment for the metadata")
    st.checkbox("Prevent upscaling images")
    st.selectbox("Precision", ["float", "fp16", "bf16"])

    st.selectbox("Random crop or cache latents", ["random_crop", "cache_latents"])

    snr_gamma = st.checkbox("Use min snr gamma training")
    if snr_gamma:
        st.number_input("Min snr gamma", min_value=0.0, value=5, step=0.1)

    st.checkbox("Generate test images during training")
    # TODO

    st.button("Save configuration")
