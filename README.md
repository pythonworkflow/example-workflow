# Arithmetic Example Workflow
[![Pipeline](https://github.com/pythonworkflow/example-workflow/actions/workflows/pipeline.yml/badge.svg)](https://github.com/pythonworkflow/example-workflow/actions/workflows/pipeline.yml)

Demonstration for publishing an interoperable workflow based on the Python Workflow Definition. The minimal workflow consists of three files:

| File            | Explanation                                             |
|-----------------|---------------------------------------------------------|
| environment.yml | Conda environment for software dependencies             |
| workflow.py     | Python functions representing the nodes of the workflow |
| workflow.json   | Workflow graph consisting of nodes and edges            |
