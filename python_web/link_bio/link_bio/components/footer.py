import reflex as rx
import datetime

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico"),
        rx.link(f"@ 2005-{datetime.date.today().year} desde Barcelona con amor!",
                href="https://www.youtube.com/channel/UCTbo3urQ9I8tB-wc3txsmXQ",
                is_external=True),
        rx.text("David Herranz Bueno")
        
    )