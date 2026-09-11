#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/1/12 22:06
# @Author   :   Shawn
# @Version  :   Version 1.0
# @File     :   st_07_slider_chart.py
# @Desc     :   streamlit run st_07_slider_chart.py

from altair import Chart
from faker import Faker
from pandas import DataFrame
from streamlit import slider, write, altair_chart, line_chart


class AltairChart(object):
    """ Altair Chart Class """

    def __init__(self, data: DataFrame) -> None:
        """ Initialize Altair Chart """
        self._data = data

    def line(self, x: str, y: str) -> Chart:
        """ Generate Chart """
        chart = Chart(self._data).mark_line().encode(
            x=x,
            y=y,
        )
        return chart


class ScoreGenerator:
    """ Data Generator Class """

    def __init__(self, amount: int) -> None:
        """ Initialize Data Generator """
        self._faker = Faker()
        self._amount = amount
        self._data = None

    def generate(self, x: str, y: str) -> DataFrame:
        """ Generate Data """
        self._data = {
            x: [self._faker.first_name() for _ in range(self._amount)],
            y: [self._faker.random_int(40, 100) for _ in range(self._amount)]
        }
        return DataFrame(self._data)


def main() -> None:
    """ Main Function """
    AMOUNT = slider(label="Decay", min_value=0, max_value=100, value=10)
    write(AMOUNT)

    COL_X: str = "Name"
    COL_Y: str = "Score"
    data = ScoreGenerator(AMOUNT).generate(COL_X, COL_Y)

    altair_chart(AltairChart(data).line(COL_X, COL_Y), use_container_width=True)

    line_chart(data=data, x=COL_X, y=COL_Y, x_label=COL_X, y_label=COL_Y, use_container_width=True)

    data.set_index(COL_X, inplace=True)
    line_chart(data, use_container_width=True)


if __name__ == "__main__":
    main()
