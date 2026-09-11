#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     : 2025/1/6 19:10
# @Author   : Shawn
# @Version  : Version 1.0
# @File     : st_03_table_03_sql.py
# @Desc     : streamlit run st_03_table_03_sql.py

from dataclasses import dataclass, field
from turtledemo.sorting_animate import start_ssort
from urllib.parse import quote

from pandas import DataFrame, read_sql
from sqlalchemy import create_engine, Engine, text
from streamlit import title, table, slider, write, markdown


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
    # Set the page number
    page = slider(label="Page", min_value=1, max_value=total, value=1)

    # Calculate the start and end row numbers of the current page
    row_start = (page - 1) * size
    row_end = row_start + size

    # Display the data of the current page
    table(df[row_start:row_end])

    # Display the page number
    markdown(f"<div style='text-align: center;'>Page {page} of {total}</div>", unsafe_allow_html=True)


def main() -> None:
    """ Main Function """
    SCHEMA: str = "public"
    TABLE: str = "db_student"

    title("Welcome to the words from SQL")

    sql = SQLRequests()
    df = sql.load_dataframe(SCHEMA, TABLE)
    df.index = [f"{i:02d}" for i in range(1, len(df) + 1)]

    table_pages(df)


if __name__ == "__main__":
    main()
