#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/1/13 23:03
# @Author   :   Shawn
# @Version  :   Version 1.0
# @File     :   st_09_canvas.py
# @Desc     :   streamlit run st_09_canvas.py
# - pip install streamlit_drawable_canvas

from PIL import Image
from streamlit import (title, sidebar, header, selectbox, slider,
                       color_picker, empty, columns, subheader, expander,
                       caption, logo, divider, button, image,
                       session_state, rerun, toggle)
from streamlit_drawable_canvas import st_canvas


def main() -> None:
    """ Main Function """
    logo("streamlit logo.png")
    title("Drawable Canvas")
    with expander("Instructions"):
        caption("1. Select a drawing tool from the sidebar.")
        caption("2. Draw on the canvas.")
        caption("3. Save or clear your drawing using the buttons below the canvas.")
        caption("4. The saved drawing will be displayed below the canvas.")
    divider()
    empty_message = empty()

    # ------------------------------ Sess Zone ------------------------------ #
    IMAGE: str = "canvas"
    if "canvas" not in session_state:
        session_state["canvas"] = "canvas_new"

    # ------------------------------ Side Zone ------------------------------ #
    with sidebar:
        header("Drawer Setting")
        col_t, _, col_b = columns([2, 0.1, 0.5], vertical_alignment="center")
        with col_t:
            undo: bool = toggle(label="Undo Function", value=False,
                                help="Enable or disable the undo function and click the back confirm button.")
        with col_b:
            button(":thumbsup:", help="Confirm the UNDO setting.", on_click=rerun)

        mode: str = selectbox(label="Drawing tool", index=1, help="Select a drawing tool.",
                              options=("point", "freedraw", "line", "rect", "circle", "transform"))
        if mode == "point":
            radius: int = slider("Point display radius", 1, 25, 3, help="Radius of the point.")

        stroke_width: int = slider("Stroke width", 10, 30, 12, help="Width of the drawing.")

        col_s, _, col_bg = columns([1, 0.9, 1.1])
        with col_s:
            stroke_color: str = color_picker("Stroke", "#000", help="Color of the drawing.")
        with col_bg:
            bg_color: str = color_picker("Background", "#eee", help="Background color of the canvas.")

        header("Actions")
        empty_button = empty()

    # ------------------------------ Main Zone ------------------------------ #
    col_c, _, col_i = columns([1, 0.4, 1])
    with col_c:
        subheader("Canvas")
        canvas_result = st_canvas(
            fill_color="rgba(255, 165, 0, 0.3)",
            stroke_width=stroke_width,
            stroke_color=stroke_color,
            background_color=bg_color,
            height=280,
            width=280,
            drawing_mode=mode,
            display_toolbar=undo,
            point_display_radius=radius if mode == "point" else 0,
            key=session_state["canvas"],
        )
    with col_i:
        subheader("Preview")
        if canvas_result.image_data is not None:
            image(canvas_result.image_data, caption="Preview of Drawing", use_container_width=True)
        empty_message.warning("No drawing to display. Draw something on the canvas!")

    if canvas_result.image_data is not None:
        with (empty_button.container()):
            col_s, _, col_c = columns([1, 0.1, 1])
            with col_s:
                if button("Save Drawing"):
                    img = Image.fromarray(canvas_result.image_data)
                    img.save(f"{IMAGE}.png")
                    empty_message.success(f"Drawing outcome **{IMAGE.upper()}** has been saved!")

            with col_c:
                if button("Clear Drawing"):
                    session_state["canvas"] = f"canvas{session_state['canvas']}"
                    empty_message.success("Drawing has been cleared!")
                    rerun()


if __name__ == "__main__":
    main()
