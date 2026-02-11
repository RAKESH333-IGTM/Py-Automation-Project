from core.executor import Executor

class AutomationEngine:
    def __init__(self, registry):
        self.registry = registry
        self.executor = Executor()

    def run(self, task_name, **kwargs):
        task = self.registry.get(task_name)
        if not task:
            raise ValueError(f"Task '{task_name}' not found in registry")

        return self.executor.execute(task, **kwargs)
