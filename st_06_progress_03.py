#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     : 2025/1/8 15:24
# @Author   : Shawn
# @Version  : Version 1.0
# @File     : st_06_progress_03.py
# @Desc     : streamlit run st_06_progress_03.py

from enum import Enum, auto, unique
from faker import Faker
from random import choice, uniform
from streamlit import markdown, empty, button, progress, number_input, columns
from time import sleep


@unique
class Gender(Enum):
    MALE: int = auto()
    FEMALE: int = auto()


def main() -> None:
    """ Main Function """
    data_faker: Faker = Faker()

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

    COL_L, COL_M, COL_R = columns([1, 7, 1])
    with COL_L:
        students: list = []
        if button("Start"):
            if input_num == 0:
                empty_message.error("Please enter a number greater than 0.")
            else:
                AGE_MIN: int = 6
                AGE_MAX: int = 24
                empty_message.info(f"You are creating {input_num} pieces of data.")

                for i in range(BAR_MIN, input_num):
                    student = {
                        "Name": data_faker.name(),
                        "Gender": choice([Gender.MALE.value, Gender.FEMALE.value]),
                        "age": data_faker.random_int(min=AGE_MIN, max=AGE_MAX)
                    }
                    students.append(student)

                    empty_table.table(students)

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
