from nicegui import ui, Client


# def Header():
#     return ui.element().classes("w-full h-16 bg-red-500 ")


# def Menu():

#     Header()
    
#     # with ui.element().classes("h-16 w-full "):
#     #     with ui.column().classes("w-full h-full p-3"):
#     #         data = ["sacha@chu-brest.fr"]
#     #         ui.select(data, value=data[0]).props("dense outlined flex-col ").classes("w-full")

#     #     ui.separator().classes()


# def Mail():
#     Header()
#     # with ui.column().classes("w-full"):
#     #     with ui.element().classes("h-16 w-full "):
#     #         with ui.row().classes(" justify-between h-full flex items-center p-3"):
#     #             ui.label("Inbox").classes("text-xl font-bold  ")
#     #             ui.toggle(["All mail", "Unread"]).props("flat").classes("")
#     #         ui.separator().classes()

#     #     ui.input("test").props("outlined dense ").classes("grow m-3")

#     #     with ui.scroll_area().classes("h-full"):
#     #         for i in range(100):
#     #             with ui.element().classes("w-full border rounded h-50"):
#     #                 with ui.column():
#     #                     with ui.row().classes("justify-around w-full"):
#     #                         ui.label("Lucas Bourneuf").classes("text-md font-bold")
#     #                         ui.label("10 months ago").classes("font-sm")


# def ReadMail():
#     Header()


# def Separator():

#     ui.html(
#         "<div class='z-10 flex h-4 w-3 items-center justify-center rounded-sm border bg-border bg-slate-200'><svg width='25' height='25' viewBox='0 0 15 15' fill='none' xmlns='http://www.w3.org/2000/svg' class='h-2.5 w-2.5'><path d='M5.5 4.625C6.12132 4.625 6.625 4.12132 6.625 3.5C6.625 2.87868 6.12132 2.375 5.5 2.375C4.87868 2.375 4.375 2.87868 4.375 3.5C4.375 4.12132 4.87868 4.625 5.5 4.625ZM9.5 4.625C10.1213 4.625 10.625 4.12132 10.625 3.5C10.625 2.87868 10.1213 2.375 9.5 2.375C8.87868 2.375 8.375 2.87868 8.375 3.5C8.375 4.12132 8.87868 4.625 9.5 4.625ZM10.625 7.5C10.625 8.12132 10.1213 8.625 9.5 8.625C8.87868 8.625 8.375 8.12132 8.375 7.5C8.375 6.87868 8.87868 6.375 9.5 6.375C10.1213 6.375 10.625 6.87868 10.625 7.5ZM5.5 8.625C6.12132 8.625 6.625 8.12132 6.625 7.5C6.625 6.87868 6.12132 6.375 5.5 6.375C4.87868 6.375 4.375 6.87868 4.375 7.5C4.375 8.12132 4.87868 8.625 5.5 8.625ZM10.625 11.5C10.625 12.1213 10.1213 12.625 9.5 12.625C8.87868 12.625 8.375 12.1213 8.375 11.5C8.375 10.8787 8.87868 10.375 9.5 10.375C10.1213 10.375 10.625 10.8787 10.625 11.5ZM5.5 12.625C6.12132 12.625 6.625 12.1213 6.625 11.5C6.625 10.8787 6.12132 10.375 5.5 10.375C4.87868 10.375 4.375 10.8787 4.375 11.5C4.375 12.1213 4.87868 12.625 5.5 12.625Z' fill='currentColor' fill-rule='evenodd' clip-rule='evenodd'></path></svg></div>"
#     )


# @ui.page('/')
# def page():
#     ui.query(".nicegui-content").classes("p-0")
#     with ui.element().classes("bg-white w-screen h-screen m-0"):
#         with ui.splitter(limits=(15, 40), value=15).classes("h-full") as splitter:
#             with splitter.before:
#                 Menu()
#             with splitter.separator:
#                 Separator()
#             with splitter.after:
#                 with ui.splitter(limits=(25, 50), value=25).classes("h-full") as splitter2:
#                     with splitter2.before:
#                         Mail()
#                     with splitter2.separator:
#                         Separator()
#                     with splitter2.after:
#                         ReadMail()




# ui.run(show=False, port=9971)

# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------

# def menu(): 
#     with ui.button().classes("w-[25%] border rounded"):
#         ui.label("blabla")
#         with ui.menu().classes("w-[24%]"):
#             ui.menu_item("1")
#             ui.menu_item("2")
#             ui.menu_item("3")
    
#     ui.separator().classes("w-[25%]")
    
    
    
# def navbar():
#     for i in range(10):
#         with ui.button().classes("w-[25%] border rounded"):
#             with ui.row().classes("w-full"):
#                 ui.icon("home")
#                 ui.label("Matthieu")
#                 ui.space()
#                 ui.label("9")

# menu()
# navbar()

# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------

def navbar():
    with ui.row().classes("flex"):
        with ui.element().classes("flex items-center"):
            ui.label("Inbox").classes("font-bold text-siz-lg")
        
        ui.space() 

        with ui.element().classes("ml-auto"):
            ui.toggle(['All mail', 'Unread']).props("no-caps size=md")
    
        ui.separator()

def searchinput():
    with ui.input(placeholder="Search...").props("outlined"):
        ui.icon("search").props("size=lg")
    # with ui.row().classes("w-full"):
    #     ui.input(placeholder="Search...").props("outlined").classes("w-[19.6%]")

    for i in range(10): 
        with ui.element().classes("border rounded p-2") :
            with ui.row().classes("w-full"):
                ui.label("William Smith").classes("font-semibold flex justify-start")
                ui.space()
                ui.label("10 months ago").classes("ml-auto flex justify-end")

            ui.label("Meeting Tomorrow")
            ui.label("Aperçu du mail...")
            with ui.row():
                ui.button("meeting").props("flat size=sm").classes("text-black")
                ui.button("work").props("color=black size=sm")
                ui.button("important").props("flat size=sm").classes("text-black")





navbar()
searchinput()

# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------

# ui.add_head_html('<link href="https://unpkg.com/eva-icons@1.1.3/style/eva-icons.css" rel="stylesheet" />')
# ui.add_head_html('<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" rel="stylesheet" />')
# ui.add_head_html('<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet" />')


# def navbar():
#         with ui.row().classes("w-full"):
#             with ui.element().classes("flex justify-start gap-3"):
#                 with ui.button(icon="eva-archive-outline").props("flat color=black size=sm"):
#                     ui.tooltip("Archive").classes("bg-black")
#                 with ui.button(icon="eva-trash-outline").props("flat color=black size=sm"):
#                     ui.tooltip("Move to junk").classes("bg-black")
#                 with ui.button(icon="eva-trash-2-outline").props("flat color=black size=sm"):
#                     ui.tooltip("Move to trash").classes("bg-black")
#                 ui.separator().props("vertical")
#                 with ui.button(icon="eva-clock-outline").props("flat color=black size=sm"):
#                     ui.tooltip("Snooze").classes("bg-black")
                
                    

#                 # ui.button(icon="fas fa-box-archive").props("flat color=black size=xs")
#                 # ui.button(icon="delete_outline").props("flat color=black size=sm")
            
#             with ui.element().classes("flex ml-auto gap-3"):
#                 with ui.button(icon="eva-arrow-ios-back-outline").props("flat color=black size=sm"):
#                     ui.tooltip("Reply").classes("bg-black")
#                 with ui.button(icon="eva-arrowhead-left-outline").props("flat color=black size=sm"):
#                     ui.tooltip("Reply all").classes("bg-black")
#                 with ui.button(icon="eva-arrow-ios-forward-outline").props("flat color=black size=sm"):
#                     ui.tooltip("Forward").classes("bg-black")
#                 ui.separator().props("vertical")
#                 with ui.button(icon="eva-more-vertical-outline").props("flat color=black size=sm"):
#                     with ui.menu():
#                         ui.menu_item("Mark as unread")
#                         ui.menu_item("Start thread")
#                         ui.menu_item("Add label")
#                         ui.menu_item("Mute thread")

        
#         ui.separator()



# def contact():
#     with ui.row().classes("w-full"):
#         ui.label("WS").style("padding: 10px; border-radius:50px; background-color: hsl(240,5%,96%)")
#         with ui.element().classes("flex-column"):
#             ui.label("William Smith").classes("font-semibold")
#             ui.label("Meeting Tomorrow")
#             ui.label("Reply-To: williamsmith@example.com")
#         ui.label("Oct 22, 2023, 9:00:00 AM").classes("ml-auto").style("color: hsl(240,4%,46%)")
#         ui.separator()

# def message():
#     with ui.element().classes("h-[45vh]"):
#         ui.label("""
#         Hi, let's have a meeting tomorrow to discuss the project. I've been reviewing the project details and have some ideas I'd like to share. It's crucial that we align on our next steps to ensure the project's success.Please come prepared with any questions or insights you may have. Looking forward to our meeting! Best regards, William
#         """)

#     ui.separator()

# def footer():
#     ui.textarea(placeholder="Reply William Smith...").props("outlined").classes("w-full")
#     with ui.row().classes("w-full"):
#         ui.switch("Mute this thread").props("color=black")
#         ui.button("Send").props("color=slate-900 no-caps").classes("ml-auto")




# navbar()
# contact()
# message()
# footer()



ui.run()