from classes.task import Task
from classes.tag import Tag

class TaskService():
    tasks = []
    tags = []
    def addTask(self, name, description, status, phase, priority,comment, tags):
        if not name:
            raise ValueError("Name is required")
        self.tasks.append(Task(name, description, status, phase, priority,comment, tags))

    def getTasks(self):
        return self.tasks
    
    def addTag(self, name, color):
        if not name:
            raise ValueError("Name is required")
        self.tags.append(Tag(name, color))

    def getTags(self):
        return self.tags