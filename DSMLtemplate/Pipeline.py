from DSMLtemplate.etl import ETL
from DSMLtemplate.proc import Proc
from DSMLtemplate.model import Model

from typing import List
import yaml
from enum import Enum


class PipelineSteps(Enum):
    """Pipeline steps. Used to specify how to name each step in the pipeline."""

    ETL = "etl"
    PROC = "proc"
    MODEL = "model"


class Pipeline:
    """Model pipeline."""

    def __init__(self, config_yaml_path):
        """Initialize pipeline.

        Args:
            config_yaml_path (str): Path to YAML file containing pipeline configuration.
        """
        with open(config_yaml_path, "r") as f:
            self.params = yaml.safe_load(f)

    def run(self, steps: List[str] = None, prev_output: any = None):
        """Run pipeline.

        Args:
            steps (List[str], optional): List of steps to run. If None, run all steps.
            prev_output (any, optional): Output from step previous to first step.
             Defaults to None.

        Returns:
            any: Output from last step.
        """
        if steps is None:
            steps = [step.value for step in PipelineSteps]
        else:
            invalid_steps = set(steps) - set(step.value for step in PipelineSteps)
            if invalid_steps:
                raise ValueError(f"Invalid steps: {invalid_steps}")

        current_output = prev_output

        if PipelineSteps.ETL.value in steps:
            etl = ETL(self.params)
            etl_output = etl.run()
            if etl_output is None:
                raise ValueError("ETL step returned None")
            current_output = etl_output

        if PipelineSteps.PROC.value in steps:
            proc = Proc(self.params)
            proc_output = proc.run(current_output)
            if proc_output is None:
                raise ValueError("PROC step returned None")
            current_output = proc_output

        if PipelineSteps.MODEL.value in steps:
            model = Model(self.params)
            model_output = model.run(current_output)
            if model_output is None:
                raise ValueError("MODEL step returned None")
            current_output = model_output

        return current_output
