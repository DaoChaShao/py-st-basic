#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     : 2025/1/6 17:06
# @Author   : Shawn
# @Version  : Version 1.0
# @File     : st_04_chart.py
# @Desc     : streamlit run st_04_chart.py

from dataclasses import dataclass, field
from enum import Enum, auto, unique
from faker import Faker
from pandas import DataFrame
from streamlit import title, table, dataframe, line_chart, area_chart, bar_chart


@unique
class Gender(Enum):
    """ This class is used to define the gender """
    MALE = auto()
    FEMALE = auto()


@dataclass
class Data(object):
    """ Data Class """

    _AMOUNT: int = 10
    _AGE_MIN: int = 6
    _AGE_MAX: int = 24
    _SCORE_MIN: int = 40
    _SCORE_MAX: int = 100

    _data_faker: Faker = field(default_factory=Faker)
    _data: dict[str, list] = field(default_factory=dict)

    def __post_init__(self):
        self._data = {
            "Name": [self._data_faker.name()
                     for _ in range(self._AMOUNT)],
            "Gender": [self._data_faker.random_element([Gender.MALE.value, Gender.FEMALE.value])
                       for _ in range(self._AMOUNT)],
            "Age": [self._data_faker.random_int(self._AGE_MIN, self._AGE_MAX)
                    for _ in range(self._AMOUNT)],
            "Chinese": [self._data_faker.random_int(self._SCORE_MIN, self._SCORE_MAX)
                        for _ in range(self._AMOUNT)],
            "Math": [self._data_faker.random_int(self._SCORE_MIN, self._SCORE_MAX)
                     for _ in range(self._AMOUNT)],
            "English": [self._data_faker.random_int(self._SCORE_MIN, self._SCORE_MAX)
                        for _ in range(self._AMOUNT)]
        }

    def to_df(self):
        """ This function is used to convert the data to a DataFrame """
        return DataFrame(self._data)


def main() -> None:
    """ Main Function """
    title("Hello Streamlit!")

    data = Data()
    df = data.to_df()
    table(df)

    dataframe(df)

    line_chart(data=df, x="Name", y=["Chinese", "Math", "English"])
    area_chart(data=df, x="Name", y=["Chinese", "Math", "English"])
    bar_chart(data=df, x="Name", y=["Chinese", "Math", "English"])



if __name__ == "__main__":
    main()
