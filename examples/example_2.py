import flet as ft
from flet_wcolors import WColors


def main(page: ft.Page):
    page.title = "Web Colors Example 2"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.window.width = 800
    page.window.height = 600

    page.add(
        ft.Container(
            width=400,
            height=400,
            bgcolor=WColors.AMARANTH,
            alignment=ft.alignment.center,
            border_radius=8,
            content=ft.Text(
                value = "AMARANTH"
            )
        )
    )

ft.app(target=main)