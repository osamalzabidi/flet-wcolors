import flet as ft
from flet_wcolors import WColors


def main(page: ft.Page):
    page.title = "Web Colors Example 2"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.window.width = 800
    page.window.height = 600

    def change_color(e: ft.ControlEvent) -> None:
        color: str = WColors.random()
        e.control.bgcolor = color
        e.control.content.color = WColors.luminance_color(color)
        e.control.update()

    page.add(
        ft.Container(
            width=400,
            height=400,
            bgcolor=(color := WColors.random()),
            alignment=ft.alignment.center,
            border_radius=8,
            content=ft.Text(value="Click me!", color=WColors.luminance_color(color)),
            on_click=change_color,
            ink=True,
        )
    )


if __name__ == "__main__":
    ft.app(target=main)
