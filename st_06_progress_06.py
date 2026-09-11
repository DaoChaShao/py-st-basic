#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     : 2025/1/8 17:00
# @Author   : Shawn
# @Version  : Version 1.0
# @File     : st_06_progress_06.py
# @Desc     : 

from dataclasses import dataclass, field
from enum import Enum, auto, unique
from faker import Faker
from pandas import DataFrame
from random import choice, uniform
from streamlit import markdown, empty, button, progress, number_input, columns
from time import sleep
from typing import final


@unique
class Gender(Enum):
    MALE: int = auto()
    FEMALE: int = auto()


@dataclass()
class DataProcessor(object):
    """ This class is used to process data """
    AGE_MIN: int = 6
    AGE_MAX: int = 24

    input_num: int = field(default=0)
    students: list = field(default_factory=list)

    @final
    def generator(self):
        _data_faker = Faker()
        student = {
            "Name": _data_faker.name(),
            "Gender": choice([Gender.MALE.value, Gender.FEMALE.value]),
            "Age": _data_faker.random_int(min=self.AGE_MIN, max=self.AGE_MAX)
        }
        self.students.append(student)

    @final
    def displayer(self, col_highlight: list[str]):
        """ Transform data to dataframe and display it """
        _df_students: DataFrame = DataFrame(self.students)
        # Set the index to start from 1
        _df_students.index = [f"{j + 1:0{len(str(len(_df_students)))}d}" for j in range(len(_df_students))]

        _df_style = _df_students.style.highlight_max(
            subset=col_highlight, color="red").highlight_min(subset=col_highlight, color="green")
        return _df_style


def main() -> None:
    """ Main Function """
    TITLE: str = "Welcome to the the page of Students Information"
    markdown(f"<h1 style='text-align: center;'>{TITLE}</h1>", unsafe_allow_html=True)

    BAR_MIN: int = 0
    BAR_MAX: int = 100
    BAR_DEFAULT: int = 0
    input_num: int = number_input("Total", min_value=BAR_MIN, max_value=BAR_MAX, value=BAR_DEFAULT)

    empty_bar = empty()
    bar: progress = progress(BAR_DEFAULT)

    empty_message = empty()

    empty_table = empty()

    dp = DataProcessor(input_num=input_num)
    COL_L, COL_M, COL_R = columns([1, 7, 1])
    with COL_L:
        if button("Start"):
            if input_num == 0:
                empty_message.error("Please enter a number greater than 0.")
            else:
                empty_message.info(f"You are creating {input_num} pieces of data.")
                COL_HIGHLIGHT: list[str] = ["Age", ]
                for i in range(input_num):
                    dp.generator()
                    df_style = dp.displayer(COL_HIGHLIGHT)

                    empty_table.dataframe(df_style, use_container_width=True)
                    prog: float = (i + 1) / input_num
                    bar.progress(prog)
                    sleep(round(uniform(0, 1), 1))
                    empty_bar.markdown(f"<p style='text-align: center;'>Creating {prog * 100:.2f} %</p>",
                                       unsafe_allow_html=True)
    with COL_M:
        pass
    with COL_R:
        if button("Reset"):
            bar.progress(BAR_DEFAULT)
            empty_bar.empty()
            empty_message.success("The progress bar has been reset.")


if __name__ == "__main__":
    main()
