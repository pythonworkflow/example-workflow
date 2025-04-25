from jobflow.managers.local import run_locally
from python_workflow_definition.jobflow import load_workflow_json


if __name__ == "__main__":
    flow = load_workflow_json(file_name="workflow.json")
    print(run_locally(flow))
