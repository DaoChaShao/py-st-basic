#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     : 2025/1/6 22:19
# @Author   : Shawn
# @Version  : Version 1.0
# @File     : st_03_table_04_sql.py
# @Desc     : streamlit run st_03_table_04_sql.py


from dataclasses import dataclass, field
from urllib.parse import quote

from pandas import DataFrame, read_sql
from sqlalchemy import create_engine, Engine, text
from streamlit import (write,
                       dataframe, markdown,
                       session_state, columns, button, rerun,
                       sidebar)


@dataclass
class SQLRequests(object):
    """
    Read the data from postgresql
    1. pip3 install psycopg2-binary
    2. pip3 install sqlalchemy
    """
    _RUNNING_TYPE: str = field(default="psycopg2")
    _DB_NAME: str = field(default="postgres")
    _DB_HOST: str = field(default="localhost")
    _DB_PORT: str = field(default="9527")
    _DB_USER: str = field(default="postgres")
    _DB_PASSWORD: str = field(default_factory=lambda: quote("123@"))

    _engine: Engine = field(init=False, repr=False)

    def __post_init__(self) -> None:
        """Initialize the SQLAlchemy engine."""
        self._engine = create_engine(
            f"postgresql+{self._RUNNING_TYPE}://"
            f"{self._DB_USER}:{self._DB_PASSWORD}@"
            f"{self._DB_HOST}:{self._DB_PORT}/"
            f"{self._DB_NAME}"
        )

    def load_dataframe(self, schema_name: str, table_name: str) -> DataFrame:
        """ Read the data from SQL """
        _query = text(f"SELECT * FROM {schema_name}.{table_name}")
        _dataframe = read_sql(_query, self._engine)

        return _dataframe


def table_pages(df: DataFrame, size: int = 10) -> None:
    """ Display the data in subpages """
    # Calculate the total number of subpages
    total = len(df) // size + (1 if len(df) % size > 0 else 0)

    # Initialize session state for the page number
    if "page" not in session_state:
        session_state.page = 1

    # Get the current page from session state
    page = session_state.page

    # Calculate the start and end row numbers of the current page
    row_start = (page - 1) * size
    row_end = row_start + size

    # Display the data of the current page
    dataframe(df.iloc[row_start:row_end], use_container_width=True)

    # Handle button clicks for previous and next page
    # Layout for buttons and page info
    col_previous, col_text, col_next = columns([1, 2, 1])
    with col_previous:
        if button("Previous", use_container_width=True):
            session_state.page = max(1, session_state.page - 1)
            rerun()
    # Display the page number in the center column
    with col_text:
        markdown(
            f"<div style='text-align: center; font-size: 16px;'>Page {page} of {total}</div>",
            unsafe_allow_html=True)
    with col_next:
        if button("Next", use_container_width=True):
            session_state.page = min(total, session_state.page + 1)
            rerun()


def main() -> None:
    """ Main Function """
    SCHEMA: str = "public"
    TABLE: str = "db_student"

    TITLE: str = "Welcome to the words from SQL"
    markdown(
        f"<h1 style='text-align: center;'>{TITLE}</h1>",
        unsafe_allow_html=True
    )

    sql = SQLRequests()
    df = sql.load_dataframe(SCHEMA, TABLE)
    df.index = [f"{i:02d}" for i in range(1, len(df) + 1)]

    cols = []
    sidebar.header("Basic Information")
    if sidebar.checkbox(label="ID", value=True):
        cols.append("id")
    if sidebar.checkbox(label="Name", value=True):
        cols.append("name")
    if sidebar.checkbox(label="Gender", value=True):
        cols.append("gender")
    if sidebar.checkbox(label="Birthday", value=True):
        cols.append("birthday")
    if sidebar.checkbox(label="Age", value=True):
        cols.append("age")
    if sidebar.checkbox(label="Class ID", value=True):
        cols.append("class_id")

    sidebar.header("Select Information")
    if sidebar.checkbox(label="Chinese"):
        cols.append("chinese")
    if sidebar.checkbox(label="Math"):
        cols.append("math")
    if sidebar.checkbox(label="English"):
        cols.append("english")

    # write(cols)
    table_pages(df[cols])


if __name__ == "__main__":
    main()
