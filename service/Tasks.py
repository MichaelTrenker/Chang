from enum import Enum

class Task():
    def __init__(self, name, description, status, phase, priority, comment, tags):
        self.name = name
        self.description = description
        self.status = status
        self.phase = phase
        self.priority = priority
        self.comment = comment
        self.tags = tags

    def __str__(self):
        return f"{self.name} {self.description} {self.status} {self.phase} {self.priority} {self.comment} {self.tags}"
class Tag():
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return f"{self.name} {self.color}"
      
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
    

class Status(Enum):
    TODO = 1
    DOING = 2
    DONE = 3
    CANCELLED = 4

class Phase(Enum):
    Reconnaissance = 1,
    Weaponization = 2,
    Delivery = 3,
    Exploitation = 4,
    Installation = 5,
    Command_and_Control = 6,
    Actions_on_Objective = 7,


class Priority(Enum):
    Low = 1
    Medium = 2
    High = 3

    
class Color(Enum):
    lightblue = 1
    orange = 2
    bluegreen = 3
    blue = 4
    violet = 5
    red = 6
    green = 7
    yellow = 8

