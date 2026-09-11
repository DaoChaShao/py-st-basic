#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     : 2025/1/7 15:24
# @Author   : Shawn
# @Version  : Version 1.0
# @File     : st_03_table_05_highlight.py
# @Desc     : streamlit run st_03_table_05_highlight.py

from pandas import DataFrame
from streamlit import dataframe


def main() -> None:
    """ Main Function """
    df = DataFrame({
        "A": [1, 2, 3, 4],
        "B": [5, 6, 7, 8],
        "C": [9, 10, 11, 12]
    })

    dataframe(df.style.highlight_max(axis=0))


if __name__ == "__main__":
    main()
