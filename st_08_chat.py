#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/1/13 18:25
# @Author   :   Shawn
# @Version  :   Version 1.0
# @File     :   st_08_chat.py
# @Desc     :   streamlit run st_08_chat.py
from streamlit import empty
from streamlit_chat import message


def main() -> None:
    """ Main Function """
    empty_chat_message = empty()

    with empty_chat_message.container():
        message("Hello, I am Ollama. How can I help you today?", False, avatar_style="bottts")
        message("I need help with my story.", True, avatar_style="adventurer-neutral")
        message("Sure, I can help you with that. What do you need help with?", False, avatar_style="pixel-art")


if __name__ == "__main__":
    main()
