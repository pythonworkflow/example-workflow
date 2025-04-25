from aiida import load_profile
load_profile()

from python_workflow_definition.aiida import load_workflow_json


if __name__ == "__main__":
    workgraph = load_workflow_json(file_name='workflow.json')
    workgraph.run()
