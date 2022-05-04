class Transport:
    def __init__(self, title, model, color):
        self.title = title
        self.model = model
        self.color = color

    def start_engine(self):
        print(f'ON {self.title} {self.model} engine started')



