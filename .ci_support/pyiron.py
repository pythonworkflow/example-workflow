from python_workflow_definition.pyiron_base import load_workflow_json


if __name__ == "__main__":
    delayed_object_lst = load_workflow_json(file_name="workflow.json")
    print(delayed_object_lst[-1].pull())
