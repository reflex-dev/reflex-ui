import reflex as rx

def hi(name: str, **props) -> rx.Component:
    return rx.icon(tag=name, **props)

def get_icon(icon: str, **props) -> rx.Component:
    return rx.icon(tag=icon, **props)

def spinner(**props) -> rx.Component:
    return rx.spinner(**props)
