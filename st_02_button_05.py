#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     : 2025/1/8 02:41
# @Author   : Shawn
# @Version  : Version 1.0
# @File     : st_02_button_05.py
# @Desc     : streamlit run st_02_button_05.py

from random import choice
from streamlit import button, empty, columns, info, warning


def click_title(empty_title: empty, empty_message: empty, content: str) -> None:
    """ Click the button to change the title """
    empty_title.markdown(f"<h1 style='text-align: center;'>{content}</h1>",
                         unsafe_allow_html=True)
    match content:
        case "":
            empty_message.success("The title is cleared.")
        case _:
            empty_message.warning(f"The title is changed to {content}.")


def main() -> None:
    """ Main Function """
    TITLES: list[str] = ["Nice Streamlit!", "Hello world!", "Good Python!"]
    TITLE_DEFAULT: str = ""
    option: str = choice(TITLES)

    empty_title = empty()
    empty_title.markdown(f"<h1 style='text-align: center;'>{TITLE_DEFAULT}</h1>",
                         unsafe_allow_html=True)

    empty_message = empty()

    col_left, col_mid, col_right = columns([1, 7, 1])
    with col_left:
        if button("Click"):
            click_title(empty_title, empty_message, option)
    with col_mid:
        pass
    with col_right:
        if button("Clear"):
            click_title(empty_title, empty_message, TITLE_DEFAULT)


if __name__ == "__main__":
    main()
