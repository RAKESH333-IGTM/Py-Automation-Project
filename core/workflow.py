class WorkflowEngine:
    def __init__(self, automation_engine):
        self.engine = automation_engine

    def run_workflow(self, steps):
        for step in steps:
            task_name = step.get("task")
            params = step.get("params", {})
            self.engine.run(task_name, **params)
