#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     : 2025/1/8 20:34
# @Author   : Shawn
# @Version  : Version 1.0
# @File     : st_06_progress_08.py
# @Desc     : streamlit run st_06_progress_08.py
# - pip install plotly

from dataclasses import dataclass, field
from enum import Enum, auto, unique
from faker import Faker
from pandas import DataFrame
from random import choice, uniform
from matplotlib import rcParams
from matplotlib import pyplot
from streamlit import markdown, empty, button, progress, sidebar, session_state
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
            "Name": _data_faker.first_name(),
            "Gender": choice([Gender.MALE.value, Gender.FEMALE.value]),
            "Age": _data_faker.random_int(min=self._AGE_MIN, max=self._AGE_MAX),
            "Chinese": _data_faker.random_int(min=self._SCORE_MIN, max=self._SCORE_MAX),
            "Math": _data_faker.random_int(min=self._SCORE_MIN, max=self._SCORE_MAX),
            "English": _data_faker.random_int(min=self._SCORE_MIN, max=self._SCORE_MAX),
        }
        self._students.append(student)

    @final
    def dataframer(self) -> DataFrame:
        """ Transform data to dataframe and display it """
        _df: DataFrame = DataFrame(self._students)
        # Set the index to start from 1
        _df.index = [f"{j + 1:0{len(str(len(_df)))}d}" for j in range(len(_df))]

        return _df

    @staticmethod
    def highlighter(df: DataFrame, col_highlight: list[str]):
        """ Highlight the max and min values in the dataframe """
        # #ECEFF1 , #FFFF80
        return df.style.highlight_max(
            subset=col_highlight, color="red"
        ).highlight_min(subset=col_highlight, color="green")


def chart_pie(counter: DataFrame, labels: list[str], title: str):
    """ Draw a pie chart """
    # Set the font as same as the font of streamlit
    rcParams["font.family"] = "sans-serif"
    # Draw the pie chart
    fig, ax = pyplot.subplots()
    # Set the background color as transparent
    fig.patch.set_facecolor("white")
    ax.pie(
        counter,
        labels=labels,
        autopct="%1.2f%%",
        startangle=90,
        colors=["red", "green"],  # 自定义颜色
    )
    # Set the title of the pie chart
    ax.set_title("Gender Distribution")
    return fig


def main() -> None:
    """ Main Function """
    TITLE: str = "Welcome to the the page of Students Information"
    markdown(f"<h1 style='text-align: center;'>{TITLE}</h1>", unsafe_allow_html=True)

    COL_HIGHLIGHT: list[str] = ["Chinese", "Math", "English"]

    sidebar.header("Data Generation")

    BAR_DEFAULT: int = 0
    input_num: int = sidebar.number_input("Data Amount", min_value=0, max_value=100, value=BAR_DEFAULT)

    # Initialize DataProcessor in session_state
    if "processor" not in session_state:
        session_state.processor = DataProcessor(input_num)
    dp: DataProcessor = session_state.processor

    empty_message = empty()
    empty_table = empty()
    empty_graph = empty()

    bar: progress = sidebar.progress(BAR_DEFAULT)
    empty_bar = sidebar.empty()

    DELAY: float = round(uniform(0, 1), 2)
    COL_L_DATA, _, COL_R_DATA = sidebar.columns([1, 1.6, 1])
    with COL_L_DATA:
        if button("Create"):
            if input_num == 0:
                empty_message.error("Please enter a number greater than 0.")
            else:
                empty_message.info(f"You are creating {input_num} pieces of data.")
                for i in range(input_num):
                    dp.generator()
                    df = dp.dataframer()
                    df_style = dp.highlighter(df, COL_HIGHLIGHT)

                    empty_table.dataframe(df_style, use_container_width=True)
                    prog: float = (i + 1) / input_num
                    bar.progress(prog)
                    sleep(DELAY)
                    empty_bar.markdown(f"<p style='text-align: center;'>Creating {prog * 100:.2f} %</p>",
                                       unsafe_allow_html=True)

            # Save the dataframe to session_state
            session_state.df = df
    with COL_R_DATA:
        if button("Reset"):
            bar.progress(BAR_DEFAULT)
            empty_bar.empty()
            empty_table.empty()
            empty_graph.empty()
            empty_message.success("The progress bar has been reset.")
            # Clear the session_state content
            if "processor" in session_state:
                del session_state.processor
            if "df" in session_state:
                del session_state.df

    sidebar.header("Results Display")

    COL_L_RESULT, _, COL_m_RESULT, _, COL_R_RESULT = sidebar.columns([1, 0.1, 1, 0.1, 1])
    with COL_L_RESULT:
        if button("LChart"):
            if "df" in session_state and not session_state.df.empty:
                empty_message.info("You chose to look at the LINE chart of the results.")
                X: str = "Name"
                Y: list[str] = COL_HIGHLIGHT
                # Display the dataframe and the line chart
                empty_table.dataframe(dp.highlighter(session_state.df, Y), use_container_width=True)
                empty_graph.line_chart(session_state.df, x=X, y=Y)
            else:
                empty_message.error("No data available. Please create data first.")
    with COL_m_RESULT:
        if button("BChart"):
            if "df" in session_state and not session_state.df.empty:
                empty_message.info("You chose to look at the BAR chart of the results.")
                X: str = "Name"
                Y: list[str] = COL_HIGHLIGHT
                # Display the dataframe and the line chart
                empty_table.dataframe(dp.highlighter(session_state.df, Y), use_container_width=True)
                empty_graph.bar_chart(session_state.df, x=X, y=Y)
            else:
                empty_message.error("No data available. Please create data first.")
    with COL_R_RESULT:
        if button("AChart"):
            if "df" in session_state and not session_state.df.empty:
                empty_message.info("You chose to look at the AREA chart of the genders.")
                X: str = "Name"
                Y: list[str] = ["Chinese", "Math", "English"]
                # Display the dataframe and the line chart
                empty_table.dataframe(dp.highlighter(session_state.df, Y), use_container_width=True)
                empty_graph.area_chart(session_state.df, x=X, y=Y)
            else:
                empty_message.error("No data available. Please create data first.")

    sidebar.header("Gender Display")

    COL_L_GENDER, _, _ = sidebar.columns([1, 1, 1])
    with COL_L_GENDER:
        if button("PChart"):
            if "df" in session_state and not session_state.df.empty:
                empty_message.info("You chose to look at the PIE chart of the genders.")

                # Count the number of genders
                counter = session_state.df["Gender"].value_counts()
                # Map gender values to labels
                category: dict[int, str] = {Gender.MALE.value: Gender.MALE.name,
                                            Gender.FEMALE.value: Gender.FEMALE.name}
                labels = counter.index.map(category)

                TITLE_PIE = "Gender Distribution"
                fig = chart_pie(counter, labels, TITLE_PIE)

                # Display the dataframe and the line chart
                empty_table.dataframe(dp.highlighter(session_state.df, COL_HIGHLIGHT), use_container_width=True)
                # Display the pie chart
                empty_graph.pyplot(fig)
            else:
                empty_message.error("No data available. Please create data first.")

    sidebar.header("Management")

    COL_L_MANAGE, _, _ = sidebar.columns([1, 1, 1])
    with COL_L_MANAGE:
        if button("Back"):
            if "df" in session_state and not session_state.df.empty:
                empty_message.info("You chose to look at the DATAFRAME.")
                # Display the dataframe and the line chart
                empty_table.dataframe(dp.highlighter(session_state.df, COL_HIGHLIGHT), use_container_width=True)
            else:
                empty_message.error("No data available. Please create data first.")


if __name__ == "__main__":
    main()
