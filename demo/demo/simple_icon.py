import reflex as rx
import reflex_ui as ui

def simple_icon_demo():
    icons = [
        "SiGithub",
        "SiPytorch",
        "SiPython",
        "SiReact",
        "SiDell",
        "SiOkta",
        "SiOpenai",
        "SiDatabricks",
        "SiDocker",
        "SiLinux",
        "SiVercel",
        "SiNetlify"
    ]

    # Define the pyramid shape (row lengths)
    row_counts = [1, 2, 3, 4, 5, 4, 3, 2, 1]

    # Track the index in the icons list
    index = 0
    rows = []

    for count in row_counts:
        row_icons = icons[index:index+count]
        index += count

        rows.append(
            rx.el.div(
                *[ui.simple_icon(icon, size=48) for icon in row_icons],
                class_name="flex justify-center gap-3 py-1"
            )
        )

    return rx.el.div(
        *rows,
        class_name="w-full h-screen flex flex-col items-center justify-center"
    )
