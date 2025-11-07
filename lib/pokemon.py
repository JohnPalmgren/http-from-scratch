class Pokemon():
    def __init__(self, name, class_type):
        self.name = name
        self.class_type = class_type
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__