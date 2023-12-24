import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title
from link_bio.styles.styles import Size as Size
import link_bio.constants as constants


def links() -> rx.Component:
    return rx.vstack(
        title("Comunidad"),
        link_button(
            "Youtube",
            "Gameplays diarios",
            "icons/youtube.svg",
            constants.YOUTUBE_URL
        ),
        link_button(
            "Twitch",
            "Retransmisiones diarias",
            "icons/twitch.svg",
            constants.TWITCH_URL
        ),
        link_button(
            "Facebook",
            "Perfil personal",
            "icons/facebook.svg",
            constants.YOUTUBE_URL
        ),
        link_button(
            "Discord",
            "De todo un poco",
            "icons/discord.svg",
            constants.DISCORD_URL
        ),

        title("Comunidad"),
        link_button(
            "Youtube",
            "Gameplays diarios",
            "icons/youtube.svg",
            constants.YOUTUBE_URL
        ),
        link_button(
            "Twitch",
            "Retransmisiones diarias",
            "icons/twitch.svg",
            constants.TWITCH_URL
        ),
        link_button(
            "Facebook",
            "Perfil personal",
            "icons/facebook.svg",
            constants.YOUTUBE_URL
        ),
        link_button(
            "Discord",
            "De todo un poco",
            "icons/discord.svg",
            constants.DISCORD_URL
        ),
        title("Contacto"),
        link_button(
            "Email",
            constants.EMAIL,
            "icons/email.svg",
            f"mailto:{constants.EMAIL}"
        ),
        width="100%",
        spacing=Size.MEDIUM.value
    )