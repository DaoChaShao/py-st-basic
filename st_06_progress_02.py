#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     : 2025/1/8 14:01
# @Author   : Shawn
# @Version  : Version 1.0
# @File     : st_06_progress_02.py
# @Desc     : streamlit run st_06_progress_02.py

from random import uniform
from streamlit import markdown, number_input, progress, empty, button, columns
from time import sleep


def main() -> None:
    """ Main Function """
    TITLE: str = "Welcome to the Progress Bar"
    markdown(f"<h1 style='text-align: center;'>{TITLE}</h1>", unsafe_allow_html=True)

    BAR_MIN: int = 0
    BAR_MAX: int = 100
    BAR_DEFAULT: int = 0
    input_num: int = number_input("Total", min_value=BAR_MIN, max_value=BAR_MAX, value=BAR_DEFAULT)

    empty_bar = empty()
    bar = progress(BAR_DEFAULT)

    empty_message = empty()

    col_left, col_mid, col_right = columns([1, 7, 1])
    with col_left:
        if button("Start"):
            if input_num == 0:
                empty_message.error("Please enter a number greater than 0.")
            else:
                empty_message.info(f"The number you entered is {input_num}.")
                for i in range(BAR_MIN, input_num + 1):
                    prog: float = i / input_num
                    bar.progress(prog)
                    sleep(round(uniform(0, 1), 1))
                    empty_bar.markdown(f"<p style='text-align: center;'>Loading {prog * 100} %</p>",
                                       unsafe_allow_html=True)
    with col_mid:
        pass
    with col_right:
        if button("Reset"):
            bar.progress(BAR_DEFAULT)
            empty_bar.empty()
            empty_message.success("The progress bar has been reset.")


if __name__ == "__main__":
    main()
