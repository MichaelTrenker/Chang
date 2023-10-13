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