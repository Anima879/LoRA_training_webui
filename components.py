import tkinter as tk
from tkinter import filedialog
from typing import Union

import streamlit as st


class DirPath:
    def __init__(self, name: str, tk_root: tk.Tk):
        self.tk_root = tk_root
        self.path = ""
        self.name = name

    def render(self, tk_root: Union[tk.Tk, None] = None) -> None:
        if tk_root is None:
            tk_root = self.tk_root

        col1, col2 = st.columns([4, 1])

        with col2:
            clicked = st.button(f'{self.name.capitalize()} path')
            if clicked:
                self.path = filedialog.askopenfile(master=tk_root).name

        with col1:
            self.path = st.text_input(f'Path to {self.name}...', self.path)