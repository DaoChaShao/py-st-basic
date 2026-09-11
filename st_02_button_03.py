#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     : 2025/1/8 02:25
# @Author   : Shawn
# @Version  : Version 1.0
# @File     : st_02_button_03.py
# @Desc     : streamlit run st_02_button_03.py

from random import choice
from streamlit import button, empty, columns


def main() -> None:
    """ Main Function """
    TITLES: list[str] = ["Nice Streamlit!", "Hello world!", "Good Python!"]

    empty_title = empty()
    empty_title.title("")

    col_left, col_right = columns(2)
    with col_left:
        if button("Count"):
            empty_title.title(choice(TITLES))

    with col_right:
        if button("Clear"):
            empty_title.title("")


if __name__ == "__main__":
    main()
