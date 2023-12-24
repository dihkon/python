import reflex as rx
import datetime
import link_bio.constants as const
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor as TextColor


def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="logo.png",
            height=Size.VERY_BIG.value
        ),
        rx.link(
            f"© 2005-{datetime.date.today().year} David Herranz v1.",
            href=const.YOUTUBE_URL,
            is_external=True,
            font_size=Size.MEDIUM.value
        ),
        rx.text(
            "Desde Barcelona con amor!",
            font_size=Size.MEDIUM.value,
            margin_top=Size.ZERO.value
        ),
        
        margin_bottom=Size.BIG.value,
        padding_bottom= Size.BIG.value,
        padding_x=Size.BIG.value,
        spacing=Size.DEFAULT.value,
        color=TextColor.FOOTER.value
    )

