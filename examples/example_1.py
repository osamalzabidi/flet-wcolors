import flet as ft
from flet_wcolors import WColors


def main(page: ft.Page):
    page.title = "Web Colors Example 1"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.window.width = 800
    page.window.height = 600

    def color_search(e: ft.ControlEvent) -> None:
        for control in page.controls[1].controls:
            control.visible = e.control.value.lower() in control.content.value.lower()
        page.update()

    page.add(
        ft.TextField(
            hint_text="Search...",
            on_change=color_search
        ),
        ft.Row(
            wrap=True,
            expand=True,
            scroll=ft.ScrollMode.AUTO,
            controls=[
                ft.Container(
                    width=80,
                    height=80,
                    bgcolor=color,
                    alignment=ft.alignment.center,
                    border_radius=8,
                    content=ft.Text(
                        value = name,
                        color = ft.WColors.luminance(color),
                        text_align="center"
                    )
                )
                for name, color in ft.WColors._member_map_.items()
            ]
        )
    )

ft.app(target=main)
