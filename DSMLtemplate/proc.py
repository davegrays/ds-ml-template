from DSMLtemplate import utils


class Proc:
    def __init__(self, config: dict):
        self.proc_key = config["PROC_KEY"]

    def run(self, etl_output):
        return utils.get_something(etl_output + self.proc_key)
