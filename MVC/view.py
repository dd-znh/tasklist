import PySimpleGUI as sg


class View:
    def __init__(self, controller):
        self.__controller = controller
        self.__layout = None
        self.__window = None
        self.__size = (800, 600)

    @property
    def layout(self):
        return self.__layout
    
    @layout.setter
    def layout(self, val):
        self.__layout = val

    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, val):
        self.__size = val

    @property
    def window(self):
        return self.__window
    
    @window.setter
    def window(self, val):
        self.__window = val

    @property
    def controller(self):
        return self.__controller

    @controller.setter
    def controller(self, val):
        self.__controller = val

    def menu(self):
        self.__layout = [
            [sg.Text("Escolha uma opção:")],
            [sg.Button("Adicionar tarefa", key="add_task")],
            [sg.Button("Listar tarefas", key="list_tasks")],
            [sg.Button("Atualizar tarefa", key="update_task")],
            [sg.Button("Excluir tarefa", key="remove_task")],
            [sg.Button("Sair", key="exit")]
        ]

        self.__window = sg.Window("Menu", self.__layout)

    def add_task(self):
        self.__layout = [
            [sg.Text("Adicionar tarefa:")],
            [sg.Text("Título:"), sg.InputText(key="title")],
            [sg.Text("Descrição:"), sg.InputText(key="description")],
            [sg.Text("Data de entrega:"), sg.InputText(key="deadline")],
            [sg.Button("Adicionar", key="add_task#2")],
            [sg.Button("Voltar", key="back")]
        ]

        self.__window = sg.Window("Adicionar tarefa", self.__layout)

    def list_tasks(self, tasks):
        self.__layout = [
            [sg.Text("Listar tarefas:")],
            [sg.Listbox(values=tasks, size=(50, 10), key="list_tasks#2")],
            [sg.Button("Voltar", key="back")]
        ]

        self.__window = sg.Window("Listar tarefas", self.__layout)

    def update_task(self):
        self.__layout = [
            [sg.Text("Atualizar tarefa:")],
            [sg.Text("id:"), sg.InputText(key="id")],
            [sg.Text("Título:"), sg.InputText(key="title")],
            [sg.Text("Descrição:"), sg.InputText(key="description")],
            [sg.Text("Data de entrega:"), sg.InputText(key="deadline")],
            [sg.Button("Atualizar", key="update_task#2")],
            [sg.Button("Voltar", key="back")]
        ]

        self.__window = sg.Window("Atualizar tarefa", self.__layout)

    def remove_task(self):
        self.__layout = [
            [sg.Text("Remover tarefa:")],
            [sg.Text("id:"), sg.InputText(key="id")],
            [sg.Button("Remover", key="remove_task#2")],
            [sg.Button("Voltar", key="back")]
        ]

        self.__window = sg.Window("Remover tarefa", self.__layout)
