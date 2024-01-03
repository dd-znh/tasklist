from MVC.view import View
from MVC.model import Model
from DAO.task_DAO import TaksDAO
from MVC.controller import Controller

import sys
sys.dont_write_bytecode = True


class Main:
    def __init__(self):
        dao = TaksDAO("JSON/tasks.json")
        model = Model(dao)
        controller = Controller(View(self), model=model)
        self.controller = controller

    def init(self):
        self.controller.event_loop()

if __name__ == "__main__":
    main = Main()
    main.init()
