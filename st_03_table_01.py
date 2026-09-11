#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     : 2025/1/6 16:56
# @Author   : Shawn
# @Version  : Version 1.0
# @File     : st_03_table_01.py
# @Desc     : streamlit run st_03_table_01.py

from dataclasses import dataclass, field
from enum import Enum, auto, unique
from faker import Faker
from pandas import DataFrame
from streamlit import title, table, dataframe


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

    _data_faker: Faker = field(default_factory=Faker)
    _data: dict[str, list] = field(default_factory=dict)

    def __post_init__(self):
        self._data = {
            "Name": [self._data_faker.name()
                     for _ in range(self._AMOUNT)],
            "Gender": [self._data_faker.random_element([Gender.MALE.value, Gender.FEMALE.value])
                       for _ in range(self._AMOUNT)],
            "Age": [self._data_faker.random_int(self._AGE_MIN, self._AGE_MAX)
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


if __name__ == "__main__":
    main()
