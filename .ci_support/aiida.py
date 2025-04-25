from python_workflow_definition.aiida import load_workflow_json
load_profile()

from aiida import load_profile


if __name__ == "__main__":
    workgraph = load_workflow_json(file_name='workflow.json')
    workgraph.run()
