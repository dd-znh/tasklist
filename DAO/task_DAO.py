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
        super().cache.remove(task for task in super().cache if task["id"] == id)

    def get_all(self):
        return super().cache

    def update(self, task1:dict):
        if task1["id"] in [task["id"] for task in super().cache]:
            super().cache.remove(task for task in super().cache if task["id"] == task1["id"])
            super().cache.append(task1)


