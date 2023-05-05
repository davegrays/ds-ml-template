from DSMLtemplate import utils


class Model:
    def __init__(self, config: dict):
        self.model_key = config["MODEL_KEY"]

    def run(self, proc_output):
        return utils.get_something(proc_output + self.model_key)
