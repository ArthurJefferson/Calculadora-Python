import flet as ft
import time


def main(page: ft.Page):

    #Colors
    cor2 = ft.Colors.GREEN

    # PAGE CONFIG
    page.title = "Calculadora 10/10"
    page.window.width = 350
    page.window.height = 450
    page.window.resizable = False
    page.window.maximizable = False

    campo = ft.TextField(value="", read_only=True, border_color=cor2)

    calculo = None  # 1 = mais, 2 = menos, 3 = div, 4 = mult
    x = None
    y = None
    z = None

    def plus(e):
        try:
            nonlocal calculo, x
            calculo = 1
            x = int(campo.value)
            campo.value = ""
            campo.update()
        except ValueError:
            campo.value = "Erro"
            campo.update()
            time.sleep(1.5)
            campo.value = ""
            campo.update()

    def menos(e):
        try:
            nonlocal calculo, x
            calculo = 2
            x = int(campo.value)
            campo.value = ""
            campo.update()
        except ValueError:
            campo.value = "Erro"
            campo.update()
            time.sleep(1.5)
            campo.value = ""
            campo.update()

    def c(e):
        try:
            nonlocal campo
            campo.value = ""
            campo.update()
        except ValueError:
            campo.value = "Erro"
            campo.update()
            time.sleep(1.5)
            campo.value = ""
            campo.update()

    def div(e):
        try:
            nonlocal calculo, x
            calculo = 3
            x = int(campo.value)
            campo.value = ""
            campo.update()
        except ValueError:
            campo.value = "Erro"
            campo.update()
            time.sleep(1.5)
            campo.value = ""
            campo.update()

    def mult(e):
        try:
            nonlocal calculo, x
            calculo = 4
            x = int(campo.value)
            campo.value = ""
            campo.update()
        except ValueError:
            campo.value = "Erro"
            campo.update()
            time.sleep(1.5)
            campo.value = ""
            campo.update()

    def igual(e):
        nonlocal y, x, calculo, campo
        y = int(campo.value)
        if x == None or y == None:
            campo.value = "Erro"

        if calculo == 3 and y == 0 or x == 0:
            z = "Não é possivel dividir 0"
        else:
            match calculo:
                case 1:
                    z = x + y
                case 2:
                    z = x - y
                case 3:
                    z = x / y
                case 4:
                    z = x * y

        campo.value = str(z)
        campo.update()

    def click(e):
        campo.value += e.control.text
        campo.update()

    tec_calc1 = ft.Row(
        controls=[
            ft.ElevatedButton(text="7", on_click=click, width=60, height=60, color=cor2),
            ft.ElevatedButton(text="8", on_click=click, width=60, height=60, color=cor2),
            ft.ElevatedButton(text="9", on_click=click, width=60, height=60, color=cor2),
            ft.ElevatedButton(text="/", on_click=div, width=60, height=60, color=cor2),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20
    )

    tec_calc2 = ft.Row(
        controls=[
            ft.ElevatedButton(text="4", on_click=click, width=60, height=60, color=cor2),
            ft.ElevatedButton(text="5", on_click=click, width=60, height=60, color=cor2),
            ft.ElevatedButton(text="6", on_click=click, width=60, height=60, color=cor2),
            ft.ElevatedButton(text="x", on_click=mult, width=60, height=60, color=cor2),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20
    )

    tec_calc3 = ft.Row(
        controls=[
            ft.ElevatedButton(text="1", on_click=click, width=60, height=60, color=cor2),
            ft.ElevatedButton(text="2", on_click=click, width=60, height=60, color=cor2),
            ft.ElevatedButton(text="3", on_click=click, width=60, height=60, color=cor2),
            ft.ElevatedButton(text="+", on_click=plus, width=60, height=60, color=cor2),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20
    )

    tec_func = ft.Row(
        controls=[
            ft.ElevatedButton(text="C", on_click=c, width=60, height=60, color=cor2),
            ft.ElevatedButton(text="0", on_click=click, width=60, height=60, color=cor2),
            ft.ElevatedButton(text="=", on_click=igual, width=60, height=60, color=cor2),
            ft.ElevatedButton(text="-", on_click=menos, width=60, height=60, color=cor2)
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20
    )

    HUD = ft.Column(
        controls=[
            campo,
            tec_calc1,
            tec_calc2,
            tec_calc3,
            tec_func
        ]
    )

    page.add(HUD)


ft.app(target=main)
