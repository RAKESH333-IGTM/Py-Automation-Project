import json

class RuleEngine:
    def __init__(self, rule_file):
        with open(rule_file, "r") as f:
            self.rules = json.load(f)

    def get_workflow(self, workflow_name):
        return self.rules.get(workflow_name, [])
