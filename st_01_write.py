#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     : 2025/1/6 16:32
# @Author   : Shawn
# @Version  : Version 1.0
# @File     : st_01_write.py
# @Desc     :
# - Before you use model streamlit, you should pip3 install streamlit initially.
# - Run this script with the command in a terminal: streamlit run st_01_write.py

from random import randint
from streamlit import title, write


def main() -> None:
    """ Main Function """
    title("Hello Streamlit!")

    write("This is a simple Streamlit app.")

    NUM_MIN: int = 1
    NUM_MAX: int = 10
    AMOUNT: int = 10
    NUMS: list[int] = [randint(NUM_MIN, NUM_MAX) for _ in range(AMOUNT)]
    write(f"Here are {AMOUNT} random numbers between {NUM_MIN} and {NUM_MAX}:")
    write(NUMS)


if __name__ == "__main__":
    main()
