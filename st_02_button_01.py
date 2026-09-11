#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     : 2025/1/6 16:43
# @Author   : Shawn
# @Version  : Version 1.0
# @File     : st_02_button_01.py
# @Desc     : streamlit run st_02_button_01.py

from random import choice
from streamlit import button, title, session_state, write


def main() -> None:
    """ Main Function """
    TITLES: list[str] = ["Hello Streamlit!", "Hello world!", "Hello Python!"]
    title("Hello Streamlit!")

    # Method 1:
    # if "clicked" not in session_state:
    #     session_state.clicked = 0

    # Method 2:
    session_state.clicked = session_state.get("clicked", 0)

    if button("Count"):
        session_state.clicked += 1
        write(f"You have clicked {session_state.clicked} times.")


if __name__ == "__main__":
    main()
