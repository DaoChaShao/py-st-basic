#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     : 2025/1/9 15:37
# @Author   : Shawn
# @Version  : Version 1.0
# @File     : st_06_progress_09.py
# @Desc     : streamlit run st_06_progress_09.py

from datetime import time
from streamlit import progress, time_input, empty, set_page_config, title
from time import sleep


def time_convertor(value: time) -> int:
    """ Convert time object to seconds integer """
    return value.hour * 3600 + value.minute * 60 + value.second


def main() -> None:
    """ Main Function """
    PAGE_TITLE: str = "Streamlit Progress Bar"
    PAGE_ICON: str = "random"  # emoji: https://www.webfx.com/tools/emoji-cheat-sheet/
    set_page_config(
        page_title=PAGE_TITLE,
        page_icon=PAGE_ICON,
        layout="centered",  # centered or wide
    )

    title(PAGE_TITLE + " " + ":hourglass_flowing_sand:")
    "---"

    empty_message = empty()

    empty_bar_info = empty()
    bar = progress(0)

    value_time = time_input(label="Select a time", value=time(0, 0, 0))
    if str(value_time) == "00:00:00":
        empty_message.warning("Please select a time.")
    else:
        empty_message.info(f"Selected time: {value_time}")
        AMOUNT: int = time_convertor(value_time)

        for i in range(AMOUNT):
            percentage = round((i + 1) / AMOUNT * 100, 2)
            empty_bar_info.markdown(
                f"<h5 style='text-align: center;'>Processing: {percentage:.2f}%</h5>",
                unsafe_allow_html=True,
            )
            bar.progress((i + 1) / AMOUNT)
            sleep(1)

        empty_bar_info.success("Processing Complete!")
        empty_message.empty()


if __name__ == "__main__":
    main()
