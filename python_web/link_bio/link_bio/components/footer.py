import reflex as rx
import datetime
from link_bio.styles.styles import Size as Size

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico"),
        rx.link(
            f"@ 2005-{datetime.date.today().year} David Herranz v1.",
            href="https://www.youtube.com/channel/UCTbo3urQ9I8tB-wc3txsmXQ",
            is_external=True,
            font_size=Size.MEDIUM.value
        ),
        rx.text(
            "Desde Barcelona con amor!",
            margin_top="0px !important"
        ),
        font_size=Size.MEDIUM.value,
        margin_bottom=Size.BIG.value
    )