#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/1/12 17:58
# @Author   :   Shawn
# @Version  :   Version 1.0
# @File     :   st_13_annotated_text_02.py
# @Desc     :   streamlit run st_13_annotated_text_02.py

from spacy import load
from streamlit import markdown
from string import punctuation


class TextAnnotator(object):
    """ This class is used to annotate text with different colors
        - NOUN: Yellow
        - VERB: Red
        - ADJ: Blue
        - ADV: Green
    """

    def __init__(self, string: str) -> None:
        self._string = string
        self._nlp = load("en_core_web_sm")
        self._doc = self._nlp(self._string)
        self._tokens = [(token.text, token.pos_) for token in self._doc]
        self._red = "#FFAAAA"
        self._yellow = "#FFEEAA"
        self._blue = "#88EEFE"
        self._green = "#AAFFAA"
        self._gray = "#525352"

    def annotate(self, size_main: int = 20, padding: int = 5, margin: int = 3, border_radius: int = 10) -> None:
        """ Annotate the text """
        _annotated = []
        _adjust: float = 0.6

        for token, pos in self._tokens:
            if token in punctuation:
                token = (f"<span style='font-size:{size_main}px;"
                         f"display:inline-block;"
                         f"margin-bottom:{margin}px;'>{token}</span>")
                _annotated.append(token)
                continue

            match pos:
                case "NOUN":
                    token = token.replace(token,
                                          f"<span style='background-color:{self._yellow};"
                                          f"font-size:{size_main}px;"
                                          f"padding:{padding}px;"
                                          f"display:inline-block;"
                                          f"margin-bottom:{margin}px;"
                                          f"border-radius:{border_radius}px;'>{token} "
                                          f"<span style='color:{self._gray};"
                                          f"font-size:{size_main * _adjust}px;'>{pos}</span></span>")
                    _annotated.append(token)
                case "VERB":
                    token = token.replace(token,
                                          f"<span style='background-color:{self._red};"
                                          f"font-size:{size_main}px;"
                                          f"padding:{padding}px;"
                                          f"display:inline-block;"
                                          f"margin-bottom:{margin}px;"
                                          f"border-radius:{border_radius}px;'>**{token}** "
                                          f"<span style='color:{self._gray};"
                                          f"font-size:{size_main * _adjust}px;'>{pos}</span></span>")
                    _annotated.append(token)
                case "ADJ":
                    token = token.replace(token,
                                          f"<span style='background-color:{self._blue};"
                                          f"font-size:{size_main}px;"
                                          f"padding:{padding}px;"
                                          f"display:inline-block;"
                                          f"margin-bottom:{margin}px;"
                                          f"border-radius:{border_radius}px;'>{token} "
                                          f"<span style='color:{self._gray};"
                                          f"font-size:{size_main * _adjust}px;'>{pos}</span></span>")
                    _annotated.append(token)
                case "ADV":
                    token = token.replace(token,
                                          f"<span style='background-color:{self._green};"
                                          f"font-size:{size_main}px;"
                                          f"padding:{padding}px;"
                                          f"display:inline-block;"
                                          f"margin-bottom:{margin}px;"
                                          f"border-radius:{border_radius}px;'>{token} "
                                          f"<span style='color:{self._gray};"
                                          f"font-size:{size_main * _adjust}px;'>{pos}</span></span>")
                    _annotated.append(token)
                case _:
                    token = (f"<span style='font-size:{size_main}px;"
                             f"padding:{padding}px;"
                             f"display:inline-block;"
                             f"margin-bottom:{margin}px;'>{token}</span>")
                    _annotated.append(token)
        _annotated = " ".join(_annotated)
        markdown(_annotated, unsafe_allow_html=True)


def main() -> None:
    """ Main Function """
    # Load the NLP model

    string = "I like to eat apples and bananas happily. I liked to eat fresh oranges and grapes."
    TextAnnotator(string).annotate()


if __name__ == "__main__":
    main()
