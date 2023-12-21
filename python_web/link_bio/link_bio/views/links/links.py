import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title


def links() -> rx.Component:
    return rx.vstack(
        title("Comunidad"),
        link_button(
            "Youtube",
            "Gameplays diarios",
            "https://www.youtube.com/channel/UCTbo3urQ9I8tB-wc3txsmXQ"
        ),
        link_button(
            "Twitch",
            "Retransmisiones diarias",
            "https://www.youtube.com/channel/UCTbo3urQ9I8tB-wc3txsmXQ"
        ),
        link_button(
            "Facebook",
            "Perfil personal",
            "https://www.youtube.com/channel/UCTbo3urQ9I8tB-wc3txsmXQ"
        ),
        link_button(
            "Discord",
            "De todo un poco",
            "https://www.youtube.com/channel/UCTbo3urQ9I8tB-wc3txsmXQ"
        ),

        title("Comunidad"),
        link_button(
            "Youtube",
            "Gameplays diarios",
            "https://www.youtube.com/channel/UCTbo3urQ9I8tB-wc3txsmXQ"
        ),
        link_button(
            "Twitch",
            "Retransmisiones diarias",
            "https://www.youtube.com/channel/UCTbo3urQ9I8tB-wc3txsmXQ"
        ),
        link_button(
            "Facebook",
            "Perfil personal",
            "https://www.youtube.com/channel/UCTbo3urQ9I8tB-wc3txsmXQ"
        ),
        link_button(
            "Discord",
            "De todo un poco",
            "https://www.youtube.com/channel/UCTbo3urQ9I8tB-wc3txsmXQ"
        ),
        width="100%"
    )