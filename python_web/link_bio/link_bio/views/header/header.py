import reflex as rx
import link_bio.constants as const
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles.colors import Color as Color


def header()-> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                name="David Herranz",
                size="xl",
                src="avatar.jpg",
                color=TextColor.BODY.value,
                bg=Color.CONTENT.value,
                padding="2px",
                border="4px",
                border_color=Color.PRIMARY.value
            ),
            rx.vstack(
                rx.heading(
                    "David Herranz",
                    size="lg"
                ),
                rx.text(
                    "@dihkon",
                    margin_top=Size.ZERO.value,
                    color=TextColor.BODY.value
                ),
                rx.hstack(
                    link_icon(
                        "icons/youtube.svg",
                        const.YOUTUBE_URL
                    ),
                    link_icon(
                        "icons/twitch.svg",
                        const.TWITCH_URL
                    ),
                    link_icon(
                        "icons/discord.svg",
                        const.DISCORD_URL
                    ),
                    spacing=Size.DEFAULT.value
                ),
                
                align_items="start"
                
            ),
            spacing=Size.BIG.value
            

        ),

        rx.flex(
            info_text("+13", "años de experiencia"),
            rx.spacer(),
            info_text("+13", "años de experiencia"),
            rx.spacer(),
            info_text("+13", "años de experiencia"),
            width="100%"            
        ),
       
        rx.text(
            f"""Soy ingeniero de sistemas especialidado en entornos Middleware y Autonmatización.
                Actualmente desarrollos automatismos con diferente herramientas, Ansible, scripting, Automate...
                Mis intereses y hobbies son las nuevas tecnolgías, los videojuegos el cine y la lectura.""",
                font_size=Size.MEDIUM.value,
                color=TextColor.BODY.value
        ),
        spacing=Size.BIG.value,
        align_items="start"
    )