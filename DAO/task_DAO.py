from abc import ABC, abstractmethod
from DAO.DAO import DAO

class TaksDAO(DAO):
    def __init__(self, datasource):
        super().__init__(datasource)

    def add(self, task:dict):
        super().cache.append(task)

    def get(self, id):
        return [task for task in super().cache if task["id"] == id][0]

    def remove(self, id):
        for element in super().cache:
            if int(element["id"]) == int(id):
                super().cache.remove(element)

    def get_all(self):
        return super().cache

    def update(self, task1:dict):
        for element in super().cache:
            if element["id"] == task1["id"]:
                element["title"] = task1["title"]
                element["description"] = task1["description"]
                element["deadline"] = task1["deadline"]
                element["done"] = task1["done"]
                break
