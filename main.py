import json
import tkinter as tk

import streamlit as st

from components import DirPath
from config_component import render_config


def main():
    root = tk.Tk()
    root.withdraw()
    root.wm_attributes('-topmost', 1)

    st.title("LoRA training webui")

    multiple_trainings = st.checkbox("Run multiple trainings", key="multiple_trainings")

    if multiple_trainings:
        DirPath("Configs directory", root).render()
        st.button("Start")
        # TODO : skip
    else:
        config_file = st.file_uploader("Config file", type="json")
        if not config_file:
            render_config(root)
        else:
            config_dict = json.load(config_file)
            render_config(root, config_dict)

    st.button("Train")


if __name__ == '__main__':
    main()
