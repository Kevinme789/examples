import flet as ft


class NewMessageWebView(ft.View):
    def __init__(self):
        super().__init__()
        self.fullscreen_dialog = True
        self.appbar = ft.AppBar(title=ft.Text("New Message"))
        self.controls = [ft.Text("New Message")]


class NewMessageMobileView(ft.View):
    def __init__(self):
        super().__init__()
        self.fullscreen_dialog = True
        self.appbar = ft.AppBar(title=ft.Text("New Message"))
        self.controls = [ft.Text("New Message")]
