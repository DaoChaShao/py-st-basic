#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     : 2025/1/8 02:30
# @Author   : Shawn
# @Version  : Version 1.0
# @File     : st_02_button_04.py
# @Desc     : streamlit run st_02_button_04.py

from random import choice
from streamlit import button, empty, columns


def click_title(empty_component: empty, content: str) -> None:
    """ Click the button to change the title """
    empty_component.title(content)


def main() -> None:
    """ Main Function """
    TITLES: list[str] = ["Nice Streamlit!", "Hello world!", "Good Python!"]
    TITLE_DEFAULT: str = ""

    empty_title = empty()
    empty_title.title(TITLE_DEFAULT)

    col_left, col_right = columns(2)
    with col_left:
        if button("Click"):
            click_title(empty_title, choice(TITLES))

    with col_right:
        if button("Clear"):
            click_title(empty_title, TITLE_DEFAULT)


if __name__ == "__main__":
    main()
