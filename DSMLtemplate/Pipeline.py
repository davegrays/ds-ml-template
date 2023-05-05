# need to add docstrings to everything

from DSMLtemplate.etl import ETL
from DSMLtemplate.proc import Proc
from DSMLtemplate.model import Model

import yaml
from enum import Enum


class PipelineSteps(Enum):
    ETL = "etl"
    PROC = "proc"
    MODEL = "model"


class Pipeline:
    """Model pipeline."""

    def __init__(self, config_yaml_path):
        with open(config_yaml_path, "r") as f:
            self.params = yaml.safe_load(f)

    def run(self, steps=None, etl_output=None, proc_output=None):
        if steps is None:
            steps = [step.value for step in PipelineSteps]
        else:
            invalid_steps = set(steps) - set(step.value for step in PipelineSteps)
            if invalid_steps:
                raise ValueError(f"Invalid steps: {invalid_steps}")

        current_output = None

        if PipelineSteps.ETL.value in steps:
            etl = ETL(self.params)
            etl_output = etl.run()
            current_output = etl_output

        if PipelineSteps.PROC.value in steps:
            proc = Proc(self.params)
            proc_output = proc.run(etl_output)
            current_output = proc_output

        if PipelineSteps.MODEL.value in steps:
            model = Model(self.params)
            model_output = model.run(proc_output)
            current_output = model_output

        return current_output
