#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     : 2025/1/6 17:17
# @Author   : Shawn
# @Version  : Version 1.0
# @File     : st_05_form.py
# @Desc     : streamlit run st_05_form.py

from streamlit import (title,
                       form,
                       text_input, radio, slider, select_slider,
                       date_input, selectbox, checkbox, multiselect,
                       form_submit_button,
                       write, balloons, warning,
                       markdown)


def main() -> None:
    """ Main Function """
    hider = """
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """
    markdown(hider, unsafe_allow_html=True)

    title("Form Example")

    with form(key="form_user_info"):
        respond = {
            "name": text_input(label="Name"),
            "gender": radio(label="Gender", options=["Female", "Male"]),
            "age": slider(label="Age", min_value=6, max_value=24, value=18),
            "height": select_slider(label="Height", options=[1.5, 1.6, 1.7, 1.8, 1.9, 2.0], value=(1.6, 1.8)),
            "birthday": date_input(label="Birthday"),
            "subject": selectbox(label="Subjects", options=["Chinese", "Math", "English"]),
            "is_student": checkbox(label="Are you a student?"),
            "hobby": multiselect(label="Hobbies", options=["Reading", "Running", "Swimming"])
        }

        submit = form_submit_button(label="Submit")

        def is_valid(data: dict) -> bool:
            return all(data.values())

        if submit and is_valid(respond):
            balloons()
            title("User Info")
            for key, value in respond.items():
                write(f"{key}: {value}")
        else:
            warning("Please complete the form.")


if __name__ == "__main__":
    main()
