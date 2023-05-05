from DSMLtemplate import utils


class ETL:
    def __init__(self, config: dict):
        self.etl_key = config["ETL_KEY"]

    def run(self):
        return utils.get_something(self.etl_key)
