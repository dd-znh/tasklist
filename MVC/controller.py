import PySimpleGUI as sg


class Controller:
    def __init__(self, view, model):
        self.__view = view
        self.__model = model

    @property
    def view(self):
        return self.__view
    
    @view.setter
    def view(self, val):
        self.__view = val

    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, val):
        self.__model = val

    def event_loop(self):
        self.__view.menu()
        while True:
            event, values = self.__view.window.read()
            all_tasks = [list(element.values()) for element in self.__model.get_all_tasks()]

            if event == sg.WINDOW_CLOSED or event == "exit":
                self.__model.save()
                break

            if event == "add_task":
                self.__view.window.close()
                self.__view.add_task()

            if event == "list_tasks":
                self.__view.window.close()
                self.__view.list_tasks(all_tasks)

            if event == "update_task":
                self.__view.window.close()
                self.__view.update_task()

            if event == "remove_task":
                self.__view.window.close()
                self.__view.remove_task()

            if event == "add_task#2":
                self.__model.add_task(values["title"], values["description"], values["deadline"])
                sg.Popup("Tarefa adicionada com sucesso!")

            if event == "list_tasks#2":
                sg.Popup("Tarefas:", self.__model.get_all_tasks())

            if event == "update_task#2":
                self.__model.update_task(values["id"], values["title"], values["description"], values["deadline"])
                sg.Popup("Tarefa atualizada com sucesso!")

            if event == "remove_task#2":
                self.__model.remove_task(values["id"])
                sg.Popup("Tarefa removida com sucesso!")

            if event == "back":
                self.__view.window.close()
                self.__view.menu()
