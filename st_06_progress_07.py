#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     : 2025/1/8 19:29
# @Author   : Shawn
# @Version  : Version 1.0
# @File     : st_06_progress_07.py
# @Desc     : streamlit run st_06_progress_07.py

from dataclasses import dataclass, field
from enum import Enum, auto, unique
from faker import Faker
from pandas import DataFrame
from random import choice, uniform
from streamlit import markdown, empty, button, progress, sidebar
from time import sleep
from typing import final


@unique
class Gender(Enum):
    MALE: int = auto()
    FEMALE: int = auto()


@dataclass()
class DataProcessor(object):
    """ This class is used to process data """
    _AMOUNT: int = field(default=0)
    _AGE_MIN: int = field(default=6)
    _AGE_MAX: int = field(default=24)
    _SCORE_MIN: int = field(default=50)
    _SCORE_MAX: int = field(default=100)

    def __post_init__(self):
        self._students = []

    @final
    def generator(self):
        _data_faker = Faker()
        student = {
            "Name": _data_faker.name(),
            "Gender": choice([Gender.MALE.value, Gender.FEMALE.value]),
            "Age": _data_faker.random_int(min=self._AGE_MIN, max=self._AGE_MAX),
            "Chinese": _data_faker.random_int(min=self._SCORE_MIN, max=self._SCORE_MAX),
            "Math": _data_faker.random_int(min=self._SCORE_MIN, max=self._SCORE_MAX),
            "English": _data_faker.random_int(min=self._SCORE_MIN, max=self._SCORE_MAX),
        }
        self._students.append(student)

    @final
    def displayer(self, col_highlight: list[str]):
        """ Transform data to dataframe and display it """
        _df_students: DataFrame = DataFrame(self._students)
        # Set the index to start from 1
        _df_students.index = [f"{j + 1:0{len(str(len(_df_students)))}d}" for j in range(len(_df_students))]

        _df_highlight = self._highlighter(_df_students, col_highlight)
        return _df_highlight

    @staticmethod
    def _highlighter(df: DataFrame, col_highlight: list[str]):
        """ Highlight the max and min values in the dataframe """
        return df.style.highlight_max(
            subset=col_highlight, color="#ECEFF1"
        ).highlight_min(subset=col_highlight, color="#FFFF80")


def main() -> None:
    """ Main Function """
    TITLE: str = "Welcome to the the page of Students Information"
    markdown(f"<h1 style='text-align: center;'>{TITLE}</h1>", unsafe_allow_html=True)

    sidebar.header("Data Generation")

    BAR_MIN: int = 0
    BAR_MAX: int = 100
    BAR_DEFAULT: int = 0
    input_num: int = sidebar.number_input("Data Amount", min_value=BAR_MIN, max_value=BAR_MAX, value=BAR_DEFAULT)

    bar: progress = sidebar.progress(BAR_DEFAULT)
    empty_bar = sidebar.empty()

    empty_message = empty()

    empty_table = empty()

    DELAY: float = round(uniform(0, 1), 2)
    dp = DataProcessor(input_num)
    COL_L, COL_M, COL_R = sidebar.columns([1, 1.6, 1])
    with COL_L:
        if button("Create"):
            if input_num == 0:
                empty_message.error("Please enter a number greater than 0.")
            else:
                empty_message.info(f"You are creating {input_num} pieces of data.")
                COL_HIGHLIGHT: list[str] = ["Chinese", "Math", "English"]
                for i in range(input_num):
                    dp.generator()
                    df_style = dp.displayer(COL_HIGHLIGHT)

                    empty_table.dataframe(df_style, use_container_width=True)
                    prog: float = (i + 1) / input_num
                    bar.progress(prog)
                    sleep(DELAY)
                    empty_bar.markdown(f"<p style='text-align: center;'>Creating {prog * 100:.2f} %</p>",
                                       unsafe_allow_html=True)
    with COL_M:
        pass
    with COL_R:
        if button("Reset"):
            bar.progress(BAR_DEFAULT)
            empty_bar.empty()
            empty_message.success("The progress bar has been reset.")

    sidebar.header("Graph Management")


if __name__ == "__main__":
    main()
