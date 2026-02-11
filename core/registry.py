class TaskRegistry:
    def __init__(self):
        self.tasks = {}

    def register(self, name, func):
        self.tasks[name] = func

    def get(self, name):
        return self.tasks.get(name)

    def list_tasks(self):
        return list(self.tasks.keys())
