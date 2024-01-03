import json
import PySimpleGUI as sg

# from DAO.task_DAO import TaksDAO

class Model:
    def __init__(self, dao):
        self.__dao = dao

    @property
    def dao(self):
        return self.__dao
    
    @dao.setter
    def dao(self, val):
        self.__dao = val
        
    def add_task(self, title, description, deadline):
        task = {
            "id": len(self.__dao.get_all()) + 1,
            "title": title,
            "description": description,
            "deadline": deadline,
            "done": False
        }
        self.__dao.add(task)
    
    def update_task(self, id, title, description, deadline):
        task = {
            "id": id,
            "title": title,
            "description": description,
            "deadline": deadline,
            "done": False
        }
        self.__dao.remove(id)
        self.__dao.add(task)

    def remove_task(self, id):
        self.__dao.remove(id)
    
    def get_all_tasks(self):
        return self.__dao.get_all()
    
    def get_task(self, id):
        return self.__dao.get(id)
    
    def save(self):
        with open("JSON/tasks.json", "w") as file:
            json.dump(self.__dao.get_all(), file)
