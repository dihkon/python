import reflex as rx

def header()-> rx.Component:
    return rx.vstack(
        rx.avatar(name="David Herranz", size="xl"),
        rx.text("@dihkon"),
        rx.text("HOLA MI NOMBRE ES DAVID HERRANZ"),
        rx.text("""Soy ingeniero de sistemas especialidado en entornos Middleware y Autonmatización.
                Actualmente desarrollos automatismos con diferente herramientas, Ansible, scripting, Automate...
                Mis intereses y hobbies son las nuevas tecnolgías, los videojuegos el cine y la lectura.""")
    )