#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/1/10 20:42
# @Author   :   Shawn
# @Version  :   Version 1.0
# @File     :   st_12_stqdm.py
# @Desc     :   streamlit run st_12_stqdm.py

from stqdm import stqdm
from time import sleep
from streamlit import empty, sidebar, container


def bar():
    for _ in stqdm(range(10), desc="outer", mininterval=1):
        for _ in stqdm(range(10), desc="inner", mininterval=1):
            sleep(0.5)


def main() -> None:
    """ Main Function """
    # with sidebar:
    #     empty_outer_text = empty()
    #     empty_outer_bar = empty()
    #     empty_inner_text = empty()
    #     empty_inner_bar = empty()
    #
    # amount = 10
    # for i in stqdm(range(amount), st_container=empty_outer_bar):
    #     empty_outer_text.markdown(f"<p style='text-align: center;'>Loading {i}/{amount}</p>",
    #                               unsafe_allow_html=True)
    #     for j in stqdm(range(10), st_container=empty_inner_bar, desc="Inner:"):
    #         empty_inner_text.markdown(f"<p style='text-align: center;'>Loading {j}/{amount}</p>",
    #                                   unsafe_allow_html=True)
    #         sleep(0.3)

    with sidebar:
        bar()


if __name__ == "__main__":
    main()
