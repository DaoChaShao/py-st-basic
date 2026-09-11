#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     : 2025/1/10 14:50
# @Author   : Shawn
# @Version  : Version 1.0
# @File     : st_13_annotated_text_01.py
# @Desc     : streamlit run st_13_annotated_text_01.py
# pip install st-annotated-text

from annotated_text import annotated_text


def main() -> None:
    """ Main Function """
    annotated_text(
        "This ",
        ("is", "Verb"),
        " some ",
        ("annotated", "Adj"),
        ("text", "Noun"),
        " for those of ",
        ("you", "Pronoun"),
        " who ",
        ("like", "Verb"),
        " this sort of ",
        ("thing", "Noun"),
        ". ",
        "And here's a ",
        ("word", ""),
        " with a fancy background but no label.",
    )


if __name__ == "__main__":
    main()
