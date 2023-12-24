import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size

def link_button(title: str, body: str, image: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src=image,
                    width=Size.LARGE.value,
                    height=Size.LARGE.value,
                    marging=Size.MEDIUM.value
                ),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    rx.text(body, style=styles.button_body_style),
                    align_items="start",
                    #spacing=Size.ZERO.value,
                    #marging=Size.ZERO.value
                    spacing=Size.SMALL.value,
                    padding_y=Size.SMALL.value,
                    padding_rigth=Size.SMALL.value
                ),
                width="100%"
                
            )
        ),
        href=url,
        is_external=True,
        width="100%"
    )
    