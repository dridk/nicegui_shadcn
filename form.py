from nicegui import ui, Client


def Login():
    with ui.column().classes("w-screen w-screen h-screen flex justify-center content-center"):
        with ui.element().classes("border p-5 gap-4 shadow-xl rounded"):

            ui.label("Dimension").classes("font-semibold text-xl ")
            ui.label("Description du formulaire").classes("text-slate-400")
            with ui.grid(columns="auto 300px 30px").classes("my-3 mt-5"):
                forms = ("Width", "Max. width", "Height", "Max. height")

                for form in forms:
                    ui.label(form).classes(
                        "0 flex items-center justify-start text-bold truncate text-ellipsis whitespace-nowrap"
                    )
                    ui.input(placeholder=form).props("outlined dense ")
                    ui.switch(value=True).props("dense size=xs color=black")

            with ui.row().classes("flex justify-end mt-10"):
                ui.button("Annuler").props("color=slate-500 no-caps unelevated").classes(
                    "hover:slate-400"
                )
                ui.button("Envoyer").props("color=black no-caps unelevated")


@ui.page("/")
def login():
    Login()


ui.run()
