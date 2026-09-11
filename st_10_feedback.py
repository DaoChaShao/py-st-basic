#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/1/14 20:40
# @Author   :   Shawn
# @Version  :   Version 1.0
# @File     :   st_10_feedback.py
# @Desc     :   streamlit run st_10_feedback.py

from streamlit import (logo, title, divider, expander, caption,
                       feedback, write, text, container, subheader,
                       columns, empty)


def main() -> None:
    """ Main Function """
    logo("streamlit logo.png")
    title("Feedback Example")
    divider()
    with expander("Feedback Example", expanded=False):
        caption("Please rate this app")

    empty_message = empty()

    stars: list[int] = [1, 2, 3, 4, 5]
    with container():
        subheader("Metrix")

        text("""
        A science-fiction masterpiece. Nolan executes a marvelous direction that slowly but efficiently puts in place a dark world creating a necessity to save humanity. Add to that great performances from Nolan and Hathaway plus a great score from Hans Zimmer. The result is on the best science-fiction movies of all time.
        """)

    col_l, _, col_r = columns([3, 9, 3])
    with col_l:
        star = feedback(options="stars")
    with col_r:
        if star is not None:
            match star:
                case 0:
                    caption(f"{stars[star]} star GRANTED")
                case 1:
                    caption(f"{stars[star]} stars GRANTED")
                case 2:
                    caption(f"{stars[star]} stars GRANTED")
                case 3:
                    caption(f"{stars[star]} stars GRANTED")
                case 4:
                    caption(f"{stars[star]} stars GRANTED")

    faces: list[str] = ["CRYING", "SAD", "NEUTRAL", "SMILING", "HAPPY"]
    with container():
        subheader("I love U")

        text("""
        After watching this insane movie in the theatres back in 2014 I swore to god I will wait 5 years to watch it again so I get to forget it and experince the insanity it has again This without doubt is THE BEST MOVIE EVER MADE
        """)

        col_l, _, col_r = columns([3, 9, 3])
        with col_l:
            face = feedback(options="faces")
        with col_r:
            if face is not None:
                match face:
                    case 0:
                        caption(f"You fell {faces[face]}")
                    case 1:
                        caption(f"You fell {faces[face]}")
                    case 2:
                        caption(f"You fell {faces[face]}")
                    case 3:
                        caption(f"You fell {faces[face]}")
                    case 4:
                        caption(f"You fell {faces[face]}")

    thumbs: list[str] = [":material/thumb_down:", ":material/thumb_up:"]
    with container():
        subheader("Good Man")

        text("""
        Sometimes I just need to see the start. Or end. Or a trailer. Or the music and theme from Hans Zimmer. Or the whole movie. Just to feel that thing, I only get from this movie. That the earth, space and time are something special, mystical. I never forget the first time I saw this movie, in an IMAX theatre in 2014. I was struck by it. Totally got me. And it stil does, 7 years later. This is the best movie ever made for me. Because of the feeling it gives me, no other movie can. So hard to get all of this emotion in only one movie. Brilliant.
        """)

        col_l, _, col_r = columns([3, 9, 3])
        with col_l:
            thumb = feedback(options="thumbs")
        with col_r:
            if thumb is not None:
                match thumb:
                    case 0:
                        caption(f"NOT AGREE {thumbs[thumb]}")
                    case 1:
                        caption(f"AGREE {thumbs[thumb]}")


if __name__ == "__main__":
    main()
