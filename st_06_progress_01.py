#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     : 2025/1/6 23:32
# @Author   : Shawn
# @Version  : Version 1.0
# @File     : st_06_progress_01.py
# @Desc     : streamlit run st_06_progress_01.py

from random import uniform
from streamlit import write, progress, markdown, empty
from time import sleep


def main() -> None:
    """ Main Function """
    TITLE: str = "Welcome to the Progress Bar"
    markdown(f"<h1 style='text-align: center;'>{TITLE}</h1>", unsafe_allow_html=True)

    BAR_START: int = 0
    BAR_END: int = 100
    bar = progress(BAR_START)

    empty_bar = empty()

    SEC_MIN: int = 0
    SEC_MAX: int = 1
    for i in range(BAR_START, BAR_END + 1):
        bar.progress(i)
        empty_bar.markdown(f"<p style='text-align: center;'>Loading {i} %</p>",
                           unsafe_allow_html=True)
        sleep(round(uniform(SEC_MIN, SEC_MAX), 1))


if __name__ == "__main__":
    main()
