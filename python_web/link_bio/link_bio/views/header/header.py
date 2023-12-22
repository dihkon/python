import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.styles.styles import Size as Size

def header()-> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(name="David Herranz", size="xl"),
            rx.vstack(
                rx.heading(
                    "David Herranz",
                     size="lg"
                ),
                rx.text(
                    "@dihkon",
                    margin_top="0px !important"
                ),
                rx.hstack(
                    link_icon("https://www.youtube.com/channel/UCTbo3urQ9I8tB-wc3txsmXQ"),
                    link_icon("https://www.youtube.com/channel/UCTbo3urQ9I8tB-wc3txsmXQ"),
                    link_icon("https://www.youtube.com/channel/UCTbo3urQ9I8tB-wc3txsmXQ"),
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
       
        rx.text("""Soy ingeniero de sistemas especialidado en entornos Middleware y Autonmatización.
                Actualmente desarrollos automatismos con diferente herramientas, Ansible, scripting, Automate...
                Mis intereses y hobbies son las nuevas tecnolgías, los videojuegos el cine y la lectura."""),
        spacing=Size.BIG.value,
        align_items="start"
    )