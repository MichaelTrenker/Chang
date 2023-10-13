from classes.tag import Tag

class TagService():
    tags = []
    
    def addTag(self, name, color):
        if not name:
            raise ValueError("Name is required")
        self.tags.append(Tag(name, color))

    def getTags(self):
        return self.tags