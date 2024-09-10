from nicegui import ui, Client


def Header():

    return ui.element().classes("w-full h-16 border-b-[1px] border-lightgray ")


def Menu():

    def Item(icon="inbox", title="inbox", count=43):
        with ui.element("div").classes(
            "flex justify-between w-full round-lg group rounded p-2 hover:bg-black"
        ):
            with ui.element("div").classes("flex gap-2 "):
                ui.icon(icon).classes("group-hover:text-white")
                ui.label(title).classes("group-hover:text-white")

            if count > 0:
                ui.label(str(count)).classes("group-hover:text-white font-semibold")

    with Header():
        # ui.select(["bob@test.fr"], value="bob@test.fr").classes("h-full")
        with ui.element().classes("flex justify-center h-full content-center mx-4"):
            with ui.element("select").classes("w-full h-8 px-2 bg-white border rounded "):
                with ui.element("option"):
                    ui.label("bob@test.fr")

    with ui.element().classes("flex justify-center m-3 gap-2"):

        for icon, title, count in (
            ("inbox", "Inbox", 128),
            ("article", "Drafts", 9),
            ("send", "Sent", 0),
            ("outbox", "Outbox", 23),
            ("delete", "Trash", 0),
            ("archive", "Archive", 0),
        ):
            Item(icon, title, count)


def Mail():

    def Message():
        with ui.element().classes(" w-full border rounded flex p-2"):

            with ui.element().classes("flex justify-between w-full  h-6"):
                ui.label("William Smith").classes("font-bold flex justify-start")
                ui.label("10 months ago").classes("flex justify-end")

            ui.label("Metting tomorow")

            ui.label(
                "Hi, let's have a meeting tomorrow to discuss the project. I've been reviewing the "
            )
            ui.toggle(["All mail", "Unread"]).props("no-caps size=md flat")

    with ui.element().classes("w-full  flex"):
        with Header():
            with ui.element().classes("w-full h-full flex justify-between content-center"):

                ui.label("Inbox").classes("font-bold mx-4 text-lg ")
                ui.toggle(["All mail", "Unread"]).props("no-caps size=md flat").classes("mx-2")

        with ui.element().classes("flex  w-full  "):
            ui.input("Search...").props("dense outlined").classes("w-full mx-2 my-2")

        with ui.element().classes("h-full no-scrollbar"):
            with ui.column():
                for i in range(4):
                    Message()


def ReadMail():

    def ActionButton(icon: str, tooltip: str = ""):
        with ui.button(icon=icon).props("flat color=black size=sm"):
            ui.tooltip("Archive").classes("bg-black")

    with Header():
        with ui.row().classes("w-full flex content-center h-full"):
            with ui.element().classes("flex justify-start gap-3"):
                ActionButton("eva-archive-outline")
                ActionButton("eva-trash-outline")
                ActionButton("eva-trash-2-outline")
                ui.separator().props("vertical")
                ActionButton("eva-clock-outline")

            with ui.element().classes("flex ml-auto gap-3"):
                ActionButton("eva-arrow-ios-back-outline")
                ActionButton("eva-arrowhead-left-outline")
                ActionButton("eva-arrow-ios-forward-outline")

            ui.separator().props("vertical")
            with ui.button(icon="eva-more-vertical-outline").props("flat color=black size=sm"):
                with ui.menu():
                    ui.menu_item("Mark as unread")
                    ui.menu_item("Start thread")
                    ui.menu_item("Add label")
                    ui.menu_item("Mute thread")

    with ui.row().classes("w-full"):
        ui.label("WS").classes("ml-4").style(
            "padding: 10px; border-radius:50px; background-color: hsl(240,5%,96%)"
        )
        with ui.element().classes("flex-column"):
            ui.label("William Smith").classes("font-semibold")
            ui.label("Meeting Tomorrow")
            ui.label("Reply-To: williamsmith@example.com")
        ui.label("Oct 22, 2023, 9:00:00 AM").classes("ml-auto mr-4").style("color: hsl(240,4%,46%)")

        ui.label(
            """Thank you for the project update. It looks great! I've gone through the report, and the progress is impressive. The team has done a fantastic job, and I appreciate the hard work everyone has put in.
            
            I have a few minor suggestions that I'll include in the attached document.
            
            Let's discuss these during our next meeting. Keep up the excellent work!
            
            Best regards, Alice"""
        ).classes("w-full h-[200px] text-left border-t-[1px] p-5")

    ui.separator()

    with ui.element().classes("flex flex-col w-full gap-2"):
        ui.textarea(placeholder="Reply William Smith...").props("outlined").classes(
            "flex justify-center m-4"
        )
        with ui.element().classes("flex justify-between"):
            ui.switch("Mute this thread").props("color=black").classes("mx-4")
            ui.button("Send").props("color=slate-900 no-caps").classes("mx-4")


@ui.page("/")
def page():
    def Separator():

        ui.html(
            "<div class='z-10 flex h-4 w-3 items-center justify-center rounded-sm border bg-border bg-slate-200'><svg width='25' height='25' viewBox='0 0 15 15' fill='none' xmlns='http://www.w3.org/2000/svg' class='h-2.5 w-2.5'><path d='M5.5 4.625C6.12132 4.625 6.625 4.12132 6.625 3.5C6.625 2.87868 6.12132 2.375 5.5 2.375C4.87868 2.375 4.375 2.87868 4.375 3.5C4.375 4.12132 4.87868 4.625 5.5 4.625ZM9.5 4.625C10.1213 4.625 10.625 4.12132 10.625 3.5C10.625 2.87868 10.1213 2.375 9.5 2.375C8.87868 2.375 8.375 2.87868 8.375 3.5C8.375 4.12132 8.87868 4.625 9.5 4.625ZM10.625 7.5C10.625 8.12132 10.1213 8.625 9.5 8.625C8.87868 8.625 8.375 8.12132 8.375 7.5C8.375 6.87868 8.87868 6.375 9.5 6.375C10.1213 6.375 10.625 6.87868 10.625 7.5ZM5.5 8.625C6.12132 8.625 6.625 8.12132 6.625 7.5C6.625 6.87868 6.12132 6.375 5.5 6.375C4.87868 6.375 4.375 6.87868 4.375 7.5C4.375 8.12132 4.87868 8.625 5.5 8.625ZM10.625 11.5C10.625 12.1213 10.1213 12.625 9.5 12.625C8.87868 12.625 8.375 12.1213 8.375 11.5C8.375 10.8787 8.87868 10.375 9.5 10.375C10.1213 10.375 10.625 10.8787 10.625 11.5ZM5.5 12.625C6.12132 12.625 6.625 12.1213 6.625 11.5C6.625 10.8787 6.12132 10.375 5.5 10.375C4.87868 10.375 4.375 10.8787 4.375 11.5C4.375 12.1213 4.87868 12.625 5.5 12.625Z' fill='currentColor' fill-rule='evenodd' clip-rule='evenodd'></path></svg></div>"
        )

    ui.add_head_html(
        '<link href="https://unpkg.com/eva-icons@1.1.3/style/eva-icons.css" rel="stylesheet" />'
    )
    ui.add_head_html(
        '<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" rel="stylesheet" />'
    )
    ui.add_head_html(
        '<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet" />'
    )
    ui.query(".nicegui-content").classes("p-0")
    with ui.element().classes("bg-white w-screen h-screen m-0"):
        with ui.splitter(limits=(16, 50), value=16).classes("h-full") as splitter:
            with splitter.before:
                Menu()
            with splitter.separator:
                Separator()
            with splitter.after:
                with ui.splitter(limits=(30, 100), value=30).classes("h-full") as splitter2:
                    with splitter2.before:
                        Mail()
                    with splitter2.separator:
                        Separator()
                    with splitter2.after:
                        ReadMail()


ui.run()
