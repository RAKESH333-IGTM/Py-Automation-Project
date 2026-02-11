from core.registry import TaskRegistry
from core.engine import AutomationEngine
from core.rules import RuleEngine
from core.workflow import WorkflowEngine
from tasks.sample_tasks import create_folder, move_file, delete_file

def main():
    registry = TaskRegistry()

    # Register tasks
    registry.register("create_folder", create_folder)
    registry.register("move_file", move_file)
    registry.register("delete_file", delete_file)

    engine = AutomationEngine(registry)

    # Load rules
    rule_engine = RuleEngine("config/rules.json")
    workflow_engine = WorkflowEngine(engine)

    # Run workflow
    workflow = rule_engine.get_workflow("daily_cleanup")
    workflow_engine.run_workflow(workflow)

if __name__ == "__main__":

    print("Automation Engine Started")

    print(create_folder("output"))

    print(move_file("data/test.txt", "output/test.txt"))

    print(delete_file("output/test.txt"))
