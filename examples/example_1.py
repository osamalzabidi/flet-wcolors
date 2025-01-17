import flet as ft
from flet_wcolors import WColors


def main(page: ft.Page):
    page.title = "Web Colors Example 1"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.window.width = 800
    page.window.height = 600

    def color_search(e: ft.ControlEvent) -> None:
        search_text = e.control.value.lower()
        if len(search_text) >= 2:
            for control in page.controls[1].controls:
                control.visible = search_text in control.content.value.lower()
            page.update()

    page.add(
        ft.SearchBar(bar_hint_text="Search...", on_change=color_search),
        ft.Row(
            wrap=True,
            expand=True,
            scroll=ft.ScrollMode.AUTO,
            controls=[
                ft.Container(
                    width=90,
                    height=90,
                    bgcolor=color,
                    alignment=ft.alignment.center,
                    border_radius=8,
                    content=ft.Text(
                        value=name,
                        color=WColors.luminance_color(color),
                        text_align="center",
                    ),
                )
                for name, color in WColors._member_map_.items()
            ],
        ),
    )


if __name__ == "__main__":
    ft.app(target=main)
