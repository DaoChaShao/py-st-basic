#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/1/15 00:42
# @Author   :   Shawn
# @Version  :   Version 1.0
# @File     :   st_11_icon.py
# @Desc     :   streamlit run st_11_icon.py
# - https://fonts.google.com/icons

from random import randint
from streamlit import logo, title, divider, expander, caption, sidebar, header, markdown


def main() -> None:
    """ Main Function """
    logo("data/logo_streamlit.png") if randint(0, 1) else logo("data/logo_ollama.png")
    title("Streamlit Icon")
    divider()
    with expander("Icon Example"):
        caption("This is an icon example")

    with sidebar:
        header("Settings")
        markdown("""
            <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
            <i class="material-icons">home</i>
        """, unsafe_allow_html=True)

        markdown(":material/logout: This is a thumbs up icon!")
        markdown(":material/account_balance: This is a thumbs up icon!")


if __name__ == "__main__":
    main()
